from flask_restful import reqparse
from flask import make_response, jsonify

 

      
    
def create_response (body, status):
    response = make_response(jsonify(body), status)
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000')
    return response





#Below are all methods to create a parser for a specific Request
def order_put_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("duration",
                        type=int,
                        required=True,
                        help="This field cannot be left blank")
    return parser
