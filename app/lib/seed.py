
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Customer, Review, Restaurant
from sqlalchemy import create_engine

engine=create_engine("sqlite:///database.sqlite")

Session= sessionmaker(bind=engine)
session= Session()

fake=Faker()
print('Seeding data ...')
# Create a new customer
