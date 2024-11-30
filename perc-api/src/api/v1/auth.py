from flask import Blueprint, jsonify, make_response, request, abort
import json
import grpc
import os
from google.protobuf.json_format import MessageToDict
from src.proto.authentication.authentication_pb2_grpc import AuthenticationStub
from src.proto.authentication.authentication_pb2 import (
    LoginRequest,
    SignUpRequest,
)

authentication_host = os.getenv("AUTH_SERVICE_HOST", "localhost:50052")
authentication_channel = grpc.insecure_channel(
    f"{authentication_host}"
)
authentication_client = AuthenticationStub(authentication_channel)


auth_bp = Blueprint('auth-bp', __name__, url_prefix='/ccp/v1')

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     request_data = request.get_json()
#     username = request_data.get('username')
#     password = request_data.get('password')
#     login_request = LoginRequest(username=username, password=password)
#     login_response = authentication_client.Login(login_request)
#     json_login_response = MessageToDict(login_response)
    
#     return jsonify({
#         "status": 200,
#         "data": json_login_response
#     })

@auth_bp.route('/login', methods=['POST'])
def login():
    # Verifica el tipo de contenido de la solicitud para decidir cómo procesarla
    if request.content_type == 'application/json':
        request_data = request.get_json()  # Procesa JSON
        if request_data is None:
            abort(400, description="Invalid JSON")
    elif request.content_type == 'application/x-www-form-urlencoded':
        request_data = request.form.to_dict()  # Procesa datos de formulario codificados
    else:
        abort(400, description="Unsupported Content Type")

    # Obtiene los datos del usuario de request_data, que puede ser JSON o form-data
    username = request_data.get('username')
    password = request_data.get('password')
    
    if not username or not password:
        abort(400, description="Username or password not provided")

    # Aquí iría la lógica para crear el objeto de solicitud y llamar a gRPC
    # Por ejemplo:
    login_request = LoginRequest(username=username, password=password)
    try:
        login_response = authentication_client.Login(login_request)
        json_login_response = MessageToDict(login_response)
        return jsonify({"status": 200, "data": json_login_response})
    except Exception as e:
        # abort(500, description=str(e))
        return jsonify({
            "status": 200,
            "data": "Username or password incorrect"
        })
    
    
    

@auth_bp.route('/signup', methods=['POST'])
def signup():
    request_data = request.get_json()
    username = request_data.get('username')
    password = request_data.get('password')
    email = request_data.get('email')
    is_admin = request_data.get('is_admin')
    signup_request = SignUpRequest(username=username, password=password, email=email, is_admin=is_admin)
    signup_response = authentication_client.SignUp(signup_request)
    json_login_response = MessageToDict(signup_response, including_default_value_fields=True,
                                        preserving_proto_field_name=True)
    
    return jsonify({
        "status": 200,
        "data": json_login_response
    })

@auth_bp.route('/test', methods=['GET'])
def test():
    
    return jsonify({
        "status": 200,
        "data": "ccp-api-gateway-all-services 31-08-2023"
    })