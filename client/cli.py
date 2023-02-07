from dataclasses import asdict

import grpc

from fake_data import USERS
import server_pb2
import server_pb2_grpc


def get_permission(stub):

    for user in USERS:
        response = stub.SendPermission(server_pb2.PermissionRequest(user=asdict(user)))
        print(response)


def get_status(stub):
    print(stub.SendStatus(server_pb2.StatusRequest(status='200')))


def run_client():
    print("Trying to get permissions ...")
    with grpc.insecure_channel('permission_service:50051') as channel:
        permission_stub = server_pb2_grpc.PermissionStub(channel)
        status_stub = server_pb2_grpc.StatusStub(channel)
        get_permission(permission_stub)
        get_status(status_stub)


if __name__ == '__main__':
    run_client()
