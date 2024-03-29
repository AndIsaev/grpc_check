# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class PermissionStub(object):
    """The permission service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPermission = channel.unary_unary(
                '/tutorial.Permission/SendPermission',
                request_serializer=server__pb2.PermissionRequest.SerializeToString,
                response_deserializer=server__pb2.PermissionResponse.FromString,
                )


class PermissionServicer(object):
    """The permission service.
    """

    def SendPermission(self, request, context):
        """schema rout
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PermissionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPermission,
                    request_deserializer=server__pb2.PermissionRequest.FromString,
                    response_serializer=server__pb2.PermissionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tutorial.Permission', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Permission(object):
    """The permission service.
    """

    @staticmethod
    def SendPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tutorial.Permission/SendPermission',
            server__pb2.PermissionRequest.SerializeToString,
            server__pb2.PermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StatusStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendStatus = channel.unary_unary(
                '/tutorial.Status/SendStatus',
                request_serializer=server__pb2.StatusRequest.SerializeToString,
                response_deserializer=server__pb2.StatusResponse.FromString,
                )


class StatusServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.SendStatus,
                    request_deserializer=server__pb2.StatusRequest.FromString,
                    response_serializer=server__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tutorial.Status', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Status(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tutorial.Status/SendStatus',
            server__pb2.StatusRequest.SerializeToString,
            server__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
