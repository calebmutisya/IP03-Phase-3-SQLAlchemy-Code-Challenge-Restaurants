from sqlalchemy import Column,String,Integer,ForeignKey

from sqlalchemy.orm import declarative_base, relationship

Base= declarative_base()

class Restaurant(Base):
    __tablename__='restaurants'

    id= Column(Integer, primary_key=True)
    name= Column(String, nullable=False, unique=True)
    price= Column(Integer, nullable=False)

    reviews= relationship('Review', back_populates='restaurant')
    #returns a collection of all the reviews for the `Restaurant`
    def reviews(self):
        return self.reviews
    #returns a collection of all the customers who reviewed the `Restaurant`
    def customers(self):
        return [review.customer for review in self.reviews]
    

class Customer(Base):
    __tablename__='customers'
    
    id= Column(Integer, primary_key=True)
    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)

    reviews= relationship('Review', back_populates='customer')

    #should return a collection of all the reviews that the `Customer` has left
    def reviews(self):
        return self.reviews
    
    #should return a collection of all the restaurants that the `Customer` has
    def restaurants(self):
        return [review.restaurant for review in self.reviews]


class Review(Base):
    __tablename__='reviews'

    id=Column(Integer, primary_key=True)
    star_rating= Column(Integer, nullable=False)
    restaurant_id= Column(Integer, ForeignKey('restaurant.id'), nullable=False)
    customer_id= Column(Integer, ForeignKey('customers.id'), nullable=False)

    restaurant=relationship('Restaurant', back_populates='reviews')
    customer= relationship('Customer', back_populates='reviews')

    #should return the `Customer` instance for this review
    def customer(self):
        return self.customer
    
    #should return the `Restaurant` instance for this review
    def restaurant(self):
        return self.restaurant