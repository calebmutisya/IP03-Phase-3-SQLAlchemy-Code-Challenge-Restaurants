
from faker import Faker
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from models import Customer, Review, Restaurant
from sqlalchemy import create_engine

import os

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(app_path, 'database.sqlite')
engine = create_engine(f"sqlite:///{db_path}")


Session= sessionmaker(bind=engine)
session= Session()

fake=Faker()
print('Seeding reataurant ...')
# Create restaurants
def seed_restaurant():
    restaurant=[
        Restaurant(name=fake.company(), price= fake.random_int(min=40, max=90))
        for i in range(6) 
     ]
    session.add_all(restaurant)
    session.commit()

#Create customers
print('Seeding customer')
def seed_customer():
    customer=[
        Customer(first_name=fake.first_name(), last_name=fake.last_name())
        for i in range(6) 
     ]
    session.add_all(customer)
    session.commit()    

#Create reviews
print('Seeding review')
def seed_review():
    all_customers= session.query(Customer).all()
    all_restaurants=session.query(Restaurant).all()
    review=[
        Review(
            star_rating=fake.random_int(min=1, max=5), 
            restaurant_id= fake.random_element(all_restaurants).id, 
            customer_id= fake.random_element(all_customers).id
        )
        for i in range(6) 
     ]
    session.add_all(review)
    session.commit() 

# seed_restaurant()

# seed_customer()

# seed_review()
