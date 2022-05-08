from flask_restful import Resource
from models.pump_model import Pump_model
from utilities import create_response, order_put_parser
from pump_controller import Pump_controller

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
        pc = Pump_controller.get_instance()
        pc.add_pump(my_pump.id, my_pump.pump_pin)
        return create_response(my_pump.to_json() ,201)
    
    def delete (self, _id):
        my_pump = Pump_model.get_pump(_id)
        if my_pump:
            my_pump.deleteMe()
        return create_response("pump deleted", 200)
    
    def put(self, _id):
        my_pump = Pump_model.get_pump(_id)
        if not my_pump:
            return create_response({"message": f"No Pump with id: {_id} exists"},
                                   404)
        
        return_value = {}
        parser = order_put_parser()
        data = parser.parse_args()
        pc = Pump_controller.get_instance()
        return_value["queue_before"] = str(pc.queue)
        pc.add_order(_id, data["duration"])
        return_value["queue_middle"] = str(pc.queue)
        
        pc.run_queue()
        return_value["queue_after"] = str(pc.queue)
        
        return create_response (return_value, 200)
        
    
class Res_pumps(Resource):
    def get(self):
        all_pumps = Pump_model.get_all()
        return_value = {}
        for pump in all_pumps:
            return_value[pump.id] = pump.to_json()
        return create_response (return_value, 200)