from flask import Flask
from flask_restful import Api
from db import db
#when run on Pi -make sure to uncomment the RPI.GPIO lib in Pump-class
from pump import Pump
from resources.res_pump import Res_pump


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

@app.route('/', methods=['GET'])
def home():
    for my_pump in all_pumps:
        my_pump.activate_pump(3)
    return "Hello world"

api.add_resource(Res_pump, "/pump/<int:_id>")

if __name__ == "__main__":
    for pin in pin_list:
        print(f"Going to add pump_pin {pin}")
        all_pumps.append(Pump(pin))
        print("Pin added")
    db.init_app(app)
    app.run(port=5000, host="0.0.0.0", debug=True)