# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dist_processing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dist_processing.proto',
  package='dist_processing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x64ist_processing.proto\x12\x0f\x64ist_processing\"#\n\x0cImageRequest\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\"@\n\nImageReply\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x12\n\nimage_name\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\x0c\"Y\n\x0eProcessedImage\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x13\n\x0bworker_name\x18\x02 \x01(\t\x12\x12\n\nimage_name\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\x0c\"\x19\n\tImageDone\x12\x0c\n\x04\x64one\x18\x01 \x01(\x08\x32\xab\x01\n\rImageTransfer\x12L\n\x0cRequestImage\x12\x1d.dist_processing.ImageRequest\x1a\x1b.dist_processing.ImageReply\"\x00\x12L\n\x0bReturnImage\x12\x1f.dist_processing.ProcessedImage\x1a\x1a.dist_processing.ImageDone\"\x00\x62\x06proto3'
)




_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='dist_processing.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_name', full_name='dist_processing.ImageRequest.worker_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=77,
)


_IMAGEREPLY = _descriptor.Descriptor(
  name='ImageReply',
  full_name='dist_processing.ImageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='dist_processing.ImageReply.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_name', full_name='dist_processing.ImageReply.image_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='dist_processing.ImageReply.image', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=143,
)


_PROCESSEDIMAGE = _descriptor.Descriptor(
  name='ProcessedImage',
  full_name='dist_processing.ProcessedImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='dist_processing.ProcessedImage.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worker_name', full_name='dist_processing.ProcessedImage.worker_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_name', full_name='dist_processing.ProcessedImage.image_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='dist_processing.ProcessedImage.image', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=234,
)


_IMAGEDONE = _descriptor.Descriptor(
  name='ImageDone',
  full_name='dist_processing.ImageDone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='done', full_name='dist_processing.ImageDone.done', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=261,
)

DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['ImageReply'] = _IMAGEREPLY
DESCRIPTOR.message_types_by_name['ProcessedImage'] = _PROCESSEDIMAGE
DESCRIPTOR.message_types_by_name['ImageDone'] = _IMAGEDONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'dist_processing_pb2'
  # @@protoc_insertion_point(class_scope:dist_processing.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

ImageReply = _reflection.GeneratedProtocolMessageType('ImageReply', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREPLY,
  '__module__' : 'dist_processing_pb2'
  # @@protoc_insertion_point(class_scope:dist_processing.ImageReply)
  })
_sym_db.RegisterMessage(ImageReply)

ProcessedImage = _reflection.GeneratedProtocolMessageType('ProcessedImage', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSEDIMAGE,
  '__module__' : 'dist_processing_pb2'
  # @@protoc_insertion_point(class_scope:dist_processing.ProcessedImage)
  })
_sym_db.RegisterMessage(ProcessedImage)

ImageDone = _reflection.GeneratedProtocolMessageType('ImageDone', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDONE,
  '__module__' : 'dist_processing_pb2'
  # @@protoc_insertion_point(class_scope:dist_processing.ImageDone)
  })
_sym_db.RegisterMessage(ImageDone)



_IMAGETRANSFER = _descriptor.ServiceDescriptor(
  name='ImageTransfer',
  full_name='dist_processing.ImageTransfer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=264,
  serialized_end=435,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestImage',
    full_name='dist_processing.ImageTransfer.RequestImage',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReturnImage',
    full_name='dist_processing.ImageTransfer.ReturnImage',
    index=1,
    containing_service=None,
    input_type=_PROCESSEDIMAGE,
    output_type=_IMAGEDONE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGETRANSFER)

DESCRIPTOR.services_by_name['ImageTransfer'] = _IMAGETRANSFER

# @@protoc_insertion_point(module_scope)
