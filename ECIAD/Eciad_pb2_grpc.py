# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ECIAD_pb2 as Fame_dot_Eciad__pb2


class ECIADStub(object):
    """The ECIAD service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EciadTask = channel.stream_stream(
                '/FAME.ECIAD.ECIAD/EciadTask',
                request_serializer=Fame_dot_Eciad__pb2.EciadRequest.SerializeToString,
                response_deserializer=Fame_dot_Eciad__pb2.EciadResponse.FromString,
                )


class ECIADServicer(object):
    """The ECIAD service definition.
    """

    def EciadTask(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ECIADServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EciadTask': grpc.stream_stream_rpc_method_handler(
                    servicer.EciadTask,
                    request_deserializer=Fame_dot_Eciad__pb2.EciadRequest.FromString,
                    response_serializer=Fame_dot_Eciad__pb2.EciadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FAME.ECIAD.ECIAD', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ECIAD(object):
    """The ECIAD service definition.
    """

    @staticmethod
    def EciadTask(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/FAME.ECIAD.ECIAD/EciadTask',
            Fame_dot_Eciad__pb2.EciadRequest.SerializeToString,
            Fame_dot_Eciad__pb2.EciadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
