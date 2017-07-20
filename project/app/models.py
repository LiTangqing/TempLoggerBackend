from mongoengine import Document, EmbeddedDocument, fields
import datetime
from django.db import models

class Logs(EmbeddedDocument):
    time = fields.StringField(null=True)
    temp = fields.StringField(null=True)
    box_activity = fields.StringField(null=True,required = False)
    


class Trip(Document):
    last_modified_on = models.DateTimeField(auto_now_add=True)
    logs = fields.EmbeddedDocumentListField(Logs)
    lati_boxopen = fields.StringField(required = True)
    longi_boxclose = fields.StringField(required = True)
