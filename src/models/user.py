from mongoengine import Document, ListField, ReferenceField, StringField


class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    full_name = StringField()
    receipts = ListField(ReferenceField("Receipt"))
