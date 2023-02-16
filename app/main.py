import pymongo
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import FastAPI, Form, Request
from passlib.context import CryptContext
from dotenv import load_dotenv
from dotenv import dotenv_values

import os
# from config.db import MONGO_URI


load_dotenv()
config = dotenv_values(".env")
client = MongoClient(config["MONGO_URI"])

app = FastAPI()

templates =Jinja2Templates(directory="templates")
# client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['scmxpertlite']
signup_collection=db['users']
shipment_collection=db['shipment']

class signup(BaseModel):
     Username:str    
     Password: str
     Email:str

class Createshipment (BaseModel):
     shipment_invoice_number:str
     container_number:str
     description:str
     route_details:str
     goods_type:str
     device:str
     expected_Delivery_Date:str
     po_number:int
     delivery_date:int
     ndcnumber:int
     batch_id:int
     serialnumberofgoods:int
      




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):  
     return pwd_context.hash(password)
def verify_password(password: str, hashed_password: str):
     return pwd_context.verify(password, hashed_password)

@app.get("/",response_class=HTMLResponse)
def home(request: Request):
     return templates.TemplateResponse("login.html",{"request": request})
@app.post("/",response_class=HTMLResponse)

def post_login_page(request:Request,email:str=Form(...),password:str=Form(...)):
     # logindetails = signup(Username=username, Password= password)
     useremail=email
     userpassword=password
     login=signup_collection.find_one({"Email":email})
     try:
          if not login:
                return templates.TemplateResponse("login.html",{'request':request})
          else:
              if verify_password(userpassword,login['Password']):
                 return templates.TemplateResponse("index.html",{'request':request})
     except Exception as e:
         print(e)
          

@app.get("/signup",response_class=HTMLResponse)
def moni(request: Request):
     return templates.TemplateResponse("signup1.html",{"request": request})
@app.post('/signup',response_class=HTMLResponse)
def post_signup_page(request: Request,username:str=Form(...),email:str=Form(...),password:str=Form(...),cpassword:str=Form(...)):
   
    hashed_password = hash_password(password)
    print(hashed_password)
     # hashed_password = hash_password(password)
    user = signup(Username=username,Password=hashed_password,Email=email)
    if password==cpassword:
       signup_collection.insert_one(dict(user))
       return templates.TemplateResponse("signup1.html",{"request":request,"message":"user was created succesfully"})
    else:
        return templates.TemplateResponse("signup1.html",{"request":request, "message":"password and confirmpassword did not matched"})

@app.get("/index",response_class=HTMLResponse)
def dashboard(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})
@app.get('/DeviceData', response_class=HTMLResponse, name="DeviceData")
async def createshipment(request: Request):
    createshipment = []
    createshipment_all = db["Device_data"].find({})
    print(createshipment_all)
    print("show data")
    for i in createshipment_all:
        createshipment.append(i)
        print(createshipment_all)
    return templates.TemplateResponse("DeviceData.html", {"request": request, "createshipment": createshipment})


# @app.get("/Shipment",response_class=HTMLResponse)
# def shipment(request: Request):
#       return templates.TemplateResponse(" shipment.html", {"request": request})
@app.get('/createshipment', response_class=HTMLResponse)
def shipment(request: Request):

    return templates.TemplateResponse("createshipment.html", {"request": request})

@app.post('/createshipments',response_class=HTMLResponse )
def post(request: Request,Shipment_invoicenumber:str=Form(...),Container_number:str=Form(...), Description:str=Form(...),Route_details:str=Form(...),Goods_type:str=Form(...), Device:str=Form(...),Expected_Delivary_Date:str=Form(...), Po_number:int=Form(...), Delivery_number:int=Form(...),Ndc_number:int=Form(...),Batch_id:int=Form(...),Serialnumberofgoods:int=Form(...)):

    shipments = Createshipment ( shipment_invoice_number = Shipment_invoicenumber , container_number = Container_number, description = Description , route_details = Route_details,goods_type = Goods_type, device= Device, expected_Delivery_Date = Expected_Delivary_Date , po_number = Po_number,delivery_date =Delivery_number , ndcnumber= Ndc_number, batch_id= Batch_id,  serialnumberofgoods= Serialnumberofgoods)
    shipment_collection.insert_one(dict(shipments))
    return templates.TemplateResponse("createshipment.html",{"request": request,"message":"Shipment  was created succesfully"})
#     shipmets = shipment_collection.insert_one(dict(shipments))
#           return templates.TemplateResponse("createshipment.html",{"request":request})
