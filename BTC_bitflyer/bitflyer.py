

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

    ### 買い注文
    def BuyOrder(self,Assets):
        self.getBTCPriceOnly(Assets)
        Assets['JPY'] -= Settings.BUY_YEN
        Assets['BTC'] += Settings.BUY_YEN / Assets['Con']
        return False

    ### 売り注文
    def SellOrder(self,Assets):
        self.getBTCPriceOnly(Assets)
        BTC = Assets['BTC']
        Assets['JPY'] += int(BTC * Assets['Con'])
        Assets['BTC'] = 0
        return True
    
    ### BTC の価格の取得
    def getBTCPriceOnly(self,Assets):
        try:
            price = self.api.ticker(product_code="BTC_JPY")
        except:
            PrintLog.printlog('Error: Bitflyer API dosen\'t  work.')
        else:
            Assets['Con'] = price['ltp']

    ### BTCの板の取得
    def getBTCBoard(self):
        try:
            board = self.api.board(product_code="BTC_JPY")
        except:
            PrintLog.printlog('Error: Bitflyer API dosen\'t  work.')
            
    def getBTCBalance(self):
        try:
            balances = self.api.getbalance(product_code="BTC_JPY")
            #print(balances)
            #jap = balances[0]
            #btc = balances[1]
        except:
            PrintLog.printlog('Error: Bitflyer API dosen\'t  work.')

    def getBTCPrices(self):
        try:
            price = self.api.ticker(product_code="BTC_JPY")
        except:
            PrintLog.printlog('Error: Bitflyer API dosen\'t  work.')
        else:
            return price
