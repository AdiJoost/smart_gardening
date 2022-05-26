from flask_restful import Resource
from datetime import datetime
from models.daily_order_model import Daily_order_model
from utilities import create_response, daily_order_post_parser, \
get_datetime
from pump_controller import Pump_controller
from log.logger import Logger


class Res_daily_order(Resource):
    def get(self):
        pass
    
    def post (self):
        return_value = {}
        parser = daily_order_post_parser()
        data = parser.parse_args()
        try:
            daily_order = Daily_order_model(data["pump_id"],
                                            data["duration"],
                                            data["hour"],
                                            data["minute"])
            daily_order.save()
            return_value["message"] = "daily order created"
            return_value["daily_order"] = daily_order.to_json()
        except ValueError as e:
            Logger.log(__name__, str(e), "error_log.txt")
            return_value["message"] = str(e)
        
        
        return create_response(return_value, 201)
    
    def delete (self):
        pass
    
    def put(self):
        pass
        
    
class Res_daily_orders(Resource):
    def get(self):
        all_orders = Daily_order_model.get_all()
        return_value = {}
        for order in all_orders:
            return_value[order.id] = order.to_json()
        return create_response (return_value, 200)