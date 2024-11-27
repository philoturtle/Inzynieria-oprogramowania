import argparse
from mongoengine import connect
from controllers.receipt import ReceiptController
from controllers.user import UserController
from models.user import User

def main():
    connect('test_receipt_manager_db', host='localhost', port=27017)
    print("connected")
    user_email = "john@example.com"  # Replace with actual user email
    # Path to your receipt image
    image_path = "/home/philoturtle/repos/projekt_inzynieria/16.jpg"

    user = User(username="john_doe", email="john@example.com", password="securepassword", full_name="John Doe")
    user.save()  # Save the user to the database

    receipt_controller = ReceiptController()
    user_controller = UserController()
    receipt = receipt_controller.save_receipt_to_db(image_path)
    user_controller.link_receipt(user_email, receipt)
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='ProjektInzyniera', description='prototype project description')
    #parser.add_argument('--db', help='mongodb connect string', type=str, required=True)
    main()