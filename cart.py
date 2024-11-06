import requests
import pyfiglet

#outputs instructions 
def getContactDetails():
    print(pyfiglet.figlet_format("CONTACT DETAILS", font = "straight" ))
    phone_no = int(input(pyfiglet.figlet_format("Enter phone number: ", font = "straight")))
    email = input(pyfiglet.figlet_format("Enter email address: ", font = "straight"))

    return [phone_no,email]

#validating postcode
def validateStatus(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)
    validate = response.json()

    status = validate["status"]

    while status != 200:
        print("Invalid postcode")
        postcode = input("Enter a different postcode: ")
        url = f"https://api.postcodes.io/postcodes/{postcode}"
        response = requests.get(url)
        validate = response.json()
        status = validate["status"]

    return postcode

#stores the address and important information
def get_address():
    canDeliver = True
    validCountries = ["UK","England","Scotland","Wales","Northern Ireland"]
    print(pyfiglet.figlet_format("DELIVERY", font = "straight"))
    print(f"We only deliver to {str(validCountries).replace("'","").replace("[","").replace("]","")}")
    country = input(pyfiglet.figlet_format("Enter Country: ", font = "straight"))
    while country.lower() not in [x.lower() for x in validCountries]:
        print("We do not deliver to your country")
        country = input("Re enter your country (leave blank if no) ")
        if country == "":
            canDeliver = False
            break
    town_city = input(pyfiglet.figlet_format("Enter Town/City: ", font = "straight")) 
    postcode = validateStatus(input(pyfiglet.figlet_format("Enter postcode: ", font = "straight")))
    house_number = input(pyfiglet.figlet_format("Enter house number: ", font = "straight"))
    address = [country,town_city,postcode,house_number]

    return address, canDeliver

#calculate shipping cost depending on distance
def shippingCost(postcode):
    delivery_method = input(pyfiglet.figlet_format("Standard (1) or Next Day (2)", font = "straight"))
    while delivery_method != "1" and delivery_method != "2":
        print("Invalid input")
        delivery_method = input(pyfiglet.figlet_format("Standard (1) or Next Day (2)", font = "straight"))

    url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins=N17%200BX&destinations={postcode}&key=OsI6PtznNFLu0fE0C14Uw5vgB0XF5s4hoTdlfzsGM5WKMx0lKfNkLLtMWMG9FZJb"
    response = requests.get(url)
    distance = response.json()

    if postcode.lower() == "n170bx" or postcode.lower() == "n17 0bx":
        delivery_price = 1
    elif delivery_method == "1":
        delivery_price = distance["rows"][0]["elements"][0]["distance"]["value"] / 1000
    elif delivery_method == "2":
        delivery_price = distance["rows"][0]["elements"][0]["distance"]["value"] / 500

    return round(delivery_price,2)

def payment_method():
    payment_method = input(pyfiglet.figlet_format("Would you like to pay with Visa or mastercard? ", font = "straight"))
    card_no = input(pyfiglet.figlet_format("Card number: ", font = "straight"))
    expiry_date = input(pyfiglet.figlet_format("Enter expiry date in the format MM/YY: ", font = "straight"))
    name = input(pyfiglet.figlet_format("Enter name: ", font = "straight"))
    cvv = input(pyfiglet.figlet_format("Enter cvv: ", font = "straight"))

    return [payment_method,card_no,expiry_date,name,cvv]
    
