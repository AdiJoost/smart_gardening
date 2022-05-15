from flask import Flask
from flask_restful import Api
from db import db
#when run on Pi -make sure to uncomment the RPI.GPIO lib in Pump-class
from pump import Pump
from resources.res_pump import Res_pump, Res_pumps
from pump_controller import Pump_controller


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "LolHAHAHA"
pin_list = (20, 21, 26, 19, 13, 6, 5, 12)
all_pumps = []
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()
    #create instance of Pump_controller
    pc = Pump_controller()
    pc.start_deamon_thread()

@app.route('/', methods=['GET'])
def home():
    for my_pump in all_pumps:
        my_pump.activate_pump(3)
    return "Hello world"

api.add_resource(Res_pump, "/pump/<int:_id>")
api.add_resource(Res_pumps, "/pumps")

if __name__ == "__main__":
    
    #setup DB
    db.init_app(app)
    
    #start app
    app.run(port=5000, host="0.0.0.0", debug=True)
    