from mongoengine import Document, ReferenceField, DateTimeField
from models.user import User
from datetime import datetime, timedelta

class Session(Document):
    user = ReferenceField(User)
    expire_time = DateTimeField(default=datetime.now() + timedelta(hours=1))