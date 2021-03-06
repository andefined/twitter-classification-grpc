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
  serialized_pb=_b('\n\x0e\x63lassify.proto\x12\x08\x63lassify\"f\n\x0cUserFeatures\x12\x11\n\tfollowers\x18\x01 \x01(\x05\x12\x0f\n\x07\x66riends\x18\x02 \x01(\x05\x12\x10\n\x08statuses\x18\x03 \x01(\x05\x12\x11\n\tfavorites\x18\x04 \x01(\x05\x12\r\n\x05lists\x18\x05 \x01(\x05\")\n\tUserClass\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x32\x42\n\x08\x43lassify\x12\x36\n\x05Parse\x12\x16.classify.UserFeatures\x1a\x13.classify.UserClass\"\x00\x62\x06proto3')
)




_USERFEATURES = _descriptor.Descriptor(
  name='UserFeatures',
  full_name='classify.UserFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='followers', full_name='classify.UserFeatures.followers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friends', full_name='classify.UserFeatures.friends', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='classify.UserFeatures.statuses', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='favorites', full_name='classify.UserFeatures.favorites', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lists', full_name='classify.UserFeatures.lists', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=130,
)


_USERCLASS = _descriptor.Descriptor(
  name='UserClass',
  full_name='classify.UserClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='classify.UserClass.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='classify.UserClass.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=132,
  serialized_end=173,
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
  serialized_start=175,
  serialized_end=241,
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
