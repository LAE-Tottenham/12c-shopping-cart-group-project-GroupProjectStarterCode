import requests #This is for API interfacing
import math #Pretty sure this was kept for if we ever needed it, not sure we ever did.

url = 'https://v6.exchangerate-api.com/v6/9539da403e1974365970d782/latest/GBP' #Exchange Rates API domain and API Key

response = requests.get(url) #Pulls data from the Exchange Rates API in the form of a massive Dict.
data = response.json() #Actual stored Dict.

def check_currency_exists(initc,finc): #Currency before and after exchange - Main design Nikhil, Final streamline/tweaks Archie
    TF = False if finc not in data["conversion_rates"] or initc != 'GBP' else True # ["Conversion"] is a subdict which houses the currency names as strings, the Dict is refreshed every 12 hours
    return TF

def validate_amount(amount): #Checks that the data is within a certain range - Main design Nikhil, Final streamline/tweaks Archie
    TF = False if float(amount) > 1000 or float(amount) < 10 else True
    return TF
    
def currency_convert(newc, amount): #Converts and rounds to new currency using conversion rate (also rounds) - Main design and streamline/tweaks Archie
    conver = data["conversion_rates"][newc] #Uses the chosen curreny to navigate the subdict and find the conversion rate.
    nam = float(amount) * float(conver) 
    nam = round(nam) if newc.upper() == "JPY" else round(nam,2)
    return nam

def convertornot(amount, currency): #Takes Currency input and then calls upon previous functions to convert to new currency, returns final value as string to be printed - Mainly designed by Nikhil tweaked slightly for API integration by Archie
    x = input("Would you like to convert the price to another currency? (y/n)").lower()
    if x.lower() == "y":    
        newc = input("What ISO 4217 currency would you like to convert into? ").upper()
        if check_currency_exists(currency,newc) and validate_amount(amount):
            converted = currency_convert(newc,amount)
            return "Great, you now must pay "+ str(newc) + " " + str(converted)
        else:
            return "Invalid Conversion, you must pay GBP £" + str(amount)
    else:
        return "Okay, you must pay GBP £ "+ str((amount))
