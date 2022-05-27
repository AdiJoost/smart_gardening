# -*- coding: utf-8 -*-
from db import db
from datetime import datetime
from log.logger import Logger
#from pump_controller import Pump_controller

class Order_model(db.Model):
    
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    pump_id = db.Column(db.Integer, db.ForeignKey('pumps.id'))
    pump = db.relationship('Pump_model')
    duration = db.Column(db.Integer)
    execution_date = db.Column(db.DateTime)
    is_done = db.Column(db.Boolean)
    
    def __init__(self, pump_id: int, duration: int, execution_date=None):
        self.pump_id = pump_id
        self.duration = duration
        self.is_done = False
        if execution_date:
            self.execution_date = execution_date
        else:
            self.execution_date = datetime.today()
    
    def to_json (self) -> str:
        return {"id" : self.id,
                "pump_id": self.pump_id,
                "duration": self.duration,
                "execution_date": self.execution_date,
                "is_done": self.is_done,
                "pump": self.pump.to_json()}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        
    def deleteMe(self):
        db.session.delete(self)
        db.session.commit()
    
    def done(self, app):
        with app.app_context():
            self.is_done = True
            self.save()
        
        
    @classmethod
    def get_order(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_all (cls):
        return cls.query.all()
    
    #todo not returning objects but rather list file (working on other thread)
    @classmethod
    def get_open_orders(cls, app):
        try:
            with app.app_context():
                orders = cls.query.filter_by(is_done=False).all()
                now = datetime.today()
                return_value = [order
                                for order in orders
                                if order.execution_date < now]
                
                
        except Exception as e:
            Logger.log(__name__, str(e), "error_log.txt")
            return_value = None
        finally:    
            return return_value
        
    @classmethod
    def deamon_create(cls, app, pump_id, duration, dt):
        with app.app_context():
            order = Order_model(pump_id, duration, execution_date=dt)
            Logger.log(__name__, f"created order: {order}"\
                       f"\nargs: ({pump_id}, {duration}, {dt})")
            order.save()
        
            