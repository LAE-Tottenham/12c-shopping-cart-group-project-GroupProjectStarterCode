from moneyexchangeapi import exchange_rates

def currency_convert(new_c, amount):
    if 10<=amount<=1000:
       conversion_rate=exchange_rates.get(new_c)
       total=amount*conversion_rate
       total=round(total,2)
       print("The total is",total,new_c)
    else:
        print("You can only convert between £10 and £1000")
