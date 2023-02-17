from pydantic import BaseModel

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
      

