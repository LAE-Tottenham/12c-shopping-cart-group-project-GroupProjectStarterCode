import pgeocode
import postcodes_uk
from currency_exchange_tool import check_currency_exists

def postcode_delivery(postcode1, postcode2, total, finalcost):
    currencyvalidity = False
    check = True
    check2 = True
    baserate = 7.5
    
    while check:
        while check2:
            postcode2 = input("Enter postcode for delivery ")
            if " " not in postcode2:
                print("Invalid postcode, separate the two codes with a space.")
            elif " " in postcode2:
                check2 = False
                valid = postcodes_uk.validate(postcode2)
                if not valid:
                    print("Invalid Postcode")
                else:
                    check = False
                    dist = pgeocode.GeoDistance('gb')
                    distance = dist.query_postal_code(postcode1, postcode2)
                    if distance <= 5:
                        baserate += 1
                    elif 5 < distance <= 10:
                        baserate *= 2
                    elif distance > 10:
                        baserate *= 3
                    finalcost = baserate + total
                    print("The total amount to be paid for delivery and products is £" + str(finalcost))
                    convertoption = input("Would you like to convert this into another currency ")
                    if convertoption.lower() == "yes":
                        check_currency_exists(currencyvalidity, finalcost)
    return ""


    

      