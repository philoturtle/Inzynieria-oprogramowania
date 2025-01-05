from models.user import User
from models.receipt import Receipt
from passlib.context import CryptContext


class UserController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    def create(self, email: str, username: str, password: str, full_name: str=""):
        hashed_password = self.pwd_context.hash(password)
        new_user = User(email=email, username=username, password=hashed_password, full_name=full_name)
        new_user.save()
    
    def delete(self, id: str):
        user = User.objects(id=id).first()
        # delete user receipts, not allow dangling leftovers
        for receipt in user.receipts:
            receipt.delete()
        user.delete()
    
    def find(self, id: str) -> User:
        user = User.objects(id=id).first()
        if user:
            user.receipts = list(user.receipts)  
        return user
    
    def link_receipt(self, user_id: str, receipt: Receipt):
        user = User.objects(id=user_id).first()
        if not user:
            print(f"No user found")
            return
        user.receipts.append(receipt)
        user.save()
    def login(self, username: str, password: str) -> User:
        user = User.objects(username=username).first()
        if user is not None and self.pwd_context.verify(password, user.password):
            return user
        return None