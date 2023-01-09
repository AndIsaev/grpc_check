from dataclasses import asdict

import grpc

from client.fake_data import USERS
from permission_service import server_pb2
from permission_service import server_pb2_grpc


def get_permission(stub):

    for user in USERS:
        response = stub.GetPermission(server_pb2.PermissionRequest(user=asdict(user)))
        print(response)


def run():
    print("Trying to get permissions ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = server_pb2_grpc.PermissionStub(channel)
        get_permission(stub)


if __name__ == '__main__':
    run()
