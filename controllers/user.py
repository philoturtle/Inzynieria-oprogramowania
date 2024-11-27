from models.user import User
from models.receipt import Receipt


class UserController:
    def create(self, email, username, password, full_name=""):
        new_user = User(email=email, username=username, password=password, full_name=full_name)
        new_user.save()
    
    def delete(self, email):
        user = User.objects(email=email).first()
        # delete user receipts, not allow dangling leftovers
        for receipt in user.receipts:
            receipt.delete()
        user.delete()

    def link_receipt(self, user_email: str, receipt: Receipt):
        user = User.objects(email=user_email).first()
        if not user:
            print(f"No user found with email {user_email}")
            return
        user.receipts.append(receipt)
        user.save()