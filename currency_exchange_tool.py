import requests

url = 'https://v6.exchangerate-api.com/v6/4f44f393d74dad8d1f909c22/latest/GBP'
response = requests.get(url)
exchange_rates = response.json()
clean_exchange_rates = exchange_rates["conversion_rates"]

def check_currency_exists(currency):
    if currency in clean_exchange_rates:
        return True
    else:
        return False 

def currency_convert(original_c, new_c, amount):
    if check_currency_exists(new_c) and original_c == "GBP":
          amount *= round(clean_exchange_rates[new_c],2)
          return amount 
    elif not check_currency_exists(new_c):
        return ("currency not avalible in store")
    elif original_c != "GBP":
        return ("cannot convert from that currency")  
         


