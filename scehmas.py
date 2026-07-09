from pydantic import BaseModel
from pydantic import EmailStr
from datetime import date

class patientcreate(BaseModel):
    full_name: str
    date_of_birth: date
    email_address: EmailStr
    glucose: float
    haemoglobin: float
    cholesterol: float
    
    
