from functools import wraps
from flask import jsonify, make_response, request
import os
import grpc
from src.proto.authentication.authentication_pb2_grpc import AuthenticationStub
from src.proto.authentication.authentication_pb2 import (
    ValidateTokenRequest,
)
from google.protobuf.json_format import MessageToDict

authentication_host = os.getenv("AUTH_SERVICE_HOST", "localhost:50052")
authentication_channel = grpc.insecure_channel(
    f"{authentication_host}"
)
authentication_client = AuthenticationStub(authentication_channel)

# Authentication decorator
def authentication_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            token = None
            # ensure the jwt-token is passed with the headers
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].replace('Bearer ', '')
            if not token: # throw error if no token provided
                return make_response(jsonify({"message": "A valid token is missing!"}), 401)
            validate_token_request = ValidateTokenRequest(token=token)
            validate_token_response = authentication_client.ValidateToken(validate_token_request)
            json_validate_token_response = MessageToDict(validate_token_response)
            valid = json_validate_token_response.get('valid', False)
            #En protofubs, las variables bool que son falso no viajan, para no gastar espacio
            if(not valid):
                return make_response(jsonify({"message": json_validate_token_response["message"]}), 401)
            
            return fn(*args, **kwargs)
        
        return decorator

    return wrapper