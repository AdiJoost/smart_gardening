from flask_restful import Resource
from models.pump_model import Pump_model

class Res_pump(Resource):
    def get(self, _id):
        my_pump = Pump_model.get_pump(_id)
        return my_pump.to_json()
    
    #on the post method _id is the pin to setup the Pump
    def post (self, _id):
        my_pump = Pump_model(_id)
        my_pump.save()
        return 201
    
    def delete (self, _id):
        my_pump = Pump_model.get_pump(_id)
        my_pump.delete()
        return 200