import pyfiglet as pfg 
from currency_exchange_tool import *  
from shop_functions import start_shop
from account import *
from cart import *

# login_or_create = input("would you like to login, say (yes) for login, or (no) for creating a acoount")
# if login_or_create.lower() == "yes" or "y":
#    login_account()
# else:
#    create_account()

print(pfg.figlet_format("shopping list",font="larry3d"))


print('Please select what you would like to buy\n')
items_to_buy = start_shop()

print("")
address, canDeliver = get_address()

if canDeliver:
    shippingCost = shippingCost(address[2])

    print(f"\nYour shipping cost is £{"{:.2f}".format(shippingCost)}")

    total = round(items_to_buy["total_cost"] + shippingCost,2)
    print(f"\nYour total is £{"{:.2f}".format(total)}\n")

    contactDetails = getContactDetails()

    print("")
    paymentMethod = payment_method()

    if total < 1000 or total > 10:
        change_currency = input("\nWould you like to switch currencies from GBP? (Yes or No) ")
        if change_currency.lower() == "yes":
            currency = input("Enter the new currency that you would like to change to (ISO 4217): ").upper()
            while not check_currency_exists(currency):
                print("We don't convert to that currency")
                currency = input("Enter a new currency (leave blank to stop): ").upper()
                if currency == "":
                    break
            if currency != "":
                print(f"You will have to pay {"{:.2f}".format(currency_convert("GBP", currency, total))} {currency}")
            else:
                 print(f"You will have to pay £{total}")
else:
    print("Your order will be cancelled")