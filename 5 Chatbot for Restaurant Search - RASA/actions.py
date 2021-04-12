from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
#import requests
import json


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"00f3caaa14109f849fb591d059237156"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine').lower()
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		d2 = d["restaurants"]
				
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			restaurant_name = []
			restaurant_rating = []
			restaurant_address = []
			restaurant_budget = []
			for x in d2:
				restaurant_name.append(x['restaurant']['name'])
				restaurant_rating.append(x['restaurant']['user_rating']['aggregate_rating'])
				restaurant_address.append(x['restaurant']['location']['address'])
				restaurant_budget.append(x['restaurant']['average_cost_for_two'])
			sorting_list = list(zip(restaurant_name, restaurant_rating, restaurant_address, restaurant_budget))
			sorting_list.sort(key = lambda x:x[1], reverse=True)
			price = tracker.get_slot('price_range')
			sorted_list = []
			for item in sorting_list:
				if price == 'low':
					if int(item[3]) < 300:
						sorted_list.append(item)
				elif price == 'mid':
					if (300 <= int(item[3])) and ( int(item[3]) <= 700):
						sorted_list.append(item)
				else:
					if int(item[3]) >= 700:
						sorted_list.append(item)
			sorted_list = sorted_list[0:5]
			count = 0
			for restaurant in sorted_list:
				count +=1
				response = response + "\n\n" + str(count) + "\n" + restaurant[0] + " in " + restaurant[2] + " has been rated " + restaurant[1] + "\nBudget for two: " + str(restaurant[3])
				
		dispatcher.utter_message(response)
		
		
		for restaurant in sorted_list[0:10]:
				count +=1
				response = response + "\n\n" + str(count) + "\n" + restaurant[0] + " in " + restaurant[2] + " has been rated " + restaurant[1] + "\nBudget for two: " + str(restaurant[3])
				
		#dispatcher.utter_message("-----"+response)
		return [SlotSet('restaurent_list',response)]


class ActionMail(Action):
	
	def name(self):
		return 'action_mail'
	def run(self, dispatcher, tracker, domain):
		
			
		import smtplib
		try:
			from_email ="zomato.upgrad@gmail.com"
			password ="Freedom@1M"
			sent_from ="Zomato "
			server= smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(from_email, password) 
			
			message  = tracker.get_slot('restaurent_list')
			to_email_id = tracker.get_slot('email_id')
			#message = [ str(x)+"."+y for x,y in enumerate (message) ]
			#message = "\n".join(message)
			
			subject ="Zomato Restaurent List requested "
			
			email_text = ("""\
			From: %s
			To: %s
			Subject: %s

			%s
			"""% (sent_from, to_email_id, subject, message))
		
			server.sendmail(sent_from, to_email_id, email_text)
			server.close()
		except:
			dispatcher.utter_message("Sorry Sir Having trouble in sending mail ... working on to fix ")

class CheckLocation(Action):
	def name(self):
		return 'check_location'
	def run(self, dispatcher, tracker, domain):
		loc_var = tracker.get_slot('location')
		with open('data\location.txt') as loc_strings:
			if loc_var.lower() in loc_strings.read().lower():
				return[SlotSet('check_loc', True)]
			else:
				return[SlotSet('check_loc', False)]


class CheckCuisine(Action):
	def name(self):
		return 'check_cuisine'
	def run(self, dispatcher, tracker, domain):
		cuisine_var = tracker.get_slot('cuisine')
		with open('data\cuisines.txt') as cuis_strings:
			if cuisine_var.lower() in cuis_strings.read().lower():
				return[SlotSet('check_cuis', True)]
			else:
				return[SlotSet('check_cuis', False)]


class PriceCategory(Action):
	def name(self):
		return 'price_category'
	def run(self, dispatcher, tracker, domain):
		price_1 = tracker.get_slot('price_one')
		price_2 = tracker.get_slot('price_two')
		price_range = tracker.get_slot('price_range')
		if not (price_range):
			if (price_2):
				price_avg = (float(price_1) + float(price_2)) / 2
			else:
				if (price_1):
					price_avg = float(price_1)
				else:
					return[SlotSet('price_range', 'high')]
			
			if price_avg < 300:
				return[SlotSet('price_range', 'low')]
			elif price_avg <= 700:
				return[SlotSet('price_range', 'mid')]
			else:
				return[SlotSet('price_range', 'high')]
