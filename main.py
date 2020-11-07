
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

### my library
from makeTweet import tweet

class mainAPP():
    logdir = './log/'
    
    def __init__(self):
        self.PrintLog('[mainAPP] BuyStock starts.')
        #self.Tweet('BuyStock starts.')
        
    def Tweet(self,text,debug=0):
        retText = tweet(text)
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
