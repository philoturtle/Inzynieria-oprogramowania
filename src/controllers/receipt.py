import re
from datetime import datetime

import pytesseract
from PIL import Image

from models.receipt import Receipt


class ReceiptController:
    def save_receipt_to_db_from_img(self, receipt_img) -> Receipt:
        receipt_data = self._extract_data_from_receipt(receipt_img)
        receipt = Receipt(
            receipt_number=receipt_data["receipt_number"],
            purchase_date=datetime.strptime(receipt_data["purchase_date"], "%Y-%m-%d"),
            products=receipt_data["products"],
            total_amount=receipt_data["total_amount"],
            currency=receipt_data["currency"],
        )
        receipt.save()
        return receipt

    def save_receipt_to_db_from_dict(self, receipt_data) -> Receipt:
        receipt = Receipt(
            receipt_number=receipt_data["receipt_number"],
            purchase_date=receipt_data["purchase_date"],
            products=receipt_data["products"],
            total_amount=receipt_data["total_amount"],
            currency=receipt_data["currency"],
        )
        receipt.save()
        return receipt

    def find(self, id) -> Receipt:
        return Receipt.objects(id=id).first()

    def _extract_data_from_receipt(self, image):
        receipt_text = [
            line.strip()
            for line in pytesseract.image_to_string(Image.open(image))
            .strip()
            .split("\n")
            if line.strip()
        ]

        patterns = {
            "receipt_number": re.compile(r"(?:ID\W+)(\w+)"),
            "products": re.compile(
                r"(?P<name>[A-Za-z0-9 ]+)(?:\s+\d+\s+)(?P<price>\d+\.\d+).*"
            ),
            "total_amount": re.compile(r"(?:TOTAL\s+)(\d+\.\d+)"),
            "purchase_date": re.compile(
                r"(?P<MONTH>\d{2})\/(?P<DAY>\d{2})\/(?P<YEAR>\d{2})"
            ),
        }

        receipt_data = {
            "receipt_number": "",
            "purchase_date": datetime.now().strftime("%Y-%m-%d"),
            "products": [],
            "total_amount": 0.0,
            "currency": "USD",
        }

        for line in receipt_text:
            for pattern_name, pattern in patterns.items():
                match = pattern.match(line)
                if not match:
                    continue
                if pattern_name == "products":
                    tmp = match.groupdict()
                    if tmp["name"] == "TAX":
                        continue
                    tmp["price"] = float(tmp["price"])
                    receipt_data[pattern_name].append(tmp)
                elif pattern_name == "purchase_date":
                    tmp = match.groupdict()
                    year, month, day = tmp["YEAR"], tmp["MONTH"], tmp["DAY"]
                    receipt_data[pattern_name] = f"20{year}-{month}-{day}"
                elif pattern_name == "total_amount":
                    receipt_data[pattern_name] = float(match.group(1))
                else:
                    receipt_data[pattern_name] = match.group(1)

        print(receipt_data)
        return receipt_data

    def create_manual_receipt(self, receipt_data):
        receipt = Receipt(
            receipt_number=receipt_data["receipt_number"],
            purchase_date=receipt_data["purchase_date"],
            products=receipt_data["products"],
            total_amount=receipt_data["total_amount"],
            currency=receipt_data["currency"],
        )
        receipt.save()
        return receipt

    def delete(self, id: str):
        receipt = Receipt.objects(id=id).first()
        receipt.delete()
