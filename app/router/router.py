from fastapi import APIRouter, Request

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse # For returning an HTML response
from fastapi.templating import Jinja2Templates  # For rendering HTML templates with Jinja2
from fastapi import  Form, Request # For creating the FastAPI application and handling requests
from passlib.context import CryptContext # For password hashing and verification
from router import router
from models.models import signup,Createshipment

from config import signup_collection,shipment_collection,db
router = APIRouter()

templates = Jinja2Templates(directory="Templates") 
# This code defines a password hashing and verification system using the bcrypt algorithm.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):  
     return pwd_context.hash(password)
def verify_password(password: str, hashed_password: str):
     return pwd_context.verify(password, hashed_password)

     ##########Rendering the signup page###########
@router.get("/signup",response_class=HTMLResponse)
def moni(request: Request):
     return templates.TemplateResponse("signup1.html",{"request": request})
#  #######To store the New user details in mongodb######3
@router.post('/signup',response_class=HTMLResponse)
def post_signup_page(request: Request,username:str=Form(...),email:str=Form(...),password:str=Form(...),cpassword:str=Form(...)):
   
    hashed_password = hash_password(password)
    print(hashed_password)
  
    user = signup(Username=username,Password=hashed_password,Email=email)
    if password==cpassword:
       signup_collection.insert_one(dict(user))
       return templates.TemplateResponse("signup1.html",{"request":request,"message":"user was created succesfully"})
    else:
        return templates.TemplateResponse("signup1.html",{"request":request, "message":"password and confirmpassword did not matched"})
# ######Rendering the login page########
@router.get("/",response_class=HTMLResponse)
def home(request: Request):
     # #####To athenticate the registered user########
     return templates.TemplateResponse("login.html",{"request": request})
@router.post("/",response_class=HTMLResponse)

def post_login_page(request:Request,email:str=Form(...),password:str=Form(...)):
     
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
     # ######Rendering the dashboard page###########
@router.get("/index",response_class=HTMLResponse)
def dashboard(request: Request):
     return templates.TemplateResponse("index.html", {"request": request})
     # Rendering the create shipment page##
@router.get('/createshipment', response_class=HTMLResponse)
def shipment(request: Request):

    return templates.TemplateResponse("createshipment.html", {"request": request})
# To store the shipment details in mongodb
@router.post('/createshipments',response_class=HTMLResponse )
def post(request: Request,Shipment_invoicenumber:str=Form(...),Container_number:str=Form(...), Description:str=Form(...),Route_details:str=Form(...),Goods_type:str=Form(...), Device:str=Form(...),Expected_Delivary_Date:str=Form(...), Po_number:int=Form(...), Delivery_number:int=Form(...),Ndc_number:int=Form(...),Batch_id:int=Form(...),Serialnumberofgoods:int=Form(...)):

    shipments = Createshipment ( shipment_invoice_number = Shipment_invoicenumber , container_number = Container_number, description = Description , route_details = Route_details,goods_type = Goods_type, device= Device, expected_Delivery_Date = Expected_Delivary_Date , po_number = Po_number,delivery_date =Delivery_number , ndcnumber= Ndc_number, batch_id= Batch_id,  serialnumberofgoods= Serialnumberofgoods)
    shipment_collection.insert_one(dict(shipments))
    return templates.TemplateResponse("createshipment.html",{"request": request,"message":"Shipment  was created succesfully"})
# To store the device data in mongidb
@router.get('/DeviceData', response_class=HTMLResponse, name="DeviceData")
async def createshipment(request: Request):
    createshipment = []
    createshipment_all =db["Device_data"].find({})
    print(createshipment_all)
    print("show data")
    for i in createshipment_all:
        createshipment.append(i)
        print(createshipment_all)
    return templates.TemplateResponse("DeviceData.html", {"request": request, "createshipment": createshipment})

## ************** Devicedata API END *********##########