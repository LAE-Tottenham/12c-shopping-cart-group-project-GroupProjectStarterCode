from pyfiglet import Figlet

# Initialize Figlet with a slant font style for text formatting
f = Figlet(font='slant')
# Define available items with their prices
items = {
    'Bread': 6.20,
    'Milk': 6.15,
    'Apples': 5.50,
    'Eggs': 6.25,
    'Rice': 6.00,
    'Biscuits': 5.70,
    "Bananas": 6.60,
    "Juice": 6.00,
    "Water": 5.70,
    "Steak": 6.95,
}
# Lists to store selected items and their prices
basket = []
basketprice = []

def start_shop():
    while True:  
        totalcost = 0.0 
        # Prompt user for item selection
        choices = input(f.renderText("What you would like to buy?")).capitalize()
        # Check if item is available
        if choices in items:
            basket.append(choices) 
            basketprice.append(items.get(choices))
            print(basket)
            print(basketprice)
        else:
            print(f.renderText("We don't have that"))  
            # Prompt for re-entry if item was not found
            choices = input(f.renderText("Try again: ")).capitalize()
            if choices in items:
                basket.append(choices) 
                basketprice.append(items.get(choices))
                print(basket)
                print(basketprice)
        # Ask if the user wants to add more items
        extra = input(f.renderText("Would you like anything else?: ")).capitalize()
        
        while extra == "Yes":
            choices = input(f.renderText("What you would like to buy?")).capitalize()
            
            if choices in items:
                basket.append(choices)
                basketprice.append(items.get(choices))
                print(basket)
                print(basketprice)
            else:
                print(f.renderText("we don't have that"))
                choices = input(f.renderText("try again")).capitalize()
            
            extra = input(f.renderText("Would you like anything else?: ")).capitalize()
        
        # Calculate and display the total cost of items in the basket
        totalcost = round(sum(basketprice), 2)
        print(f.renderText("Your total cost is £" + str(totalcost)))
        print(f.renderText(str(basket)))
        
        return totalcost
