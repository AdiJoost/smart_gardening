from db import db

class Pump_model(db.Model):
    
    __tablename__ = 'pumps'
    id = db.Column(db.Integer, primary_key=True)
    pump_pin = db.Column(db.Integer)
    
    def __init__(self, pump_pin: int):
        self.pump_pin = pump_pin
        
    def to_json (self) -> str:
        return {"id" : self.id,
                "pump_pin": self.pump_pin,
                "type": "pump"}
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def deleteMe(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def get_pump(cls, _id: int):
        return cls.query.filter_by(id=_id).first()