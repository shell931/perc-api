"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14authentication.proto\x12\x0eauthentication"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t"\x1e\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t"T\n\rSignUpRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x10\n\x08is_admin\x18\x04 \x01(\x08"\x1f\n\x0eSignUpResponse\x12\r\n\x05token\x18\x01 \x01(\t"9\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05email\x18\x03 \x01(\t"%\n\x14ValidateTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t"7\n\x15ValidateTokenResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xfd\x01\n\x0eAuthentication\x12D\n\x05Login\x12\x1c.authentication.LoginRequest\x1a\x1d.authentication.LoginResponse\x12G\n\x06SignUp\x12\x1d.authentication.SignUpRequest\x1a\x1e.authentication.SignUpResponse\x12\\\n\rValidateToken\x12$.authentication.ValidateTokenRequest\x1a%.authentication.ValidateTokenResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authentication_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_LOGINREQUEST']._serialized_start = 40
    _globals['_LOGINREQUEST']._serialized_end = 90
    _globals['_LOGINRESPONSE']._serialized_start = 92
    _globals['_LOGINRESPONSE']._serialized_end = 122
    _globals['_SIGNUPREQUEST']._serialized_start = 124
    _globals['_SIGNUPREQUEST']._serialized_end = 208
    _globals['_SIGNUPRESPONSE']._serialized_start = 210
    _globals['_SIGNUPRESPONSE']._serialized_end = 241
    _globals['_USER']._serialized_start = 243
    _globals['_USER']._serialized_end = 300
    _globals['_VALIDATETOKENREQUEST']._serialized_start = 302
    _globals['_VALIDATETOKENREQUEST']._serialized_end = 339
    _globals['_VALIDATETOKENRESPONSE']._serialized_start = 341
    _globals['_VALIDATETOKENRESPONSE']._serialized_end = 396
    _globals['_AUTHENTICATION']._serialized_start = 399
    _globals['_AUTHENTICATION']._serialized_end = 652