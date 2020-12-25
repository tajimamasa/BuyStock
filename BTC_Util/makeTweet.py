
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 # テキストデータをツイートします
 # API Keyに関する情報はSettingsを参します
 #
 #

"""

import tweepy
import os

from BTC_setting import Settings
from BTC_Util import PrintLog

def Tweet(text,image_ifile=None,TweetFlag=False):

    ### Get API Data
    dic = Settings.info_tweepy()
    CK = dic['consumer_key']
    CS = dic['consumer_secret']
    AT = dic['access_token']
    AS = dic['access_token_secret']

    ### API接続の準備
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    ### Tweetが必要ないときはここで終了します
    if not (TweetFlag):
        PrintLog.printlog('Not Tweet for debug')
        return
        
    ### Tweeterに接続及び& Tweet        
    try:
        if image_ifile == None:
            api.update_status(text)
        else:
            api.update_with_media(status = text, filename =image_ifile)
    except:
        retText = '-Warning - tweepy API connction cannot be built.'
        PrintLog.printlog(retText)
        return
    ### Tweetしたことを記録します
    ## retText = 'Tweet' if (image_ifile==None) else 'Tweet with: ' + image_ifile
    ## PrintLog.printlog(retText)

if __name__=='__main__':
    
    pass
