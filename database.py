#when i directly use sqlalchemy
# import sqlalchemy as db
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base

#connect sqlite database with python using engine and connection
# engine  = db.create_engine('sqlite:///healthdata.db')
# connection = engine.connect()

# #metadata object holds information about tables and schema
# metadata = db.MetaData()
# patients = db.Table('patients',metadata,
#                     db.Column('id', db.Integer, primary_key=True),
#                     db.Column("full_name", db.String(100), nullable=False),
#                     db.Column("date_of_birth", db.Date, nullable=False),
#                     db.Column("email_address", db.String(100), unique=True, nullable=False),
#                     db.Column("glucose", db.Float, nullable=False),
#                     db.Column("haemoglobin", db.Float, nullable=False),
#                     db.Column("cholesterol", db.Float, nullable=False),
#                     db.Column("remarks", db.Text, nullable=True)
#                     )

# metadata.create_all(engine)  # Create the table in the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

database_url = 'sqlite:///healthdata.db'

engine = create_engine(database_url,connect_args={"check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()