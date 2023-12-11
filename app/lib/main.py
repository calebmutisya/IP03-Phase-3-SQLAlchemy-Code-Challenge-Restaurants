from config import *

#RESTAURANT
#returns a collection of all the reviews for the `Restaurant`
def reviews(self):
    return self.reviews
#returns a collection of all the customers who reviewed the `Restaurant`
def customers(self):
    return [review.customer for review in self.reviews]
#returns _one_ restaurant instance for the restaurant that has the highest   price
@classmethod
def fanciest(cls):
    return cls.query.order_by(cls.price.desc()).first()
#should return an list of strings with all the reviews for this restaurant
def all_reviews(self):
    return [review.full_review() for review in self.reviews]

#CUSTOMER
#returns the full name of the customer, with the first name and the last name  concatenated, Western style.
def full_name(self):
    return f"{self.first_name} {self.last_name}"

#returns the restaurant instance that has the highest star rating from this customer
def favorite_restaurant(self):
    return max([review.restaurant for review in self.reviews], key= lambda r: r.average_rating())

#takes a `restaurant` (an instance of the `Restaurant` class) and a rating- creates a new review for the restaurant with the given `restaurant_id`
def add_review(self,restaurant,rating):
    new_review= Review(customer=self, restaurant=restaurant, star_rating=rating)
    return new_review

#takes a `restaurant` (an instance of the `Restaurant` class) and
#- removes **all** their reviews for this restaurant
def delete_reviews(self, restaurant):
    reviews_to_delete= [review for review in self.reviews if review.restaurant == restaurant]
    for review in reviews_to_delete:
        session.delete(review)
    session.commit()



#should return a collection of all the reviews that the `Customer` has left
def reviews(self):
    return self.reviews

#should return a collection of all the restaurants that the `Customer` has
def restaurants(self):
    return [review.restaurant for review in self.reviews]


#REVIEW
#should return a string formatted as follows:
# Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
def full_review(self):
    return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."
#should return the `Customer` instance for this review
def customer(self):
    return self.customer

#should return the `Restaurant` instance for this review
def restaurant(self):
    return self.restaurant
