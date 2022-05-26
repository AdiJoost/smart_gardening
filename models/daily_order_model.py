# -*- coding: utf-8 -*-
from db import db
#from datetime import datetime
#from log.logger import Logger
#from pump_controller import Pump_controller

class Daily_order_model(db.Model):
    
    __tablename__ = 'daily_orders'
    id = db.Column(db.Integer, primary_key=True)
    pump_id = db.Column(db.Integer, db.ForeignKey('pumps.id'))
    pump = db.relationship('Pump_model')
    duration = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    
    def __init__(self, pump_id: int, duration: int, hour: int, minute: int):
        if hour > 23 or hour < 0:
            raise ValueError("hour must be between 0 and 23.")
        if minute > 59 or minute < 0:
            raise ValueError("Minute must be beween 0 an 59")
        self.pump_id = pump_id
        self.duration = duration
        self.hour = hour
        self.minute = minute
        
        
    
    def to_json (self) -> str:
        return {"id" : self.id,
                "pump_id": self.pump_id,
                "duration": self.duration,
                "hour": self.hour,
                "minute": self.minute,
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
        
        """
    def place(self):
        ""place will put the order in queue, however, if the app
        crashes while order is in queue, the order is marked complete,
        but never actually shot.""
        pc = Pump_controller.get_instance()
        pc.add_order(self.pump_id, self.duration)
        self.is_done = True
        self.save()"""
        
    @classmethod
    def get_order(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_all (cls):
        return cls.query.all()
    
    @classmethod
    def get_deamon_orders(cls, app):
        
        with app.app_context():
            return cls.query.all()
                