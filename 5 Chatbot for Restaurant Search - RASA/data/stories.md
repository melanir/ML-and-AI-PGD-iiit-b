## cuisine_not_available
* greet
    - utter_greet
* food_request
	- utter_food_request
* restaurant_search{"location": "cochin"}
    - slot{"location": "cochin"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "sushi"}
    - slot{"cuisine": "sushi"}
	- check_cuisine
	- slot{"check_cuis": false}
	- utter_cuisine_unknown
* restaurant_search{"cuisine": "north indian"}
	- slot{"cuisine": "north indian"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "750", "price_two": "1200"}
	- slot{"price_one": "750"}
	- slot{"price_two": "1200"}	
	- price_category
	- slot{"price_range": "high"}	
	- action_search_restaurants
	- utter_ask_want_mail
* affirm
	- utter_ask_emailid
* emailID{"email_id": "something@yahoo.com"}
	- slot{"email_id": "something@yahoo.com"}
	- action_mail
	- utter_mailed
	- utter_search_again
* negate
	- utter_goodbye
	
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "cochin"}
	- slot{"location": "cochin"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
	- slot{"cuisine": "north indian"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_range": "Lesser than Rs. 300"}
	- slot{"price_range": "low"}
	- price_category
	- action_search_restaurants
	- utter_ask_want_mail
* emailID{"email_id": "something@yahoo.com"}
	- slot{"email_id": "something@yahoo.com"}
	- action_mail
	- utter_mailed
	- utter_search_again
* negate
* goodbye
	- utter_goodbye
	
	
## incorrect location specified
* greet
    - utter_greet
* restaurant_search{"location": "deli"}
	- slot{"location": "deli"}
	- check_location
	- slot{"check_loc": false}
	- utter_enter_city
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
	- slot{"cuisine": "mexican"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_range": "Lesser than Rs. 300"}
	- slot{"price_range": "low"}
	- price_category
	- action_search_restaurants
	- utter_ask_want_mail
* affirm
	- utter_ask_emailid
* emailID{"email_id": "something@gmail.com"}
	- action_mail
	- utter_mailed
	- utter_search_again
* negate
	- utter_goodbye


## location specified in first search
* greet
    - utter_greet
* restaurant_search{"location": "deli"}
	- slot{"location": "delhi"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_range": "Between Rs. 300 and Rs. 700"}
	- slot{"price_range": "mid"}
	- price_category
	- action_search_restaurants
	- utter_ask_want_mail
* negate
* goodbye
	- utter_goodbye


## location specified in first search
* greet
    - utter_greet
* restaurant_search{"location": "deli"}
	- slot{"location": "delhi"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_range": "Between Rs. 300 and Rs. 700"}
	- slot{"price_range": "mid"}
	- price_category
	- action_search_restaurants
	- utter_ask_want_mail
* negate
	- utter_goodbye


## no_price_limit
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
	- slot{"cuisine": "North Indian"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* negate
	- price_category
	- slot{"price_range": "high"}
	- action_search_restaurants
	- utter_ask_want_mail
* negate
	- utter_search_again
* negate
	- utter_goodbye
	
	
## unservicable location
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "italy"}
	- slot{"location": "italy"}
	- check_location
	- slot{"check_loc": false}
	- utter_enter_city
* restaurant_search{"location": "milan"}
	- slot{"location": "milan"}
	- check_location
	- slot{"check_loc": false}
	- utter_dont_operate
	- utter_search_again
* negate
	- utter_goodbye
	
	
## interactive_story_1_stop
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
	- slot{"cuisine": "chinese"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "500"}
	- slot{"price_one": "500"}
	- price_category
	- slot{"price_range": "mid"}
	- action_search_restaurants
	- utter_ask_want_mail
* negate
	- utter_search_again
* negate
* stop
	- utter_goodbye
	

## incorrect_cuisine_specified
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "continental"}
	- slot{"cuisine": "continental"}
	- check_cuisine
	- slot{"check_cuis": false}
	- utter_cuisine_unknown
* restaurant_search{"cuisine": "american"}
	- slot{"cuisine": "american"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "2500"}
	- slot{"price_one": "2500"}
	- price_category
	- slot{"price_range": "high"}
	- action_search_restaurants
	- utter_ask_want_mail
* stop
	- utter_goodbye


## all_three_together_incorrect_cuisine
* greet
    - utter_greet
* restaurant_search{"location": "nagpur", "cuisine": "lebanese", "price_one": "1000"}
	- slot{"location": "nagpur"}
	- slot{"cuisine": "lebanese"}
	- slot{"price_one": "1000"}
	- check_location
	- slot{"check_loc": true}
	- check_cuisine
	- slot{"check_cuis": false}
	- utter_cuisine_unknown
* restaurant_search{"cuisine": "mexican"}
	- slot{"cuisine": "mexican"}
	- check_cuisine
	- slot{"check_cuis": true}
	- price_category
	- slot{"price_range": "high"}
	- action_search_restaurants
	- utter_ask_want_mail
* affirm
	- utter_ask_emailid
* emailID{"email_id": "whattever125@gmail.com"}
	- slot{"email_id": "whattever125@gmail.com"}
	- action_mail
	- utter_mailed
	- utter_search_again
* negate
	- utter_goodbye
	
	
## location_and_price
* greet
    - utter_greet
* restaurant_search{"location": "bengaluru", "price_one": "300", "price_two": "700"}
	- slot{"location": "bengaluru"}
	- slot{"price_one": "300"}
	- slot{"price_one": "700"}
	- check_location
	- slot{"check_loc": true}
	- price_category
	- slot{"price_range": "mid"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
	- slot{"cuisine": "mexican"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_want_mail
* emailID
	- utter_ask_emailid
* emailID{"email_id": "ahbcdj@dkj.com"}
	- slot{"email_id": "ahbcdj@dkj.com"}
	- action_mail
	- utter_mailed
	- utter_search_again
* negate
	- utter_goodbye
	
	
## changing_location
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
	- check_location
	- slot{"check_loc": false}
	- utter_enter_city
* restaurant_search{"location": "rishikesh"}
	- slot{"location": "rishikesh"}
	- check_location
	- slot{"check_loc": false}
	- utter_dont_operate
	- utter_search_again
* restaurant_search{"location": "Allahabad"}
	- slot{"location": "Allahabad"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
	- slot{"cuisine": "mexican"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "500"}
	- slot{"price_one": "500"}
	- price_category
	- slot{"price_range": "mid"}
	- action_search_restaurants
	- slot{"restaurent_list": "\n\n1\nMcDonald's in 34-B, M.G. Marg, Allahabad, Zone No-3, Allahabad (Uttar Pradesh)  has been rated 4.3\nBudget for two: 500\n\n2\nKFC in 229/71, Ground Floor, P Square Mall, MG Marg, Civil Lines, Allahabad has been rated 4.3\nBudget for two: 450\n\n3\nWell Bean Cafe in 33/5A, First Floor , Above Subway,Tashkand Marg,Civil Lines, Allahabad has been rated 4.3\nBudget for two: 500\n\n4\nPizza Hut in Shop 31/31, S. P. Marg, Civil Lines, Allahabad has been rated 4.2\nBudget for two: 600\n\n5\nHot N Cool in 194, Opposite Anand Bhawan, Colonel Ganj, Allahabad has been rated 4.2\nBudget for two: 450"}
	- utter_ask_want_mail
* negate
	- utter_search_again
* negate
	- utter_goodbye

	
## mid_price
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
	- slot{"location": "kolkata"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
	- slot{"cuisine": "american"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "350"}
	- slot{"price_one": "350"}
	- price_category
	- slot{"price_range": "mid"}
	- action_search_restaurants
	- slot{"restaurent_list": "\n\n1\nPizza Hut in 32, 3rd Floor, Avani Riverside Mall, Jagat Banerjee Ghat Road, Shibpur, Howrah has been rated 4.0\nBudget for two: 600\n\n2\nForkstruck in 188/13, Jodhpur Garden, Lake Gardens, Kolkata has been rated 4.0\nBudget for two: 400\n\n3\nThe Bahubelly in 67, Natabar Paul Road, Tikiapara, Kadamtala, Howrah has been rated 4.0\nBudget for two: 400\n\n4\nPizza Hut in Ground Floor, City Centre 2 Mall, Chinar Park, Kolkata has been rated 4.0\nBudget for two: 600\n\n5\nPizza Hut in 20 & 22B, Unimark Riviera, Bhadrakali, Near GT Road Uttarpara, Uttarpara, Kolkata has been rated 4.0\nBudget for two: 600"}
	- utter_ask_want_mail
* emailID{"email_id": "jddk.2jmd@kdl.co.in"}
	- action_mail
	- utter_mailed
	- utter_search_again
* stop
	- utter_goodbye
	
	
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
	- utter_ask_location
* restaurant_search{"location": "mubaim"}
	- slot{"location": "mubaim"}
	- check_location
	- slot{"check_loc": false}
	- utter_enter_city
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
	- check_location
	- slot{"check_loc": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chines"}
	- slot{"cuisine": "chines"}
	- check_cuisine
	- slot{"check_cuis": true}
	- utter_ask_price
* restaurant_search{"price_one": "300", "price_two": "700"}
	- slot{"price_one": "300"}
	- slot {"price_two": "700"}
	- price_category
	- slot{"price_range": "mid"}
	- action_search_restaurants
	- slot{"restaurent_list": "\n\n1\nPizza Hut in 32, 3rd Floor, Avani Riverside Mall, Jagat Banerjee Ghat Road, Shibpur, Howrah has been rated 4.0\nBudget for two: 600\n\n2\nForkstruck in 188/13, Jodhpur Garden, Lake Gardens, Kolkata has been rated 4.0\nBudget for two: 400\n\n3\nThe Bahubelly in 67, Natabar Paul Road, Tikiapara, Kadamtala, Howrah has been rated 4.0\nBudget for two: 400\n\n4\nPizza Hut in Ground Floor, City Centre 2 Mall, Chinar Park, Kolkata has been rated 4.0\nBudget for two: 600\n\n5\nPizza Hut in 20 & 22B, Unimark Riviera, Bhadrakali, Near GT Road Uttarpara, Uttarpara, Kolkata has been rated 4.0\nBudget for two: 600"}
	- utter_ask_want_mail
* emailID{"email_id": "xyz@sth.edu"}
	- action_mail
	- utter_mailed
	- utter_search_again
* stop
	- utter_goodbye