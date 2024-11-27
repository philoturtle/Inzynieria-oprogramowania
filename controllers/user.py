from models.user import User
from models.receipt import Receipt


class UserController:
    def
    def link_receipt(self, user_email: str, receipt: Receipt):
        user = User.objects(email=user_email).first()
        if not user:
            print(f"No user found with email {user_email}")
            return
        user.receipts.append(receipt)
        user.save()