from flask import Flask
from flask_restful import Api
from db import db
#when run on Pi -make sure to uncomment the RPI.GPIO lib in Pump-class
from pump import Pump

app = Flask(__name__)
pin_list = (20, 21, 26, 19, 13, 6, 5, 12)
all_pumps = []

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    for my_pump in all_pumps:
        my_pump.activate_pump(3)
    return "Hello world"


if __name__ == "__main__":
    for pin in pin_list:
        print(f"Going to add pump_pin {pin}")
        all_pumps.append(Pump(pin))
        print("Pin added")
    db.init_app(app)
    app.run(port=5000, host="0.0.0.0", debug=True)