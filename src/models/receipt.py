from datetime import datetime

from mongoengine import (
    DateTimeField,
    DictField,
    Document,
    FloatField,
    ListField,
    StringField,
)


class Receipt(Document):
    receipt_number = StringField(required=True)
    purchase_date = DateTimeField(default=datetime.now())
    products = ListField(DictField())
    total_amount = FloatField()
    currency = StringField()
