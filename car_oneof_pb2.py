# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car_oneof.proto

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
  name='car_oneof.proto',
  package='',
  serialized_pb=_b('\n\x0f\x63\x61r_oneof.proto\"M\n\x08\x43\x61rOneOf\x12\x12\n\nnum_wheels\x18\x01 \x02(\r\x12\x0f\n\x05\x63olor\x18\x10 \x01(\tH\x00\x12\x0f\n\x05\x62rand\x18\x11 \x01(\tH\x00\x42\x0b\n\tcar_specs')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CARONEOF = _descriptor.Descriptor(
  name='CarOneOf',
  full_name='CarOneOf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_wheels', full_name='CarOneOf.num_wheels', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='CarOneOf.color', index=1,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brand', full_name='CarOneOf.brand', index=2,
      number=17, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='car_specs', full_name='CarOneOf.car_specs',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=19,
  serialized_end=96,
)

_CARONEOF.oneofs_by_name['car_specs'].fields.append(
  _CARONEOF.fields_by_name['color'])
_CARONEOF.fields_by_name['color'].containing_oneof = _CARONEOF.oneofs_by_name['car_specs']
_CARONEOF.oneofs_by_name['car_specs'].fields.append(
  _CARONEOF.fields_by_name['brand'])
_CARONEOF.fields_by_name['brand'].containing_oneof = _CARONEOF.oneofs_by_name['car_specs']
DESCRIPTOR.message_types_by_name['CarOneOf'] = _CARONEOF

CarOneOf = _reflection.GeneratedProtocolMessageType('CarOneOf', (_message.Message,), dict(
  DESCRIPTOR = _CARONEOF,
  __module__ = 'car_oneof_pb2'
  # @@protoc_insertion_point(class_scope:CarOneOf)
  ))
_sym_db.RegisterMessage(CarOneOf)


# @@protoc_insertion_point(module_scope)
