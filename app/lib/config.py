from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship,joinedload
from models import Base, Restaurant, Review, Customer

# Set up SQLite database engine
import os

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(app_path, 'database.sqlite')
engine = create_engine(f"sqlite:///{db_path}")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()