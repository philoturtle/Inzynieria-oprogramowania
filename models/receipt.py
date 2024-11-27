from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, DictField
from datetime import datetime

class Receipt(Document):
    receipt_number = StringField(required=True)
    purchase_date = DateTimeField(default=datetime.utcnow)
    products = ListField(DictField())  # e.g., [{"name": "WING PLATE", "price": 3.98}]
    total_amount = FloatField()
    currency = StringField()
    #user = me.ReferenceField(User, required=True)
