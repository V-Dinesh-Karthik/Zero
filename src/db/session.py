from sqlmodel import SQLModel, create_engine, Session
from db.models import User
from db.models import Text
from db.models import Keyword
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)   

