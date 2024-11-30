"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from . import PercUsers_pb2 as PercUsers__pb2
GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in PercUsers_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class PercUsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary('/users.PercUsers/CreateUser', request_serializer=PercUsers__pb2.CreateUserRequest.SerializeToString, response_deserializer=PercUsers__pb2.CreateUserResponse.FromString, _registered_method=True)
        self.GetAllUser = channel.unary_unary('/users.PercUsers/GetAllUser', request_serializer=PercUsers__pb2.GetUserAllRequest.SerializeToString, response_deserializer=PercUsers__pb2.GetUserAllResponse.FromString, _registered_method=True)
        self.SearchUsers = channel.unary_unary('/users.PercUsers/SearchUsers', request_serializer=PercUsers__pb2.SearchUsersRequest.SerializeToString, response_deserializer=PercUsers__pb2.SearchUsersResponse.FromString, _registered_method=True)

class PercUsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_PercUsersServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateUser': grpc.unary_unary_rpc_method_handler(servicer.CreateUser, request_deserializer=PercUsers__pb2.CreateUserRequest.FromString, response_serializer=PercUsers__pb2.CreateUserResponse.SerializeToString), 'GetAllUser': grpc.unary_unary_rpc_method_handler(servicer.GetAllUser, request_deserializer=PercUsers__pb2.GetUserAllRequest.FromString, response_serializer=PercUsers__pb2.GetUserAllResponse.SerializeToString), 'SearchUsers': grpc.unary_unary_rpc_method_handler(servicer.SearchUsers, request_deserializer=PercUsers__pb2.SearchUsersRequest.FromString, response_serializer=PercUsers__pb2.SearchUsersResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('users.PercUsers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('users.PercUsers', rpc_method_handlers)

class PercUsers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.PercUsers/CreateUser', PercUsers__pb2.CreateUserRequest.SerializeToString, PercUsers__pb2.CreateUserResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetAllUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.PercUsers/GetAllUser', PercUsers__pb2.GetUserAllRequest.SerializeToString, PercUsers__pb2.GetUserAllResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SearchUsers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/users.PercUsers/SearchUsers', PercUsers__pb2.SearchUsersRequest.SerializeToString, PercUsers__pb2.SearchUsersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)