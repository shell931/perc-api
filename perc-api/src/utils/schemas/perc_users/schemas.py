from marshmallow import Schema, fields, ValidationError

class Geo(Schema):
    lat = fields.String(required=True)
    lng = fields.String(required=True)
    
class Address(Schema):
    street = fields.String(required=True)
    suite = fields.String(required=True)
    city = fields.String(required=True)
    zipcode = fields.String(required=True)
    geo = fields.Nested(Geo, required=True)
    
class Company(Schema):
    name = fields.String(required=True)
    catchPhrase = fields.String(required=True)
    bs = fields.String(required=True)

#Schemas to validate CreateUser services fields
class CreateUserSchema(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    address = fields.Nested(Address, required=True)
    phone = fields.String(required=True)
    website = fields.String(required=True)
    company = fields.Nested(Company, required=True)
    
#Schemas to validate user search services fields
class SearchUsers(Schema):
    name = fields.String(required=True) 
    city = fields.String(required=True)
    company_name = fields.String(required=True)
    order_by = fields.String(required=True)