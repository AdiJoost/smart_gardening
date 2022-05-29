from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from db import db
#when run on Pi -make sure to uncomment the RPI.GPIO lib in Pump-class
from resources.res_pump import Res_pump, Res_pumps
from resources.res_order import Res_order, Res_orders
from resources.res_daily_order import Res_daily_order, Res_daily_orders
from pump_controller import Pump_controller
from log.logger import Logger


app = Flask(__name__)
CORS(app)
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
    Logger.log(__name__, "setup pumpcontroller")
    pc = Pump_controller()
    pc.start_deamon_thread(app)
    Logger.log(__name__, "setup completed\n*****************************")

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

api.add_resource(Res_pump, "/pump/<int:_id>")
api.add_resource(Res_pumps, "/pumps")
api.add_resource(Res_order, "/order")
api.add_resource(Res_orders, "/orders")
api.add_resource(Res_daily_order, "/daily_order")
api.add_resource(Res_daily_orders, "/daily_orders")

if __name__ == "__main__":
    Logger.log(__name__, "\n*****************************\n"\
               "Start application")
    #setup DB
    db.init_app(app)
    
    #start app
    app.run(port=5000, host="0.0.0.0", debug=True)
    