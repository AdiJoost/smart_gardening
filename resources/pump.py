from flask_restful import Resource
from models.pump_model import Pump_model

class Pump(Resource):
    def get(self, _id):
        pass
    
    #on the post method _id is the pin to setup the Pump
    def post (self, _id):
        pass
    
    def delete (self, _id):
        pass