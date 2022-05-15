from flask_restful import Resource
from datetime import datetime
from models.order_model import Order_model
from utilities import create_response, order_put_parser, order_post_parser,\
get_datetime
from pump_controller import Pump_controller


class Res_order(Resource):
    def get(self):
        pass
    
    #on the post method _id is the pin to setup the Pump
    def post (self):
        parser = order_post_parser()
        data = parser.parse_args()
        my_datetime = get_datetime(data["time_date"])
        order = Order_model(data["pump_id"],
                            data["duration"],
                            execution_date=my_datetime)
        order.save()
        return create_response(order.to_json(), 200)
    
    def delete (self):
        pass
    
    def put(self):
        
        
        return_value = {}
        parser = order_put_parser()
        data = parser.parse_args()
        pc = Pump_controller.get_instance()
        return_value["queue_before"] = str(pc.queue)
        pc.add_order()#pump_id data["duration"])
        return_value["queue_middle"] = str(pc.queue)
        
        #pc.run_queue()
        return_value["queue_after"] = str(pc.queue)
        
        return create_response (return_value, 200)
        
    
class Res_orders(Resource):
    def get(self):
        all_orders = Order_model.get_all()
        return_value = {}
        for order in all_orders:
            return_value[order.id] = order.to_json()
        return create_response (return_value, 200)