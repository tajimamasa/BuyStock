
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

from BTC_setting import Settings
from BTC_Util import PrintLog

class bitflyer():
    ### set API
    APIdic = Settings.info_bitflyer()
    api = pybitflyer.API(api_key=APIdic['api_key'],
                         api_secret=APIdic['api_secret'])
    
    def __init__(self):
        pass
    
    def BuyOrder(self,Assets):
        self.getBTCPriceOnly(Assets)
        Assets['JPY'] -= Settings.BUY_YEN
        Assets['BTC'] += Settings.BUY_YEN / Assets['Con']
        return False
                
    def SellOrder(self,Assets):
        self.getBTCPriceOnly(Assets)
        BTC = Assets['BTC']
        Assets['JPY'] += int(BTC * Assets['Con'])
        Assets['BTC'] = 0
        return True
    

    def getBTCPriceOnly(self,Assets):
        try:
            price = self.api.ticker(product_code="BTC_JPY")
        except:
            PrintLog('Error: Bitflyer API dosen\'t  work.')
        else:
            Assets['Con'] = price['best_ask']


    ''''
    ### get assets
    try:
        balances = api.getbalance(product_code="BTC_JPY")

    except:
        return '[pybitflyer:getTotalAssets] '

    ### en & BTC
    jap = balances[0]
    btc = balances[1]

    text = f"{jap['currency_code']} : ¥{jap['amount']:.0f},  {btc['currency_code']} : {btc['amount']:f} (¥{btc['amount'] *price['best_ask']:.0f})\n"
    text = text + f"total : ¥{jap['amount']+btc['amount'] *:.0f}"
    return text



if __name__=='__main__':
    text = getTotalAssets()
    print(text) 
'''
