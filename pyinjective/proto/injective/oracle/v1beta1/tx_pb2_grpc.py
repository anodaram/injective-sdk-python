# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.oracle.v1beta1 import tx_pb2 as injective_dot_oracle_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the oracle Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RelayPriceFeedPrice = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayPriceFeedPrice',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.FromString,
                )
        self.RelayBandRates = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayBandRates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.FromString,
                )
        self.RequestBandIBCRates = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RequestBandIBCRates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.FromString,
                )
        self.RelayCoinbaseMessages = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayCoinbaseMessages',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the oracle Msg service.
    """

    def RelayPriceFeedPrice(self, request, context):
        """RelayPriceFeedPrice defines a method for relaying a price for a price feeder-based oracle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayBandRates(self, request, context):
        """RelayBandRates defines a method for relaying rates from Band
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestBandIBCRates(self, request, context):
        """RequestBandIBCRates defines a method for fetching rates from Band ibc
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayCoinbaseMessages(self, request, context):
        """RelayCoinbaseMessages defines a method for relaying price messages from Coinbase API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RelayPriceFeedPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayPriceFeedPrice,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.SerializeToString,
            ),
            'RelayBandRates': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayBandRates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.SerializeToString,
            ),
            'RequestBandIBCRates': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestBandIBCRates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.SerializeToString,
            ),
            'RelayCoinbaseMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayCoinbaseMessages,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.oracle.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the oracle Msg service.
    """

    @staticmethod
    def RelayPriceFeedPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Msg/RelayPriceFeedPrice',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelayBandRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Msg/RelayBandRates',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestBandIBCRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Msg/RequestBandIBCRates',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelayCoinbaseMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.oracle.v1beta1.Msg/RelayCoinbaseMessages',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
