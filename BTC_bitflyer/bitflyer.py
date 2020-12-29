

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
import time
import numpy as np

from BTC_setting import Settings
from BTC_Util import PrintLog

class bitflyer():
    ### set API
    APIdic = Settings.info_bitflyer()
    api = pybitflyer.API(api_key=APIdic['api_key'],
                         api_secret=APIdic['api_secret'])

    ### データ取得のインターバル[s]
    AcquisitionInterval = Settings.WHILE_INTERVAL_ACQUISITION
    ### データ長さ
    DataLength = Settings.ACQUISITION_LENGTH
    ### データ取得の単位長
    UnitLength = Settings.ACQUISITION_UNIT
    ### 保存データ
    SaveDataKey = Settings.SAVE_DATA_KEY
    SaveKeyNum = len(SaveDataKey)-1
    times = [str(i) for i in range(DataLength)]
    values = np.zeros((DataLength,SaveKeyNum))
    try_times = 0
    
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

    ### 配列に価格を保存
    def renewBTCPrices(self):
        for i in range(self.UnitLength):
            # print(f'try times: {self.try_times}')
            ### インターバル    
            time.sleep(self.AcquisitionInterval)
            ### データ取得
            price = self.getBTCPrices()
            ### タイムスタンプ
            self.times[self.try_times] = price[self.SaveDataKey[0]]
            ### 価格データの取得
            for i in range(self.SaveKeyNum):
                self.values[self.try_times,i] = price[self.SaveDataKey[i+1]]
            ### 保存ユニットに達したら保存
            if self.try_times == (self.DataLength - 1):
                self.try_times = 0
            else:
                self.try_times += 1

        
