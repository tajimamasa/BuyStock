
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 #
 #
 #
 #

"""

import tweepy
import os
import datetime

from personalData import info_tweepy

def tweet(text,image_ifile=None):

    ### Get API Data
    dic = info_tweepy()

    CK = dic['consumer_key']
    CS = dic['consumer_secret']
    AT = dic['access_token']
    AS = dic['access_token_secret']

    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)

    ### Connet tweeter & Tweet
    try:
        if image_ifile == None:
            api.update_status(text)
        else:
            api.update_with_media(status = text, filename =image_ifile)
    except:
        return '[tweepy] API connction cannot be built.'

    buf = '[tweepy] Tweet: =\n' + text
    if image_ifile != None:
        buf = '\n' + 'with: ' + image_ifile
    return buf
        
if __name__=='__main__':
    
    pass
