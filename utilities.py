#from flask_restful import reqparse
from flask import make_response, jsonify

 

      
    
def create_response (body, status):
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response




"""
#Below are all methods to create a parser for a specific Request
def employee_post_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("monday",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("tuesday",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("wednesday",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("thursday",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    parser.add_argument("friday",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    return parser
"""