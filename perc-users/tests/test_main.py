import grpc
import PercUsers_pb2
import PercUsers_pb2_grpc
from concurrent import futures
import pytest
from main import serve
from grpc_testing import server_from_dictionary
from PercUsers_pb2_grpc import PercUsersServicer, add_PercUsersServicer_to_server
from PercUsers_pb2 import CreateUserRequest, CreateUserResponse

class TestPercUsersService(PercUsersServicer):
    """Mock implementation of PercUsersService."""
    def CreateUser(self, request, context):
        return CreateUserResponse(
            httpCode=201,
            name=request.name,
            username=request.username,
            email=request.email,
            messaje="User created success"
        )
        
@pytest.fixture
def grpc_server():
    """Fixture to set up a test GRPC server."""
    test_server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_PercUsersServicer_to_server(TestPercUsersService(), test_server)
    test_server.add_insecure_port("[::]:50057")
    test_server.start()
    yield test_server
    test_server.stop(None)
    
def test_create_user(grpc_server):
    """Integration test for CreateUser."""
    channel = grpc.insecure_channel("[::]:50057")
    stub = PercUsers_pb2_grpc.PercUsersStub(channel)
    request = CreateUserRequest(name="John", username="john123", email="john@example.com")
    response = stub.CreateUser(request)
    
    assert response.httpCode == 201
    assert response.name == "John"
    assert response.username == "john123"
    assert response.email == "john@example.com"
    assert response.messaje == "User created success"