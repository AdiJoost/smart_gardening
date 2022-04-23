from flask import Flask
from flask_restful import Api
from db import db
#when run on pi, uncomment all lines run with Pump module
#from pump import Pump

app = Flask(__name__)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return "Hello world"


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, host="0.0.0.0", debug=True)