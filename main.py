# from pydanti_schema import patientcreate
# from fastapi import FastAPI
# from fastapi import Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from model import patienttable as Patient
# from ai_service import generate_health_remark
# app = FastAPI()





# @app.post("/add_patient")
# def add_patient(patient : patientcreate,db: Session = Depends(get_db)):
#     remarks = generate_health_remark(patient.glucose, patient.haemoglobin, patient.cholesterol)
#     new_patient = Patient(
        
#         full_name=patient.full_name,
#         date_of_birth=patient.date_of_birth,
#         email_address=patient.email_address,
#         glucose=patient.glucose,
#         haemoglobin=patient.haemoglobin,
#         cholesterol=patient.cholesterol,
       
#     )
#     new_patient.remarks = remarks
#     db.add(new_patient)
#     db.commit()
#     db.refresh(new_patient)
#     return {"message": "Patient added successfully", "remarks": remarks}

# @app.get("/get_patient/{patient_name}")
# def get_one_patient(patient_name:str,db: Session = Depends(get_db)):
#     patient_data = db.query(Patient).filter(Patient.full_name == patient_name).first()
#     if patient_data:
#         return patient_data 
#     else:
#         return {"message": "Patient not found"}


# # @app.put("/update_patient/{patient_name}")
# # def update_patient(patient_name:str, patient_data: patientcreate, db: Session = Depends(get_db)):
# #     existing_patient = db.query(Patient).filter(Patient.full_name == patient_name).first()
# #     if existing_patient:
# #         existing_patient.full_name = patient_data.full_name
# #         existing_patient.date_of_birth = patient_data.date_of_birth
# #         existing_patient.email_address = patient_data.email_address
# #         existing_patient.glucose = patient_data.glucose
# #         existing_patient.haemoglobin = patient_data.haemoglobin
# #         existing_patient.cholesterol = patient_data.cholesterol
# #         existing_patient.remarks = generate_health_remark(patient_data)
        
# #         db.commit()
# #         db.refresh(existing_patient)
# #         return {"message": "Patient updated successfully", "remarks": existing_patient.remarks}
# #     else:
# #         return {"message": "Patient not found"}

# # @app.delete("/delete_patient/{patient_id}")
# # def delete_patient(patient_id:int, db: Session = Depends(get_db)):
# #     existing_patient = db.query(patient).filter(patient.id == patient_id).first()
# #     if existing_patient:
# #         db.delete(existing_patient)
# #         db.commit()
# #         return {"message": "Patient deleted successfully"}
# #     else:
# #         return {"message": "Patient not found"}

from fastapi import FastAPI
from  scehmas import patientcreate
from fastapi import Depends
from  database import get_db
from model import Patient
from ai_service import generate_health_remark
app = FastAPI()


@app.post("/add_patient")
def add_patient(patient : patientcreate,db = Depends(get_db)):
    existing_patient= db.query(Patient).filter(Patient.full_name == patient.full_name, Patient.email_address == patient.email_address).first()
    if existing_patient:
        return {"message":"patient already exists"}  
    else:
        remarks = generate_health_remark(patient.glucose,patient.haemoglobin,patient.cholesterol)
        new_patient = Patient(
        full_name = patient.full_name,
        date_of_birth = patient.date_of_birth,
        email_address = patient.email_address,
        glucose = patient.glucose,  
        haemoglobin = patient.haemoglobin,
        cholesterol = patient.cholesterol,
        remarks = remarks

    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient.remarks


@app.get("/get_patient")
def get_one_patient(patient_name: str, email_address: str, db = Depends(get_db)):
    patient_data=db.query(Patient).filter(Patient.full_name == patient_name, Patient.email_address == email_address).first()
    if patient_data:
        return patient_data
    else :
        return {"message": "patient not found"}


@app.put("/update_patient")
def update_patient(patient_name: str , email_address : str , patient_data: patientcreate , db = Depends(get_db)):
    d =db.query(Patient).filter(Patient.full_name == patient_name , Patient.email_address == email_address).first()
    if not d:
        return {"message": "Patient not found"}
    else:
        d.full_name = patient_data.full_name
        d.date_of_birth = patient_data.date_of_birth
        d.email_address = patient_data.email_address
        d.glucose = patient_data.glucose
        d.haemoglobin = patient_data.haemoglobin
        d.cholesterol = patient_data.cholesterol
        d.remarks = generate_health_remark(patient_data.glucose , patient_data.haemoglobin , patient_data.cholesterol)
        db.commit()
        db.refresh(d)
        return {"message": "Patient updated successfully", "remarks": d.remarks}
 
@app.delete("/delete_patient")
def delete_patient(patient_name:str , email_address:str , db = Depends(get_db)):
    d = db.query(Patient).filter(Patient.full_name ==  patient_name, Patient.email_address == email_address).first()
    if not d:
        return {"message": "Patient not found"}
    else:
        db.delete(d)
        db.commit()
        return {"message": "Patient deleted successfully"}