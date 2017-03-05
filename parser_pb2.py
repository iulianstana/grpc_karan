# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parser.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='parser.proto',
  package='twittertext',
  syntax='proto3',
  serialized_pb=_b('\n\x0cparser.proto\x12\x0btwittertext\"\x1c\n\x0cTweetRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\";\n\x0eParsedResponse\x12\r\n\x05users\x18\x01 \x03(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\x12\x0c\n\x04urls\x18\x03 \x03(\t2P\n\x0bTwitterText\x12\x41\n\x05Parse\x12\x19.twittertext.TweetRequest\x1a\x1b.twittertext.ParsedResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TWEETREQUEST = _descriptor.Descriptor(
  name='TweetRequest',
  full_name='twittertext.TweetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='twittertext.TweetRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=57,
)


_PARSEDRESPONSE = _descriptor.Descriptor(
  name='ParsedResponse',
  full_name='twittertext.ParsedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='twittertext.ParsedResponse.users', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='twittertext.ParsedResponse.tags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='urls', full_name='twittertext.ParsedResponse.urls', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['TweetRequest'] = _TWEETREQUEST
DESCRIPTOR.message_types_by_name['ParsedResponse'] = _PARSEDRESPONSE

TweetRequest = _reflection.GeneratedProtocolMessageType('TweetRequest', (_message.Message,), dict(
  DESCRIPTOR = _TWEETREQUEST,
  __module__ = 'parser_pb2'
  # @@protoc_insertion_point(class_scope:twittertext.TweetRequest)
  ))
_sym_db.RegisterMessage(TweetRequest)

ParsedResponse = _reflection.GeneratedProtocolMessageType('ParsedResponse', (_message.Message,), dict(
  DESCRIPTOR = _PARSEDRESPONSE,
  __module__ = 'parser_pb2'
  # @@protoc_insertion_point(class_scope:twittertext.ParsedResponse)
  ))
_sym_db.RegisterMessage(ParsedResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class TwitterTextStub(object):
    """This is the service for our API
    This is where we define the methods in this service
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Parse = channel.unary_unary(
          '/twittertext.TwitterText/Parse',
          request_serializer=TweetRequest.SerializeToString,
          response_deserializer=ParsedResponse.FromString,
          )


  class TwitterTextServicer(object):
    """This is the service for our API
    This is where we define the methods in this service
    """

    def Parse(self, request, context):
      """We have a mehtod called 'Parse' which takes
      parameter called 'TweetRequest' and returns
      the message 'ParsedResponse'
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TwitterTextServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Parse': grpc.unary_unary_rpc_method_handler(
            servicer.Parse,
            request_deserializer=TweetRequest.FromString,
            response_serializer=ParsedResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'twittertext.TwitterText', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTwitterTextServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This is the service for our API
    This is where we define the methods in this service
    """
    def Parse(self, request, context):
      """We have a mehtod called 'Parse' which takes
      parameter called 'TweetRequest' and returns
      the message 'ParsedResponse'
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTwitterTextStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This is the service for our API
    This is where we define the methods in this service
    """
    def Parse(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """We have a mehtod called 'Parse' which takes
      parameter called 'TweetRequest' and returns
      the message 'ParsedResponse'
      """
      raise NotImplementedError()
    Parse.future = None


  def beta_create_TwitterText_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('twittertext.TwitterText', 'Parse'): TweetRequest.FromString,
    }
    response_serializers = {
      ('twittertext.TwitterText', 'Parse'): ParsedResponse.SerializeToString,
    }
    method_implementations = {
      ('twittertext.TwitterText', 'Parse'): face_utilities.unary_unary_inline(servicer.Parse),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_TwitterText_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('twittertext.TwitterText', 'Parse'): TweetRequest.SerializeToString,
    }
    response_deserializers = {
      ('twittertext.TwitterText', 'Parse'): ParsedResponse.FromString,
    }
    cardinalities = {
      'Parse': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'twittertext.TwitterText', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
