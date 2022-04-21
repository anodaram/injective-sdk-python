# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/params/v1beta1/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cosmos/params/v1beta1/params.proto',
  package='cosmos.params.v1beta1',
  syntax='proto3',
  serialized_options=b'Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal\250\342\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"cosmos/params/v1beta1/params.proto\x12\x15\x63osmos.params.v1beta1\x1a\x14gogoproto/gogo.proto\"\x82\x01\n\x17ParameterChangeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x39\n\x07\x63hanges\x18\x03 \x03(\x0b\x32\".cosmos.params.v1beta1.ParamChangeB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"A\n\x0bParamChange\x12\x10\n\x08subspace\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t:\x04\x98\xa0\x1f\x00\x42:Z4github.com/cosmos/cosmos-sdk/x/params/types/proposal\xa8\xe2\x1e\x01\x62\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMETERCHANGEPROPOSAL = _descriptor.Descriptor(
  name='ParameterChangeProposal',
  full_name='cosmos.params.v1beta1.ParameterChangeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='cosmos.params.v1beta1.ParameterChangeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cosmos.params.v1beta1.ParameterChangeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changes', full_name='cosmos.params.v1beta1.ParameterChangeProposal.changes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=214,
)


_PARAMCHANGE = _descriptor.Descriptor(
  name='ParamChange',
  full_name='cosmos.params.v1beta1.ParamChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subspace', full_name='cosmos.params.v1beta1.ParamChange.subspace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='cosmos.params.v1beta1.ParamChange.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cosmos.params.v1beta1.ParamChange.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=281,
)

_PARAMETERCHANGEPROPOSAL.fields_by_name['changes'].message_type = _PARAMCHANGE
DESCRIPTOR.message_types_by_name['ParameterChangeProposal'] = _PARAMETERCHANGEPROPOSAL
DESCRIPTOR.message_types_by_name['ParamChange'] = _PARAMCHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParameterChangeProposal = _reflection.GeneratedProtocolMessageType('ParameterChangeProposal', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERCHANGEPROPOSAL,
  '__module__' : 'cosmos.params.v1beta1.params_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.params.v1beta1.ParameterChangeProposal)
  })
_sym_db.RegisterMessage(ParameterChangeProposal)

ParamChange = _reflection.GeneratedProtocolMessageType('ParamChange', (_message.Message,), {
  'DESCRIPTOR' : _PARAMCHANGE,
  '__module__' : 'cosmos.params.v1beta1.params_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.params.v1beta1.ParamChange)
  })
_sym_db.RegisterMessage(ParamChange)


DESCRIPTOR._options = None
_PARAMETERCHANGEPROPOSAL.fields_by_name['changes']._options = None
_PARAMETERCHANGEPROPOSAL._options = None
_PARAMCHANGE._options = None
# @@protoc_insertion_point(module_scope)
