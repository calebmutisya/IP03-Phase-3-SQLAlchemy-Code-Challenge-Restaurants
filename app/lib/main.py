from config import *
from models import Customer, Review, Restaurant
from sqlalchemy.sql import func
#RESTAURANT
#returns a collection of all the reviews for the `Restaurant`
def reviews(restaurant_id):
    reviews_collection = session.query(Review).filter(Review.restaurant_id == restaurant_id).all()
    return reviews_collection
#returns a collection of all the customers who reviewed the `Restaurant`
def customers(restaurant_id):
    return session.query(Customer).join(Review).filter(Review.restaurant_id == restaurant_id).all()
#returns _one_ restaurant instance for the restaurant that has the highest   price
def fanciest():
    return session.query(Restaurant).order_by(Restaurant.price.desc()).first()
#should return an list of strings with all the reviews for this restaurant
def all_reviews(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    return [full_review(review) for review in restaurant.reviews]

#CUSTOMER
#returns the full name of the customer, with the first name and the last name  concatenated, Western style.
def full_name(customer_id):
    customer = session.query(Customer).get(customer_id)
    return f"{customer.first_name} {customer.last_name}"

#returns the restaurant instance that has the highest star rating from this customer
def favorite_restaurant(customer_id):
    return (
        session.query(Restaurant)
        .join(Review)
        .filter(Review.customer_id == customer_id)
        .group_by(Restaurant.id)
        .order_by(func.avg(Review.star_rating).desc())
        .first()
    )

#takes a `restaurant` (an instance of the `Restaurant` class) and a rating- creates a new review for the restaurant with the given `restaurant_id`
def add_review(customer, restaurant, rating):
    new_review = Review(customer=customer, restaurant=restaurant, star_rating=rating)
    session.add(new_review)
    session.commit()
    return new_review

#takes a `restaurant` (an instance of the `Restaurant` class) and
#- removes **all** their reviews for this restaurant
def delete_reviews(customer, restaurant):
    reviews_to_delete = [review for review in customer.reviews if review.restaurant == restaurant]
    for review in reviews_to_delete:
        session.delete(review)
    session.commit()



#should return a collection of all the reviews that the `Customer` has left
def customer_reviews(customer):
    return customer.reviews

#should return a collection of all the restaurants that the `Customer` has
def reviewed_restaurants(customer):
    return [review.restaurant for review in customer.reviews]


#REVIEW
#should return a string formatted as follows:
# Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
def full_review(review):
    try:
        restaurant_name = review.restaurant.name if review.restaurant else "Unknown Restaurant"
        
        if review.customer_id:
            customer = session.query(Customer).get(review.customer_id)
            customer_name = full_name(customer.id)  # Using the modified full_name function
        else:
            customer_name = "Unknown Customer"
        
        return f"Review for {restaurant_name} by {customer_name}: {review.star_rating} stars."
    except Exception as e:
        return f"Error in full_review: {e}"
#should return the `Customer` instance for this review
def reviewer(review):
    return review.customer

#should return the `Restaurant` instance for this review
def reviewed_restaurant (review):
    return review.restaurant
