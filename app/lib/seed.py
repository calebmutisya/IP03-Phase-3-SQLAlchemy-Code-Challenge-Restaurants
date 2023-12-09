
from faker import Faker
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from models import Customer, Review, Restaurant
from sqlalchemy import create_engine

engine=create_engine("sqlite:///database.sqlite")

Session= sessionmaker(bind=engine)
session= Session()

fake=Faker()
print('Seeding reataurant ...')
# Create restaurants
def seed_restaurant():
    for _ in range(5):  # Adjust the number of restaurants as needed
        restaurant = Restaurant(
            name=fake.company(),
            price=fake.random_int(min=1, max=5)
        )
        session.add(restaurant)
    session.commit()

#Create customers
print('Seeding customer')
def seed_customer():
    for _ in range(10):  # Adjust the number of customers as needed
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
    session.commit()

#Create reviews
print('Seeding review')
def seed_review():
    for _ in range(20):  # Adjust the number of reviews as needed
        restaurant = session.query(Restaurant).order_by(func.random()).first()
        customer = session.query(Customer).order_by(func.random()).first()
        review = Review(
            star_rating=fake.random_int(min=1, max=5),
            restaurant=restaurant,
            customer=customer
        )
        session.add(review)
    session.commit()