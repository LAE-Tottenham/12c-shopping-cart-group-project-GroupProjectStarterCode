import currency_exchange_tool 
import deliveryprice
import shop_functions 

cost = shop_functions.start_shop()
costandship = deliveryprice.deliveryprice(cost)
print(currency_exchange_tool.convertornot(costandship,"GBP"))
