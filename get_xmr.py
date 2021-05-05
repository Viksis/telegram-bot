import cryptocompare
import requests
import json
import auth_data
from auth_data import currency

def getPrice():
    #currency = input('what currency you want to use (enter input like RUB or USD in caps): ')
    currency = ''
    cryptocurrency = ''
    from auth_data import currency
    a = cryptocompare.get_price('BTC', currency=currency, full=False)
    btc_json = json.dumps(a, indent = 4)  
    y = json.loads(btc_json)
    sell_price = y["BTC"][currency]
    print("Bitcoin price is " + str(sell_price) + " " + currency)
    output = str(sell_price)
    currency = ''
    return output