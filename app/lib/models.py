from sqlalchemy import Column,String,Integer,ForeignKey

from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
engine=create_engine("sqlite:///database.sqlite")

Session= sessionmaker(bind=engine)
session= Session()

Base= declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

    id= Column(Integer, primary_key=True)
    name= Column(String, nullable=False, unique=True)
    price= Column(Integer, nullable=False)

    reviews= relationship('Review', back_populates='restaurant')
    
class Customer(Base):
    __tablename__='customers'
    
    id= Column(Integer, primary_key=True)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)

    reviews= relationship('Review', back_populates='customer')

class Review(Base):
    __tablename__='reviews'

    id=Column(Integer, primary_key=True)
    star_rating= Column(Integer, nullable=False)
    restaurant_id= Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    customer_id= Column(Integer, ForeignKey('customers.id'), nullable=False)

    restaurant=relationship('Restaurant', back_populates='reviews')
    customer= relationship('Customer', back_populates='reviews')
