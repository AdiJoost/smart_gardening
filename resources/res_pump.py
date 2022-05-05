from flask_restful import Resource
from models.pump_model import Pump_model
from utilities import create_response

class Res_pump(Resource):
    def get(self, _id):
        my_pump = Pump_model.get_pump(_id)
        if my_pump:
            return create_response(my_pump.to_json(), 200)
        return create_response({"message": f"Pump with id:{_id} not found"},
                               404)
    
    #on the post method _id is the pin to setup the Pump
    def post (self, _id):
        my_pump = Pump_model(_id)
        my_pump.save()
        return create_response(my_pump.to_json() ,201)
    
    def delete (self, _id):
        my_pump = Pump_model.get_pump(_id)
        if my_pump:
            my_pump.deleteMe()
        return create_response("pump deleted", 200)