# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x08tutorial\"s\n\x04User\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\'\n\x04role\x18\x03 \x02(\x0e\x32\x13.tutorial.User.Role:\x04USER\"(\n\x04Role\x12\t\n\x05\x41\x44MIN\x10\x00\x12\x0b\n\x07MANAGER\x10\x01\x12\x08\n\x04USER\x10\x02\"1\n\x11PermissionRequest\x12\x1c\n\x04user\x18\x01 \x02(\x0b\x32\x0e.tutorial.User\":\n\x0ePermissionBody\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0e\n\x06result\x18\x03 \x02(\x08\"@\n\x12PermissionResponse\x12*\n\x08response\x18\x01 \x02(\x0b\x32\x18.tutorial.PermissionBody2[\n\nPermission\x12M\n\x0eSendPermission\x12\x1b.tutorial.PermissionRequest\x1a\x1c.tutorial.PermissionResponse\"\x00\x42\x32\n\x19io.grpc.examples.tutorialB\rTutorialProtoP\x01\xa2\x02\x03TUT')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031io.grpc.examples.tutorialB\rTutorialProtoP\001\242\002\003TUT'
  _USER._serialized_start=26
  _USER._serialized_end=141
  _USER_ROLE._serialized_start=101
  _USER_ROLE._serialized_end=141
  _PERMISSIONREQUEST._serialized_start=143
  _PERMISSIONREQUEST._serialized_end=192
  _PERMISSIONBODY._serialized_start=194
  _PERMISSIONBODY._serialized_end=252
  _PERMISSIONRESPONSE._serialized_start=254
  _PERMISSIONRESPONSE._serialized_end=318
  _PERMISSION._serialized_start=320
  _PERMISSION._serialized_end=411
# @@protoc_insertion_point(module_scope)
