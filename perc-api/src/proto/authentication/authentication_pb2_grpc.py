"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import authentication_pb2 as authentication__pb2

class AuthenticationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary('/authentication.Authentication/Login', request_serializer=authentication__pb2.LoginRequest.SerializeToString, response_deserializer=authentication__pb2.LoginResponse.FromString)
        self.SignUp = channel.unary_unary('/authentication.Authentication/SignUp', request_serializer=authentication__pb2.SignUpRequest.SerializeToString, response_deserializer=authentication__pb2.SignUpResponse.FromString)
        self.ValidateToken = channel.unary_unary('/authentication.Authentication/ValidateToken', request_serializer=authentication__pb2.ValidateTokenRequest.SerializeToString, response_deserializer=authentication__pb2.ValidateTokenResponse.FromString)

class AuthenticationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignUp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AuthenticationServicer_to_server(servicer, server):
    rpc_method_handlers = {'Login': grpc.unary_unary_rpc_method_handler(servicer.Login, request_deserializer=authentication__pb2.LoginRequest.FromString, response_serializer=authentication__pb2.LoginResponse.SerializeToString), 'SignUp': grpc.unary_unary_rpc_method_handler(servicer.SignUp, request_deserializer=authentication__pb2.SignUpRequest.FromString, response_serializer=authentication__pb2.SignUpResponse.SerializeToString), 'ValidateToken': grpc.unary_unary_rpc_method_handler(servicer.ValidateToken, request_deserializer=authentication__pb2.ValidateTokenRequest.FromString, response_serializer=authentication__pb2.ValidateTokenResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('authentication.Authentication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Authentication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authentication.Authentication/Login', authentication__pb2.LoginRequest.SerializeToString, authentication__pb2.LoginResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignUp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authentication.Authentication/SignUp', authentication__pb2.SignUpRequest.SerializeToString, authentication__pb2.SignUpResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateToken(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authentication.Authentication/ValidateToken', authentication__pb2.ValidateTokenRequest.SerializeToString, authentication__pb2.ValidateTokenResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)