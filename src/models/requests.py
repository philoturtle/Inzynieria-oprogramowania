from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    amount: float


class ReceiptRequest(BaseModel):
    user_id: str
    items: List[Item]
    purchase_date: str