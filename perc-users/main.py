from concurrent import futures
from signal import signal, SIGTERM
import grpc
from grpc_interceptor import ServerInterceptor
from PercUsers_pb2 import (
    CreateUserResponse,
    GetUserAllResponse,
    SearchUsersResponse
)
import PercUsers_pb2_grpc
from services import (CreateUser, GetAllUser, SearchUsers)
from google.protobuf.json_format import Parse
from google.protobuf.json_format import MessageToDict

class PercUsersService(PercUsers_pb2_grpc.PercUsersServicer):
    
    """_summary_
        Function that obtains payload from services api and pass to the CreateUser service
    Returns:
        _type_: response serialize to CreateUserResponse
    """
    def CreateUser(self, request, context):
        name = request.name
        username = request.username
        email = request.email
        httpCode, name, username, email, messaje = CreateUser(name=name, username=username, email=email)
        return CreateUserResponse(httpCode=httpCode, name=name, username=username, email=email, messaje=messaje)
    
    """_summary_
        Get request an serialize the response to show all users
    Returns:
        _type_: response serialize to GetUserAllResponse
    """ 
    def GetAllUser(self, request, context):
        httpCode, payload = GetAllUser()
        user_response = GetUserAllResponse()
        conta = 0
        for user_data in payload:
            conta = conta + 1
            user = user_response.users.add()
            user.name = user_data["name"]
            user.city = user_data["address"]["city"]
            user.company = user_data["company"]["name"]
            # user.id = user_data["id"]
            # user.name = user_data["name"]
            # user.username = user_data["username"]
            # user.email = user_data["email"]

            # user.address.street = user_data["address"]["street"]
            # user.address.suite = user_data["address"]["suite"]
            # user.address.city = user_data["address"]["city"]
            # user.address.zipcode = user_data["address"]["zipcode"]
            # user.address.geo.lat = user_data["address"]["geo"]["lat"]
            # user.address.geo.lng = user_data["address"]["geo"]["lng"]

            # user.phone = user_data["phone"]
            # user.website = user_data["website"]
            # user.company.name = user_data["company"]["name"]
            # user.company.catchPhrase = user_data["company"]["catchPhrase"]
            # user.company.bs = user_data["company"]["bs"]
        user_response.totalUsers = conta
        return user_response
        
    """_summary_
        Get request an serialize the response to filter and sort users
    Returns:
        _type_: response serialize to SearchUsersResponse
    """ 
    def SearchUsers(self, request, context):
        httpCode, payload = SearchUsers(request)
        search_user_response = SearchUsersResponse()
        conta = 0
        for user_data in payload:
            conta = conta + 1
            user = search_user_response.users.add()
            user.name = user_data["name"]
            user.city = user_data["address"]["city"]
            user.company = user_data["company"]["name"]
        search_user_response.totalUsers = conta
        return search_user_response
    
class ErrorLogger(ServerInterceptor):
    
    """_summary_
        Function that intercept messaje from api service 
    Returns:
        _type_: request
    """
    def intercept(self, method, request, context, method_name):
        try:
            return method(request, context)
        except Exception as e:
            self.log_error(e)
            raise

    def log_error(self, e: Exception) -> None:
        print(str(e))

"""_summary_
    Up the service by port 50057
Returns:
    
"""
def serve():
    interceptors = [ErrorLogger()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    PercUsers_pb2_grpc.add_PercUsersServicer_to_server(
        PercUsersService(), server
    )
    
    server.add_insecure_port("[::]:50057")
    server.start()
    print("PERC-USERS-SVC GRPC SERVER running")
    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)

    server.wait_for_termination()


if __name__ == "__main__":
    serve()