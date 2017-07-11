from mongoengine import Document, EmbeddedDocument, fields
import datetime
from django.db import models

class Logs(EmbeddedDocument):

    time = fields.StringField(null=True)
    temp = fields.StringField(null=True)

class Trip(Document):
    last_modified_on = models.DateTimeField(auto_now_add=True)
    arrival_lat = fields.StringField(null=True, required = False)
    arrival_long = fields.StringField(null=True, required = False)
    logs = fields.EmbeddedDocumentListField(Logs)
