exchange_rates = {
  'USD': 1.13,
  'EUR': 1.15,
  'YEN': 1195.23,
  'AUD': 1.94,
  'CAD': 1.8,
  'CHF': 1.13,
  'HKD': 10.15,
  'NZD':2.15,
  'SGD':1.71,
}
symbols = {
  'USD':"US$",
  'EUR':"€",
  'YEN':'¥',
  'AUD':'AU$',
  'CAD':'CA$',
  'CHF':'₣',
  'HKD':'HK$',
  'NZD':'NZ$',
  'SGD':'S$',

}
def check_currency_exists(initc,finc): # currency before and after exchange
  TF = False if finc not in exchange_rates or initc != 'GBP' else True
  return TF

def validate_amount(amount):
  TF = False if amount > 1000 or amount < 10 else True
  return TF


def currency_convert(newc, amount): # Converts and rounds to new currency
  nam = amount * exchange_rates[newc.upper()] 
  nam = round(nam) if newc.upper() == "YEN" or newc.upper == 'HKD' else round(nam,2)
  return nam





def convertornot(amount, currency):
  x = input("Would you like to convert the price to another currency? (y/n)\n").lower()
  if x.lower() == "y":
      print('\n'.join(exchange_rates.keys()))
      newc = input("What currency would you like to convert into?\n")
      if check_currency_exists(currency,newc) and validate_amount(amount):
          converted = currency_convert(newc,amount)
          return "Great, you now must pay "+ symbols[newc] + str(converted)
      else:
          return "Invalid Conversion, you must pay £" + str(amount)
  else:
      return "Okay, you must pay £ "+ str((amount))

