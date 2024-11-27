from models.receipt import Receipt
from datetime import datetime
import pytesseract
from PIL import Image
import re

class ReceiptController:
    def save_receipt_to_db(self, receipt_img: str) -> Receipt:
        receipt_data = self._extract_data_from_receipt(receipt_img)
        receipt = Receipt(
            receipt_number=receipt_data['receipt_number'],
            purchase_date=datetime.strptime(receipt_data['purchase_date'], "%Y-%m-%d"),
            products=receipt_data['products'],
            total_amount=receipt_data['total_amount'],
            currency=receipt_data['currency'],
        )
        receipt.save()
        return receipt
    
    def _extract_data_from_receipt(self, image_path: str):
        # Extract text from image using Tesseract
        receipt_text = pytesseract.image_to_string(Image.open(image_path))

        # Process text to extract product details (example regex)
        product_pattern = r'^(?!.*\b(?:SUBTOTAL|TAX|TOTAL|DEBIT TEND|CHANGE DUE)\b)([\w\s]+?)\s+(\d+\.\d{2})\b'

        products = []
        
        for match in re.finditer(product_pattern, receipt_text):
            name, price = match.groups()
            products.append({"name": name.strip(), "price": float(price)})

        # Example: Returning dummy data (customize based on your text extraction)
        receipt_data = {
            "receipt_number": "R12345",  # Generate dynamically if needed
            "purchase_date": "2024-04-23",
            "products": products,
            "total_amount": sum(p['price'] for p in products),
            "currency": "USD"
        }
        return receipt_data