# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests.proto

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
  name='tests.proto',
  package='Tests',
  syntax='proto2',
  serialized_pb=_b('\n\x0btests.proto\x12\x05Tests\"\xb7\x02\n\x05Test1\x12\r\n\x05Int32\x18\x01 \x01(\x05\x12\x0e\n\x06Sint32\x18\x02 \x01(\x11\x12\x0e\n\x06Uint32\x18\x03 \x01(\r\x12\r\n\x05Int64\x18\x04 \x01(\x03\x12\x0e\n\x06Sint64\x18\x05 \x01(\x12\x12\x0e\n\x06Uint64\x18\x06 \x01(\x04\x12\x0c\n\x04\x42ool\x18\x07 \x01(\x08\x12,\n\x04\x45num\x18\x08 \x01(\x0e\x32\x16.Tests.Test1.Test1Enum:\x06ValueA\x12\x0f\n\x07\x46ixed32\x18\t \x01(\x07\x12\x0f\n\x07\x46ixed64\x18\n \x01(\x06\x12\x10\n\x08Sfixed32\x18\x0b \x01(\x0f\x12\x10\n\x08Sfixed64\x18\x0c \x01(\x10\x12\r\n\x05\x46loat\x18\r \x01(\x02\x12\x0e\n\x06\x44ouble\x18\x0e \x01(\x01\"/\n\tTest1Enum\x12\n\n\x06ValueA\x10\x01\x12\n\n\x06ValueB\x10\x02\x12\n\n\x06ValueC\x10\x03')
)



_TEST1_TEST1ENUM = _descriptor.EnumDescriptor(
  name='Test1Enum',
  full_name='Tests.Test1.Test1Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ValueA', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ValueB', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ValueC', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=287,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_TEST1_TEST1ENUM)


_TEST1 = _descriptor.Descriptor(
  name='Test1',
  full_name='Tests.Test1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Int32', full_name='Tests.Test1.Int32', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sint32', full_name='Tests.Test1.Sint32', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Uint32', full_name='Tests.Test1.Uint32', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Int64', full_name='Tests.Test1.Int64', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sint64', full_name='Tests.Test1.Sint64', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Uint64', full_name='Tests.Test1.Uint64', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Bool', full_name='Tests.Test1.Bool', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Enum', full_name='Tests.Test1.Enum', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fixed32', full_name='Tests.Test1.Fixed32', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fixed64', full_name='Tests.Test1.Fixed64', index=9,
      number=10, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sfixed32', full_name='Tests.Test1.Sfixed32', index=10,
      number=11, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Sfixed64', full_name='Tests.Test1.Sfixed64', index=11,
      number=12, type=16, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Float', full_name='Tests.Test1.Float', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Double', full_name='Tests.Test1.Double', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TEST1_TEST1ENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=334,
)

_TEST1.fields_by_name['Enum'].enum_type = _TEST1_TEST1ENUM
_TEST1_TEST1ENUM.containing_type = _TEST1
DESCRIPTOR.message_types_by_name['Test1'] = _TEST1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Test1 = _reflection.GeneratedProtocolMessageType('Test1', (_message.Message,), dict(
  DESCRIPTOR = _TEST1,
  __module__ = 'tests_pb2'
  # @@protoc_insertion_point(class_scope:Tests.Test1)
  ))
_sym_db.RegisterMessage(Test1)


# @@protoc_insertion_point(module_scope)
