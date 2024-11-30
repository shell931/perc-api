from marshmallow import Schema, fields, ValidationError

#Esquemas para validar los payloads que llegan

class CreateTemplateSchema(Schema):
    name = fields.String(required=True)
    htmlContent = fields.String(required=True)
    textContent = fields.String(required=True)

class UpdateTemplateSchema(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    htmlContent = fields.String(required=True)
    textContent = fields.String(required=True)

class SendMailSchema(Schema):
    templateId = fields.String(required=True)
    variables = fields.Dict(keys=fields.Str(), values=fields.Str())
    send_to = fields.String(required=True)
    send_to_cc = fields.String(required=True)
    send_to_bcc = fields.String(required=True)
    subject = fields.String(required=True)