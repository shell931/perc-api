"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'PercUsers.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fPercUsers.proto\x12\x05users\x1a\x1cgoogle/protobuf/struct.proto"\x1f\n\x03Geo\x12\x0b\n\x03lat\x18\x01 \x01(\t\x12\x0b\n\x03lng\x18\x02 \x01(\t"`\n\x07Address\x12\x0e\n\x06street\x18\x01 \x01(\t\x12\r\n\x05suite\x18\x02 \x01(\t\x12\x0c\n\x04city\x18\x03 \x01(\t\x12\x0f\n\x07zipcode\x18\x04 \x01(\t\x12\x17\n\x03geo\x18\x05 \x01(\x0b2\n.users.Geo"8\n\x07Company\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bcatchPhrase\x18\x02 \x01(\t\x12\n\n\x02bs\x18\x03 \x01(\t"\xb6\x01\n\x11CreateUserRequest\x12\x10\n\x08httpCode\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\r\n\x05email\x18\x04 \x01(\t\x12\x1f\n\x07address\x18\x0b \x01(\x0b2\x0e.users.Address\x12\r\n\x05phone\x18\x0c \x01(\t\x12\x0f\n\x07website\x18\r \x01(\t\x12\x1f\n\x07company\x18\x0e \x01(\x0b2\x0e.users.Company"f\n\x12CreateUserResponse\x12\x10\n\x08httpCode\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\r\n\x05email\x18\x04 \x01(\t\x12\x0f\n\x07messaje\x18\x05 \x01(\t"\x13\n\x11GetUserAllRequest"3\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04city\x18\x02 \x01(\t\x12\x0f\n\x07company\x18\x03 \x01(\t"D\n\x12GetUserAllResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b2\x0b.users.User\x12\x12\n\ntotalUsers\x18\x02 \x01(\x05"X\n\x12SearchUsersRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04city\x18\x02 \x01(\t\x12\x14\n\x0ccompany_name\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t"E\n\x13SearchUsersResponse\x12\x1a\n\x05users\x18\x01 \x03(\x0b2\x0b.users.User\x12\x12\n\ntotalUsers\x18\x02 \x01(\x052\xd7\x01\n\tPercUsers\x12A\n\nCreateUser\x12\x18.users.CreateUserRequest\x1a\x19.users.CreateUserResponse\x12A\n\nGetAllUser\x12\x18.users.GetUserAllRequest\x1a\x19.users.GetUserAllResponse\x12D\n\x0bSearchUsers\x12\x19.users.SearchUsersRequest\x1a\x1a.users.SearchUsersResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PercUsers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_GEO']._serialized_start = 56
    _globals['_GEO']._serialized_end = 87
    _globals['_ADDRESS']._serialized_start = 89
    _globals['_ADDRESS']._serialized_end = 185
    _globals['_COMPANY']._serialized_start = 187
    _globals['_COMPANY']._serialized_end = 243
    _globals['_CREATEUSERREQUEST']._serialized_start = 246
    _globals['_CREATEUSERREQUEST']._serialized_end = 428
    _globals['_CREATEUSERRESPONSE']._serialized_start = 430
    _globals['_CREATEUSERRESPONSE']._serialized_end = 532
    _globals['_GETUSERALLREQUEST']._serialized_start = 534
    _globals['_GETUSERALLREQUEST']._serialized_end = 553
    _globals['_USER']._serialized_start = 555
    _globals['_USER']._serialized_end = 606
    _globals['_GETUSERALLRESPONSE']._serialized_start = 608
    _globals['_GETUSERALLRESPONSE']._serialized_end = 676
    _globals['_SEARCHUSERSREQUEST']._serialized_start = 678
    _globals['_SEARCHUSERSREQUEST']._serialized_end = 766
    _globals['_SEARCHUSERSRESPONSE']._serialized_start = 768
    _globals['_SEARCHUSERSRESPONSE']._serialized_end = 837
    _globals['_PERCUSERS']._serialized_start = 840
    _globals['_PERCUSERS']._serialized_end = 1055