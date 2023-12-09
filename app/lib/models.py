from sqlalchemy import Column,String,Integer,ForeignKey

from sqlalchemy.orm import declarative_base, relationship

Base= declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

class Customer(Base):
    __tablename__='customers'

class Review(Base):
    __tablename__='reviews'