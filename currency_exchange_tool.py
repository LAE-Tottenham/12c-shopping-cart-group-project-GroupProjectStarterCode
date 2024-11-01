from moneyexchangeapi import exchange_rates
from TONYE1 import currency_convert
def check_currency_exists(currencyvalidity,finalcost):
    a = True
    while a == True:
     currency = input("Choose a desired currency(USD,EUR,CAD,ALL,VND) : ")
     if not currency.isalpha():
         print(" Invalid format ")
     if currency.upper() in exchange_rates:
         currencyvalidity = True
         if currencyvalidity == True:
            new_c = currency
            amount = finalcost
            
            currency_convert(new_c, amount)
            a = False
     else:
         print ("Currency unavailable")