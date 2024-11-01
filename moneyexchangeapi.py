import requests
import json
response=requests.get("https://api.currencyapi.com/v3/latest?apikey=cur_live_p8X8M4MgnIReag0L8h41uBOjZueTyJhUfESdMsgE&currencies=EUR%2CUSD%2CCAD%2CALL%2CVND%2CUGX&base_currency=GBP")
exchange_rates={
 "UGX":response.json()["data"]["UGX"]["value"],
 "USD":response.json()["data"]["USD"]["value"],
 "CAD":response.json()["data"]["CAD"]["value"],
 "EUR":response.json()["data"]["EUR"]["value"],
 "ALL":response.json()["data"]["ALL"]["value"],
 "VND":response.json()["data"]["VND"]["value"],
  }