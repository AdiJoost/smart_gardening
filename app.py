from flask import Flask
from pump import Pump

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    pump_21 = Pump(21)
    pump_21.activate_pump(10)
    return "Hello world"


if __name__ == "__main__":
    
    app.run(port=5000, host="0.0.0.0", debug=True)