from concurrent import futures
import logging
import time

import grpc
import user_pb2_grpc
import user_pb2
import services

def get_status(status_db, user):
    for status in status_db:
        if status.data == user:
            return status
    return None

class Server(user_pb2_grpc.RouteGuideServicer):

    def __init__(self):
        self.db = services.read_JSONs()

    def GetStatus(self, request, context):

        status = get_status(self.db, request)
        if status is None:

            return user_pb2.Status(status="not Known", data=request)
        else:

            return (status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_RouteGuideServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:40')
    print("server running at port: 40")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()