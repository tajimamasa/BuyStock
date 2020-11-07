
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

### my library
from makeTweet import tweet
from bitflyer import getTotalAssets

class mainAPP():
    logdir = './log/'
    project = 'BuyStock'
    def __init__(self):
        self.PrintLog(f'[mainAPP] {self.project} starts.')
        assets = getTotalAssets()
        self.Tweet(f'{self.project} starts.\n' + assets)

        while True:
            time.sleep(100)
            assets = getTotalAssets()
            self.Tweet('[Regular report]\n' + assets)
        
    def Tweet(self,text,debug=0):
        dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        retText = tweet(f'[{dt_now}] {text}')
        self.PrintLog(retText)
        
    def PrintLog(self,text):
        ## print console
        dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S ')
        print(dt_now+text)
        ## write log
        logtext = self.logdir + \
          datetime.datetime.now().strftime('%Y%m%d.txt')
        try:
            with open(logtext, "a") as f:
                f.write(dt_now + text + "\n")
        except:
            print(dt_now + '[mainAPP] -Worning- Log cannot be written!!!')
            os.mkdir(self.logdir)

if __name__=='__main__':
    
    mainAPP()
