from TONYE1 import currency_convert
from postcode import postcode_delivery
from currency_exchange_tool import check_currency_exists
items = {
    "Bread": 1.20,
    'Milk': 1.15,
    'Chocolate':1.50,
    "Eggs" : 1.60,
    "Chicken" : 2.50,
    "Broccoli" :1.20,
    "Apple" : 1.75,
    "Cheese" : 1.80,
    "Sweets" : 1.70,
    "Crisps" : 1.50
}   
from pyfiglet import Figlet
shopname = Figlet(font='slant')
print(shopname.renderText('Shop'))
total = 0
deliverytext = Figlet(font='slant')
product_cost_arr = []
def start_shop():
        finalcost = 0
        postcode1= "N17 0BX"
        postcode2=""
        print("What you would like to buy from the shop? ")
        print("\n".join("{}\t{}".format(k, v) for k, v in items.items()))
        print("(All prices in GBP)")
        a = True
        while True: 
         product = input()
         if product in items:
           total = product_cost_arr.append(items.get(product))
           print("Checkout or continue (leave blank for continue) ")
           checkout = input()
           while a == True:
            if checkout.lower() == "continue" or checkout == "":
                product = input("What else would you like ")
                total = items.get(product)
                product_cost_arr.append(total)
                print("Checkout or continue (leave blank for continue) ")
                checkout = input()
            if checkout.lower() == "checkout":
                   a = False
                   total = sum(product_cost_arr)
                   total = round(total,2)
                   print("The total cost of these products is £"+str(total))  
                   postcode_delivery(postcode1,postcode2,total,finalcost)     
         else:
            print("We do not sell this.")
            print("What you would like to buy from the shop? ")                  
start_shop()
