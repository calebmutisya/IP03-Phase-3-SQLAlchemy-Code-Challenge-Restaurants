from main import reviews, customers,fanciest,all_reviews
from main import full_name,favorite_restaurant,add_review,delete_reviews,customer_reviews,reviewed_restaurants,add_review, delete_reviews,customer_reviews,reviewed_restaurant
from main import full_review,reviewer,reviewed_restaurant

#Restaurant
print(">>>>>>>>>>>> RESTAURANT OPERATIONS <<<<<<<<<<<")
print("***** collection of all the reviews for Restaurant Pitts Callahan *****")
restaurant_id=2
restaurant_reviews = reviews(restaurant_id)
for review in restaurant_reviews:
    print(f"Review ID: {review.id}, Star Rating: {review.star_rating}")

#Customer
print(">>>>>>>>>>>> CUSTOMER OPERATIONS <<<<<<<<<<<")

#Review
print(">>>>>>>>>>>> REVIEW OPERATIONS <<<<<<<<<<<")