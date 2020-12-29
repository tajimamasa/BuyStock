
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 #
 #
 #
 #

"""
import datetime
import os
import time

### original library
from BTC_setting import Settings
from BTC_analysis import DataAnalysis
from BTC_bitflyer import bitflyer
from BTC_Util import PrintLog
from BTC_Util import makeTweet

class mainAPP():

    BTCData = DataAnalysis.DataAnalysis()
    BTCbitflyer = bitflyer.bitflyer()

    ### 定時報告用のタイマー
    AppTime = None

    ### 財産
    Assets = {'JPY':3000,'BTC':0,'Con':0}

    ### 買いモード(True) or 売りモード(False)
    AppMode = True

    ### 設定
    RegularReportInterval = Settings.REGULAR_REPORT_INTERVAL_SECOND
    ProjectName =Settings.PROJECT_NAME
    TWEET_SWITCH=False

    def __init__(self):
        ## App 立ち上げ
        self.StartUp()
        while True:
            ### データ取得
            self.BTCbitflyer.renewBTCPrices()

            ### 買いモード
            if self.AppMode:
                self.BuyMode()
            ### 売りモード
            else:
                self.SellMode()
                
            ### 定時報告
            if (time.time()-self.AppTime)>self.RegularReportInterval:
                self.RegularReport()
                 
    
    def StartUp(self):
        ### 時間の取得
        self.AppTime = time.time()
        ### 現在の資金を計算
        assetsText = self.renewAssets()
        ### 状況をコンソールに出力
        text = f'{self.ProjectName} starts.\n' + assetsText
        PrintLog.printlog(text)
        ### 内容をtweet
        makeTweet.Tweet(text,TweetFlag=self.TWEET_SWITCH)

    def BuyMode(self):
        ### 買いの判断
        retval=self.BTCData.JudgeBuy(self.BTCbitflyer.times,self.BTCbitflyer.values)
        if retval:
            ### 注文
            self.AppMode=self.BTCbitflyer.BuyOrder(self.Assets)

    def SellMode(self):
        ### 売りの判断
        retval = self.BTCData.JudgeSell()
        if retval:
            ### 注文
            self.AppMode=self.BTCbitflyer.SellOrder(self.Assets)

    def RegularReport(self):
        ### 時間の更新
        self.AppTime = time.time()
        ### 資金の更新
        assetsText = self.renewAssets()
        ### 状況を更新
        text = f'Regular report\n' + assetsText
        PrintLog.printlog(text)
        ### 内容をtweet
        makeTweet.Tweet(text,TweetFlag=self.TWEET_SWITCH)

    def renewAssets(self):
        ### Bitflyerから資金データの取得
        self.BTCbitflyer.getBTCPriceOnly(self.Assets)
        ### 取得したデータの荷詰め
        yen = self.Assets['JPY']
        btc = self.Assets['BTC']
        BTCValue = self.Assets['Con']
        BTC_YEN = btc*BTCValue
        return f' Now BTC Value {BTCValue} Yen\n Assets: JPY {yen}, BTC {btc}(JPY {BTC_YEN}),\n Total JPY {yen+BTC_YEN}'

    
if __name__=='__main__':
    
    mainAPP()
