from mongoengine import connect
from controllers.receipt import ReceiptController
from controllers.user import UserController
from controllers.session import SessionController

from fastapi import FastAPI, File, Form, UploadFile, HTTPException, Depends, status, APIRouter
import os
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import random
from fastapi import Request
from fastapi import Body

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import Annotated, List, Dict
from pydantic import BaseModel
class ReceiptRequest(BaseModel):
    session_id: Annotated[str, Form()]
    img_file: Annotated[UploadFile, File()] = File(...)
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from fastapi.responses import FileResponse

import io
import base64
import calendar


app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")
templates = Jinja2Templates(directory="templates")

connect('appdb', host='mongodb://localhost', port=27020)


sessions = {}

MAX_FILE_SIZE = 500 * 1024 

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login(username: str,  password: str):
    sc = SessionController()
    uc = UserController()
    user = uc.login(username, password)
    if not user:
        return {"message": "Wrong"}

    session = sc.create_session(user=user)
    return {"message": "Logged in successfully", "session_id": str(session.id)}

@app.get("/user/{id}")
def read_item(id: str):
    uc = UserController()
    user = uc.find(id)
    print(user)
    return user.to_json()

@app.post("/user/")
def create_user(username: str, email: str, password: str, full_name: str=""):
    uc = UserController()
    uc.create(email=email, username=username, full_name=full_name, password=password)
    return True

@app.delete("/user/{id}")
def delete_user(id: str):
    uc = UserController()
    uc.delete(id)
    return{'message':f'Succesfully deleted user'}

@app.post("/receipt")
async def upload_image(session_id: Annotated[str, Form()], img_file: Annotated[UploadFile, File()]):
    sc = SessionController()
    # if not sc.is_active(session_id=session_id):
    #     raise HTTPException(status_code=401, detail="Your session is expired.")
    user = sc.get_user(session_id)
    rc = ReceiptController()

    file_size = len(await img_file.read())
    img_file.file.seek(0)
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File is too large. Maximum allowed size is 500 KB.")

    
    if img_file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are allowed.")
    receipt = rc.save_receipt_to_db_from_img(img_file.file)
    uc = UserController()
    uc.link_receipt(user.id, receipt)
    id = receipt.id
    extension = img_file.filename.split('.')[-1]

    file_save_path=f"./images/{id}.{extension}"
    if os.path.exists("./images") == False:
        os.makedirs("./images")

    with open(file_save_path, "wb") as f:
        img_file.file.seek(0)
        f.write(img_file.file.read())

    return {"image_path":file_save_path,"message": "Image saved successfully"}

    
@app.get("/receipt/{id}")
def read_item(id: str):
    rc = ReceiptController()
    receipt = rc.find(id)
    return receipt.to_json()

@app.delete("/receipt/{id}")
def delete_receipt(id: str):
    rc = ReceiptController()
    rc.delete(id)
    return{'message':f'Succesfully deleted receipt'}

@app.get('/view/receipt/{id}', response_class=HTMLResponse)
def view_receipt(request: Request, id: str):
    rc = ReceiptController()
    receipt = rc.find(id)
    return templates.TemplateResponse(
        request=request, name="receipt.html", context={"receipt": receipt}
    )


@app.get('/view/receipts/{user_id}', response_class=HTMLResponse)
def list_user_receipts(
    request: Request,
    user_id: str,
    year: str = '',
    month: str = '',
    day: str = '',
):
    uc = UserController()
    user = uc.find(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get all receipts
    receipts = user.receipts

    # Filter receipts based on query parameters
    filtered_receipts = []
    for receipt in receipts:
        purchase_date = receipt.purchase_date  
        if (
            (year == '' or purchase_date.year == int(year)) and
            (month == '' or purchase_date.month == int(month)) and
            (day == '' or purchase_date.day == int(day))
        ):
            filtered_receipts.append(receipt)
    receipts = filtered_receipts

    if receipts:
        # Prepare data for plotting
        data = [
            {
                "Date": receipt.purchase_date,
                "Total Amount": receipt.total_amount,
            }
            for receipt in receipts
        ]
        df = pd.DataFrame(data)
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day

        # Initialize paths for the plots
        yearly_plot_path = monthly_plot_path = daily_plot_path = None

        # If a year is selected, generate the monthly plot
        if year and not month:
            # Aggregate the total amounts by Month for the year
            monthly_data = df.groupby('Month')['Total Amount'].sum().reset_index()

            monthly_data = monthly_data.set_index('Month').reindex(range(1, 13), fill_value=0).reset_index()
            monthly_data.columns = ['Month', 'Total Amount']

            # Generate monthly plot (for all 12 months)
            sns.barplot(data=monthly_data, x="Month", y="Total Amount", errorbar=None)
            plt.title(f"Total Amount by Month for Year {year}")
            iobytes = io.BytesIO()
            plt.savefig(iobytes, format='jpg')
            iobytes.seek(0)
            monthly_plot_path = base64.b64encode(iobytes.read()).decode()
            plt.close()

        # If a month is selected, generate the daily plot for that month
        elif month and not year:
            # Aggregate the total amounts by Day for the selected month
            monthly_data = df[df['Month'] == int(month)]
            daily_data = monthly_data.groupby('Day')['Total Amount'].sum().reset_index()

            # Ensure all 31 days are present
            daily_data = daily_data.set_index('Day').reindex(range(1, 32), fill_value=0).reset_index()
            daily_data.columns = ['Day', 'Total Amount']

            # Generate daily plot (for all 31 days in the month)
            sns.barplot(data=daily_data, x="Day", y="Total Amount", errorbar=None)
            plt.title(f"Total Amount by Day for Month {month}")
            iobytes = io.BytesIO()
            plt.savefig(iobytes, format='jpg')
            iobytes.seek(0)
            daily_plot_path = base64.b64encode(iobytes.read()).decode()
            plt.close()

    else:
        # If no receipts, set paths to None
        yearly_plot_path = monthly_plot_path = daily_plot_path = None

    return templates.TemplateResponse(
        "receipts_list.html",
        {
            "request": request,
            "user": user,
            "receipts": receipts,
            "year": year,
            "month": month,
            "day": day,
            "yearly_plot": yearly_plot_path,
            "monthly_plot": monthly_plot_path,
            "daily_plot": daily_plot_path,
        },
    )
class Item(BaseModel):
    name: str
    amount: float

class ReceiptRequest(BaseModel):
    user_id: str
    items: List[Item]
    purchase_date: str

@app.post("/add-expense")
def add_expense(
    request: ReceiptRequest
):
    uc = UserController()
    user = uc.find(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    total_amount = sum(item.amount for item in request.items)
    receipt = {
        "receipt_number": f"{random.randint(1000, 9999)}", 
        "purchase_date": datetime.strptime(request.purchase_date, "%Y-%m-%d"),  
        "products": [{"name": item.name, "price": item.amount} for item in request.items],
        "total_amount": total_amount,
        "currency": "USD",
    }

    rc = ReceiptController()
    new_receipt = rc.save_receipt_to_db_from_dict(receipt)
    uc.link_receipt(user.id, new_receipt)

    return {"message": "Expense added successfully!"}
