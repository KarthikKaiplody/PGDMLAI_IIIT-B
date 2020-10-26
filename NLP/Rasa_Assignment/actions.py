from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

from email.message import EmailMessage
import smtplib

d_email_rest = []

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"a6b506bef65f43bcf7b9f9750e9fc175"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		global d_email_rest
		d_email_rest = response
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class VerifyLocation(Action):
	Tier1 = []
	Tier2 = []

	def __init__(self):
		self.Tier1 = ['ahmedabad', 'bangalore', 'chennai', 'delhi',
		 'hyderabad', 'kolkata', 'mumbai', 'pune']
		self.Tier2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 
					   'amritsar', 'asansol', 'aurangabad', 'bareilly', 
					   'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 
					   'bhubaneswar', 'bikaner', 'bokaro steel city', 
					   'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 
					   'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 
					   'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 
					   'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 
					   'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 
					   'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur', 
					   'kanpur', 'kakinada', 'kochi','kottayam', 'kolhapur', 'kollam', 
					   'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana', 'madurai', 
					   'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 
					   'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 
					   'patna', 'pondicherry', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 
					   'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 
					   'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 
					   'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 
					   'vasai-virar city', 'vijayawada', 'visakhapatnam', 'warangal'] 

	def name(self):
		return 'verify_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		if not (self.check_location(location)):
			dispatcher.utter_message(f"We do not operate in {location} yet.")
			return [SlotSet('location', None), SlotSet('check_op', False)]
		else:
			return [SlotSet('location', location), SlotSet('check_op', True)]	

	def check_location(self, location):
		if location:
			return location.lower() in self.Tier1 or location.lower() in self.Tier2	

class VerifyCuisine(Action):
	def name(self):
		return 'verify_cuisine'

	def run(self, dispatcher, tracker, domain):
		cuisines = ['chinese','mexican','italian','american','south indian','north indian']
		error_msg = "Sorry! specified cuisine is not available. Please re-enter"
		cuisine = tracker.get_slot('cuisine')
		
		if cuisine in cuisines:
			return [SlotSet('cuisine', cuisine), SlotSet('cuisine_check',True)]
		else:
			dispatcher.utter_message(error_msg)
			return [SlotSet('cuisine', None), SlotSet('cuisine_check', False)]	

class VerifyBudget(Action):
	def name(self):
		return 'verify_budget'

	def run(self, dispatcher, tracker, domain):
		error_msg = "Sorry!! please enter a budget withing the specified range"
		_price = tracker.get_slot('price')
		price = int(_price.split('Rs')[0])
		if (price > 0) and (price <= 300):
			return [SlotSet('price', price),SlotSet('budget', 'low'), SlotSet('budget_check', True)]
		elif (price > 300) and (price <=700):
			return [SlotSet('price', price),SlotSet('budget', 'mid'), SlotSet('budget_check', True)]
		elif (price > 700) and (price <=10000):
			return [SlotSet('price', price),SlotSet('budget', 'high'), SlotSet('budget_check', True)]
		else:
			dispatcher.utter_message(error_msg)
			return [SlotSet('price', None), SlotSet('budget_check', False)]

class SendEmail(Action):
	def name(self):
		return 'send_email'

	def run(self, dispatcher, tracker, domain):
		# Get user's email id
		to_email = tracker.get_slot('email_address')

        # Get location and cuisines to put in the email
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		d_email_subj = "Top 5 Restaurants in"+ loc + "of" + cuisine
		global d_email_rest
		email_rest_list = [i for i in d_email_rest.split("Found")]
		# Construct the email 'subject' and the contents.
		d_email_msg = "Hi there! Here are the Restaurants you are looking for" +"\n"
		for restaurant in email_rest_list:
			d_email_msg = d_email_msg + restaurant

		# Open SMTP connection to our email id.
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login("chatbot.upgrad2020@gmail.com", "upgrad2020")

		# Create the msg object
		msg = EmailMessage()

		# Fill in the message properties
		msg['Subject'] = d_email_subj
		msg['From'] = "chatbot.upgrad2020@gmail.com"

		# Fill in the message content
		msg.set_content(d_email_msg)
		msg['To'] = to_email

		s.send_message(msg)
		s.quit()
		dispatcher.utter_message("Email Sent Successfully! Visit again")
		return []	

	