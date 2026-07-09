from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import Text

from database import base


class Patient(base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index = True)
    full_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email_address = Column(String(100), unique=True, nullable=False)
    glucose = Column(Float, nullable=False)
    haemoglobin = Column(Float, nullable=False)
    cholesterol = Column(Float, nullable=False)
    remarks = Column(Text, nullable=True)