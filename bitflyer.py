
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 #
 #
 #
 #

"""
import pybitflyer
from personalData import info_bit

def getTotalAssets():

    ### set API
    dic = info_bit()
    api = pybitflyer.API(api_key=dic['api_key'], api_secret=dic['api_secret'])

    ### get assets
    try:
        balances = api.getbalance(product_code="BTC_JPY")
        price = api.ticker(product_code="BTC_JPY")
    except:
        return '[pybitflyer:getTotalAssets] Error:API dosen\'t  work.'

    ### en & BTC
    jap = balances[0]
    btc = balances[1]

    text = f"{jap['currency_code']} : ¥{jap['amount']:.0f},  {btc['currency_code']} : {btc['amount']:f} (¥{btc['amount'] *price['best_ask']:.0f})\n"
    text = text + f"total : ¥{jap['amount']+btc['amount'] *price['best_ask']:.0f}"
    return text

if __name__=='__main__':
    text = getTotalAssets()
    print(text) 
