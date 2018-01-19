# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classify.proto

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
  name='classify.proto',
  package='classify',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x63lassify.proto\x12\x08\x63lassify\"\x1c\n\x0cUserFeatures\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1b\n\tUserClass\x12\x0e\n\x06result\x18\x02 \x01(\t2B\n\x08\x43lassify\x12\x36\n\x05Parse\x12\x16.classify.UserFeatures\x1a\x13.classify.UserClass\"\x00\x62\x06proto3')
)




_USERFEATURES = _descriptor.Descriptor(
  name='UserFeatures',
  full_name='classify.UserFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='classify.UserFeatures.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=28,
  serialized_end=56,
)


_USERCLASS = _descriptor.Descriptor(
  name='UserClass',
  full_name='classify.UserClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='classify.UserClass.result', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['UserFeatures'] = _USERFEATURES
DESCRIPTOR.message_types_by_name['UserClass'] = _USERCLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserFeatures = _reflection.GeneratedProtocolMessageType('UserFeatures', (_message.Message,), dict(
  DESCRIPTOR = _USERFEATURES,
  __module__ = 'classify_pb2'
  # @@protoc_insertion_point(class_scope:classify.UserFeatures)
  ))
_sym_db.RegisterMessage(UserFeatures)

UserClass = _reflection.GeneratedProtocolMessageType('UserClass', (_message.Message,), dict(
  DESCRIPTOR = _USERCLASS,
  __module__ = 'classify_pb2'
  # @@protoc_insertion_point(class_scope:classify.UserClass)
  ))
_sym_db.RegisterMessage(UserClass)



_CLASSIFY = _descriptor.ServiceDescriptor(
  name='Classify',
  full_name='classify.Classify',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=87,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='Parse',
    full_name='classify.Classify.Parse',
    index=0,
    containing_service=None,
    input_type=_USERFEATURES,
    output_type=_USERCLASS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLASSIFY)

DESCRIPTOR.services_by_name['Classify'] = _CLASSIFY

# @@protoc_insertion_point(module_scope)