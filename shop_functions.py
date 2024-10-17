from pyfiglet import Figlet
f = Figlet(font='slant')
items = {
  'Bread': 6.20,
   'Milk': 6.15,
  'Apples': 5.50,
  'Eggs':6.25,
  'Rice': 6.00,
  'Biscuits':5.70,
  "Bananas":6.60,
  "Juice":6.00,
  "Water":5.70,
  "Steak":6.95,
}
basket=[]
basketprice=[]

def start_shop():
    while True:  
      totalcost=0.0
      choices=input(f.renderText("What you would like to buy?"))
      choices=choices.capitalize()
      if choices in items:
          basket.append(choices) 
          basketprice.append(items.get(choices))
      else:
          print(f.renderText("We don't have that"))
          choices=input(f.renderText("Try again: "))
          choices=choices.capitalize()
          if choices in items:
            basket.append(choices) 
            basketprice.append(items.get(choices))
            print(basket)
            print(basketprice)
      extra=input(f.renderText("Would you like anything else?: "))
      extra=extra.capitalize()
      while extra=="Yes":
            choices=input(f.renderText("What you would like to buy?"))
            choices=choices.capitalize()
            if choices in items:
                basket.append(choices)
                basketprice.append(items.get(choices))
                print(basket)
                print(basketprice)
            else:
                print(f.renderText("we dont have that"))
                choices=input(f.renderText("try again"))
                choices=choices.capitalize()
            extra=input(f.renderText("Would you like anything else?: "))
            extra=extra.capitalize()
      totalcost= round(sum(basketprice),2)
      print(f.renderText("Your total cost is £"+str(totalcost)))
      print(f.renderText(str(basket)))
      return totalcost

   
          
          
          
          
          
          
      
      
    
   


    
