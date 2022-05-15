from flask_restful import reqparse
from flask import make_response, jsonify
from datetime import datetime

 

      
    
def create_response (body, status):
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response

def get_datetime(input_string: str) -> datetime:
    splitted = input_string.split("-")
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    hour = int(splitted[3])
    minute = int(splitted[4])
    seconds = int(splitted[5])
    return datetime(year, month, day, hour, minute, seconds)



#Below are all methods to create a parser for a specific Request
def order_put_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("duration",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    return parser

def order_post_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("pump_id",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("duration",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("time_date",
                        type=str,
                        required=False,
                        help="This field has to be formatet like"\
                            "yyyy-MM-dd-hh-mm-ss")
    return parser