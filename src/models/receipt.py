from mongoengine import Document, StringField, DateTimeField, ListField, FloatField, DictField
from datetime import datetime

class Receipt(Document):
    receipt_number = StringField(required=True)
    purchase_date = DateTimeField(default=datetime.now())
    products = ListField(DictField())  
    total_amount = FloatField()
    currency = StringField()
 