# -*- coding: utf-8 -*-

import grpc  # type: ignore
from grpc import (  # type: ignore
    UnaryUnaryClientInterceptor,
    UnaryStreamClientInterceptor,
    StreamUnaryClientInterceptor,
    StreamStreamClientInterceptor
)
from typing import Dict, Optional, Union, Sequence, List
from src.proto import runtime_pb2,runtime_pb2_grpc

class RuntimeGrpcClient:
    """The convenient layer implementation of Layotto gRPC APIs.
    This provides the wrappers and helpers to allows developers to use runtime gRPC API
    easily and consistently.
    Examples:
        >>> from src.client import RuntimeGrpcClient
        >>> cli = RuntimeGrpcClient("127.0.0.1", 34904)
        >>> resp = cli.invoke_method('callee', 'method', b'data')
    With context manager:
        >>> from src.client import RuntimeGrpcClient
        >>> with RuntimeGrpcClient("127.0.0.1",34904) as cli:
        ...     resp = cli.invoke_method('callee', 'method', b'data')
    """

    def __init__(
        self,
        ip: str,
        port: int,
        interceptors: Optional[List[Union[
            UnaryUnaryClientInterceptor,
            UnaryStreamClientInterceptor,
            StreamUnaryClientInterceptor,
            StreamStreamClientInterceptor]]] = None):
        """Connects to Layotto Runtime and initialize gRPC client stub.
        Args:
            ip: The IP address of Layotto Runtime.
            port: The port of Layotto Runtime.
            interceptors (list of UnaryUnaryClientInterceptor or
                UnaryStreamClientInterceptor or
                StreamUnaryClientInterceptor or
                StreamStreamClientInterceptor, optional): gRPC interceptors.
        """
        self._address = ip+":"+str(port)
        self._channel = grpc.insecure_channel(self._address)   # type: ignore

        if interceptors:
            self._channel = grpc.intercept_channel(   # type: ignore
                self._channel, *interceptors)
        # set stub
        self._stub = runtime_pb2_grpc.RuntimeStub(self._channel)

    def close(self):
        """Closes runtime gRPC channel."""
        if self._channel:
            self._channel.close()

    def __del__(self):
        self.close()

    def __enter__(self) -> 'RuntimeGrpcClient':
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def say_hello(self,service_name:str):
        """Sends a Hello request to Layotto Runtime.
        Returns:
            HelloResponse: The response from Layotto Runtime.
        """
        response, call= self._stub.SayHello.with_call(runtime_pb2.HelloRequest(service_name=service_name))
        # TODO send request to layotto runtime
        return response.hello

