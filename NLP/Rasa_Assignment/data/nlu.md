## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- medium
- Yes
- No
- high

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- please find me [chinese](cuisine) restaurant in [delhi](location) within [2000Rs](price)
- please find me [chinese](cuisine) restaurant in [delhi](location) within [2000](price)
- can you find me a [chinese](cuisine) restaurant [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location) within [100Rs](price)
- please show me a few [italian](cuisine) restaurants in [bangalore](location) within [100](price)
- please show me a few [italian](cuisine) restaurants in [bangalore](location) with [100](price)
- search restaurant in [mumbai](location)
- search restaurant
- search restaurant in [mumbai](location) within [200Rs](price)
- search restaurant in [bangalore](location)
- [delhi](location)
- [South Indian](cuisine)

## intent:sending_mail
- yes please note it down, it is [chatbot.upgrad@gmail.com](email_address)
- it is [chatbot.upgrad@gmail.com](email_address)
- yes sure it is [chatbot.upgrad@gmail.com](email_address)
- [chatbot.upgrad@gmail.com](email_address)
- yes please note down it is [chatbot.upgrad@gmail.com](email_address)
- yes please note it down it is [chatbot.upgrad@gmail.com](email_address)
- my gmail address is [chatbot.upgrad@gmail.com](email_address)
- i would like to get the mail to [chatbot.upgrad@gmail.com](email_address)
- [karthik@gmail.com](email_address)
- [logontokarthikk@gmail.com](email_address)
- [logontokarthikk@gmail.com](email_address)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru
- BLR

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
