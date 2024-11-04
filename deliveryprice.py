from geopy.geocoders import Nominatim
from geopy import distance
from ukpostcodeutils import validation
# Initialize the Nominatim geocoder with a user agent name
geocoder = Nominatim(user_agent="Geocoder")
# Define a fixed location (postcode) to calculate distances from
location1 = "N170BX"

def deliveryprice(cost):
    shipping_price = 0
    postcode = input("Enter your post code ")
    postcode = (postcode.replace(" ", "")).upper()
    # Validate entered postcode
    if validation.is_valid_postcode(postcode):
        print("Postcode OK.")
        location2 = postcode
        coordinates1 = geocoder.geocode(location1)
        coordinates2 = geocoder.geocode(location2)
        print(coordinates2)
        # Extract latitude and longitude for both locations
        lat1, long1 = (coordinates1.latitude), (coordinates1.longitude)
        lat2, long2 = (coordinates2.latitude), (coordinates2.longitude)
        # Calculate distance between the two locations
        place1 = (lat1, long1)
        place2 = (lat2, long2)
        distancefromlaet = distance.distance(place1, place2)
        # Determine shipping price based on distance
        if distancefromlaet < 20:
            shipping_price = 8.00
        elif distancefromlaet >= 20:
            shipping_price = 13.00
        elif distancefromlaet >= 40:
            shipping_price = 20.00
        # Offer same-day delivery option for an additional charge
        sameday = input("Would you like to have same day delivery for +£10.00?").capitalize()
        if sameday == "Yes":
            shipping_price += 10.00
        print("Your shipping price is ", shipping_price)
        return (shipping_price+cost)
    else:
        print("This postcode doesn't exist")
