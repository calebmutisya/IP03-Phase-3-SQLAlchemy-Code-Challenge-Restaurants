from main import reviews, customers,fanciest,all_reviews
from main import full_name,favorite_restaurant,add_review,delete_reviews,customer_reviews,reviewed_restaurants,add_review, delete_reviews,customer_reviews,reviewed_restaurant
from main import full_review,reviewer,reviewed_restaurant
from main import *

#Restaurant
print(">>>>>>>>>>>> RESTAURANT OPERATIONS <<<<<<<<<<<")
print("***** collection of all the reviews for Restaurant Pitts Callahan *****")
restaurant_id=2
restaurant_reviews = reviews(restaurant_id)
for review in restaurant_reviews:
    print(f"Review ID: {review.id}, Star Rating: {review.star_rating}")


print("***** a collection of all the customers who reviewed the Restaurant Pitts Callahan *****")
restaurant_id = 2
restaurant_customers = customers(restaurant_id)

for customer in restaurant_customers:
    print(f"Customer ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

print("***** the restaurant that has the highest price *****")
fanciest_restaurant = fanciest()
print(f"The restaurant with the highest price is {fanciest_restaurant.name}")

print("***** A list with all the reviews for the Restaurant Pitts Callahan *****")
restaurant_id = 2
all_reviews_list = all_reviews(restaurant_id)
for review in all_reviews_list:
    print(review)



#Customer
print(">>>>>>>>>>>> CUSTOMER OPERATIONS <<<<<<<<<<<")

# customer_id = 1
# customer_name = full_name(customer_id)
# print(f"***** Full name of customer with ID {customer_id} *****")
# print(f"Customer Full Name: {customer_name}")

# # Test favorite_restaurant function
# customer_id = 1
# favorite_restaurant_instance = favorite_restaurant(customer_id)
# print(f"***** The restaurant instance that has the highest star rating from this customer *****")
# print(f"Favorite Restaurant: {favorite_restaurant_instance.name}")


# # Test add_review function
# customer = session.query(Customer).first()
# restaurant = session.query(Restaurant).first()
# rating = 5
# new_review = add_review(customer, restaurant, rating)
# print("***** Add a new review *****")
# print(f"New Review ID: {new_review.id}, Star Rating: {new_review.star_rating}")


# # Test delete_reviews function
# delete_reviews(customer, restaurant)
# print("***** Delete all reviews for the customer and restaurant *****")
# print("Reviews after deletion:")
# for review in customer_reviews(customer):
#     print(f"Review ID: {review.id}, Star Rating: {review.star_rating}")


# # Test customer_reviews function
# print("***** A collection of all the reviews that the Customer has left *****")
# customer_reviews_list = customer_reviews(customer)
# for review in customer_reviews_list:
#     print(f"Review ID: {review.id}, Star Rating: {review.star_rating}")


# # Test reviewed_restaurants function
# print("***** A collection of all the restaurants that the Customer has reviewed *****")
# reviewed_restaurants_list = reviewed_restaurants(customer)
# for reviewed_restaurant in reviewed_restaurants_list:
#     print(f"Restaurant ID: {reviewed_restaurant.id}, Name: {reviewed_restaurant.name}")


#Review
print(">>>>>>>>>>>> REVIEW OPERATIONS <<<<<<<<<<<")

# # Test full_review function
# review = session.query(Review).first()
# print("***** Full review details *****")
# print(full_review(review))

# # Test reviewer function
# print("***** The Customer instance for this review *****")
# reviewer_instance = reviewer(review)
# print(f"Reviewer: {reviewer_instance.full_name()}")

# # Test reviewed_restaurant function
# print("***** The Restaurant instance for this review *****")
# reviewed_restaurant_instance = reviewed_restaurant(review)
# print(f"Reviewed Restaurant: {reviewed_restaurant_instance.name}")