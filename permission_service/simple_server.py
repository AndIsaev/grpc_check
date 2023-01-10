from concurrent import futures
import logging

import grpc
import server_pb2
import server_pb2_grpc


class Permission(server_pb2_grpc.PermissionServicer):

    def SendPermission(self, request, context):
        permission = False
        if request.user.role == server_pb2.User.Role.ADMIN:
            permission = True

        body = server_pb2.PermissionBody(
            id=request.user.id,
            name=request.user.name,
            result=permission
        )

        return server_pb2.PermissionResponse(response=body)


def run_server():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_PermissionServicer_to_server(Permission(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    run_server()
