from functools import wraps
from flask import Blueprint, jsonify, make_response, request, abort
import json
from flask import request
import grpc
import os
from google.protobuf.json_format import MessageToDict
from src.proto.perc_users.PercUsers_pb2_grpc import PercUsersStub
from src.proto.perc_users.PercUsers_pb2 import (
    CreateUserRequest,
    GetUserAllRequest,
    SearchUsersRequest
)
from src.utils.decorators.authentication_decorator import authentication_required
from src.utils.schemas.perc_users.schemas import (
    CreateUserSchema, SearchUsers
)
from marshmallow import Schema, fields, ValidationError
from google.protobuf.json_format import Parse, ParseDict


# Comunicate whit perc users services by grpc proto microservices
perc_users_host = os.getenv("PERC_USERS_SVC_SERVICE_HOST", "localhost:50057")
perc_users_service_channel = grpc.insecure_channel(
    f"{perc_users_host}"
)
perc_users_service_client = PercUsersStub(perc_users_service_channel)
perc_service_bp = Blueprint('perc_service_bp', __name__, url_prefix='/api/v1/PercServices')

"""
    function to comunicate with services create users
    Returns:
        _type_: payload
"""
@perc_service_bp.route('/CreateUser', methods=['POST'])
#@authentication_required()
def create_user():
    request_data = request.get_json()
    schema = CreateUserSchema()
    
    try:
        # Validate request body against schema data types
        validated_request_json = schema.load(request_data)
        
        # Object CreateUserRequest 
        perc_users_request = ParseDict(validated_request_json, CreateUserRequest())
        
        # Call to CreateUser services proto
        perc_users_response = perc_users_service_client.CreateUser(
            perc_users_request
        )
        
        # Get response and converto to python dict
        perc_users_response_dict = MessageToDict(perc_users_response)
        
        return jsonify({
            "status": perc_users_response_dict['httpCode'],
            "data": perc_users_response_dict,
        }), perc_users_response_dict['httpCode']

    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400


"""
    function to comunicate with services get all user
    Returns:
        _type_: payload
"""
@perc_service_bp.route('/GetAllUser', methods=['GET'])
# @authentication_required()
def get_all_users():
    try:
        get_all_users_request = GetUserAllRequest()
        get_all_users_response = perc_users_service_client.GetAllUser(
            get_all_users_request
        )
        get_all_users_response_dict = MessageToDict(get_all_users_response)
        
        return get_all_users_response_dict

    except Exception as err:
        # Return a nice message if validation fails
        return err, 400


"""
    function to filter user 
    Returns:
        _type_: payload
"""
@perc_service_bp.route('/SearchUsers', methods=['POST'])
#@authentication_required()
def search_user():
    request_data = request.get_json()
    schema = SearchUsers()
    
    try:
        # Validate request body against schema data types
        validated_request_json = schema.load(request_data)
        
        # Object CreateUserRequest 
        perc_search_users_request = ParseDict(validated_request_json, SearchUsersRequest())
        
        # Call to CreateUser services proto
        perc_search_users_response = perc_users_service_client.SearchUsers(
            perc_search_users_request
        )
        
        # Get response and converto to python dict
        perc_search_users_response_dict = MessageToDict(perc_search_users_response)
        
        return perc_search_users_response_dict
        
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400





