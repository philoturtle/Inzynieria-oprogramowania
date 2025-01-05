from datetime import datetime, timedelta

from mongoengine import DateTimeField, Document, ReferenceField

from models.user import User


class Session(Document):
    user = ReferenceField(User)
    expire_time = DateTimeField(default=datetime.now() + timedelta(hours=1))
