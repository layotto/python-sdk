# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import appcallback_pb2 as appcallback__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class AppCallbackStub(object):
    """AppCallback V1 allows user application to interact with runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from runtime.
    // Invokes service method with InvokeRequest.
    rpc OnInvoke (InvokeRequest) returns (InvokeResponse) {}
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListTopicSubscriptions = channel.unary_unary(
                '/spec.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
                )
        self.OnTopicEvent = channel.unary_unary(
                '/spec.proto.runtime.v1.AppCallback/OnTopicEvent',
                request_serializer=appcallback__pb2.TopicEventRequest.SerializeToString,
                response_deserializer=appcallback__pb2.TopicEventResponse.FromString,
                )


class AppCallbackServicer(object):
    """AppCallback V1 allows user application to interact with runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from runtime.
    // Invokes service method with InvokeRequest.
    rpc OnInvoke (InvokeRequest) returns (InvokeResponse) {}
    """

    def ListTopicSubscriptions(self, request, context):
        """Lists all topics subscribed by this app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnTopicEvent(self, request, context):
        """Subscribes events from Pubsub
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AppCallbackServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListTopicSubscriptions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTopicSubscriptions,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=appcallback__pb2.ListTopicSubscriptionsResponse.SerializeToString,
            ),
            'OnTopicEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.OnTopicEvent,
                    request_deserializer=appcallback__pb2.TopicEventRequest.FromString,
                    response_serializer=appcallback__pb2.TopicEventResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spec.proto.runtime.v1.AppCallback', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AppCallback(object):
    """AppCallback V1 allows user application to interact with runtime.
    User application needs to implement AppCallback service if it needs to
    receive message from runtime.
    // Invokes service method with InvokeRequest.
    rpc OnInvoke (InvokeRequest) returns (InvokeResponse) {}
    """

    @staticmethod
    def ListTopicSubscriptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spec.proto.runtime.v1.AppCallback/ListTopicSubscriptions',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            appcallback__pb2.ListTopicSubscriptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnTopicEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spec.proto.runtime.v1.AppCallback/OnTopicEvent',
            appcallback__pb2.TopicEventRequest.SerializeToString,
            appcallback__pb2.TopicEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)