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

templates = Jinja2Templates(directory="templates") 
# This code defines a password hashing and verification system using the bcrypt algorithm.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):  
     return pwd_context.hash(password)
def verify_password(password: str, hashed_password: str):
     return pwd_context.verify(password, hashed_password)
@router.get("/signup",response_class=HTMLResponse)
def signup(request: Request):
     return templates.TemplateResponse("signup1.html",{"request": request})

#    To store the signup details in the database
@router.post('/signup',response_class=HTMLResponse)
def signup(request: Request,username:str=Form(...),email:str=Form(...),password:str=Form(...),cpassword:str=Form(...)):
   
    hashed_password = hash_password(password)
    print(hashed_password)
    
    users = db["users"].find_one({"Email": email}) 
    try:
      if not users:
            signup_collection.insert_one({"Username": username, 'Email': email,"Password": hashed_password})
            return templates.TemplateResponse("signup1.html", {'request': request, "message": "User was created successfully"})
    except Exception as e:
        print(e)
    return templates.TemplateResponse("signup1.html", {"request": request, "message": "user already exists"})
@router.get("/",response_class=HTMLResponse)
def login(request: Request):
     return templates.TemplateResponse("login.html",{"request": request})
#  ########To check the signup details given in database matches or not in login page#######

@router.post("/",response_class=HTMLResponse)

def login(request:Request,email:str=Form(...),password:str=Form(...)):
     
     useremail=email
     userpassword=password
     login=signup_collection.find_one({"Email":email})
     try:
          if  login and verify_password(userpassword,login['Password']):
               return templates.TemplateResponse("Dashboard.html",{'request':request})
          else:
            #   if verify_password(userpassword,login['Password']):
                
               return templates.TemplateResponse("login.html",{'request':request,"message":"password or email did not matched"})
          
     except Exception as e:
         print(e)
     # ######Rendering the dashboard page###########
@router.get("/Dashboard",response_class=HTMLResponse)
def Dashboard(request: Request):
     return templates.TemplateResponse("Dashboard.html", {"request": request})



     # Rendering the create shipment page##
@router.get('/createshipment', response_class=HTMLResponse)
def shipment(request: Request):

    return templates.TemplateResponse("createshipment.html", {"request": request})
# To store the shipment details in mongodb
@router.post('/createshipments',response_class=HTMLResponse )
def post(request: Request,Shipment_invoice_number:str=Form(...),Container_number:str=Form(...), Description:str=Form(...),Route_details:str=Form(...),Goods_type:str=Form(...), Device:str=Form(...),Expected_Delivary_Date:str=Form(...), Po_number:int=Form(...), Delivery_number:int=Form(...),Ndc_number:int=Form(...),Batch_id:int=Form(...),Serialnumberofgoods:int=Form(...)):

    shipments = Createshipment ( shipment_invoice_number = Shipment_invoice_number , container_number = Container_number, description = Description , route_details = Route_details,goods_type = Goods_type, device= Device, expected_Delivery_Date = Expected_Delivary_Date , po_number = Po_number,delivery_date =Delivery_number , ndcnumber= Ndc_number, batch_id= Batch_id,  serialnumberofgoods= Serialnumberofgoods)
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