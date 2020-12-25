
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 #
 #
 #
 #

"""

PROJECT_NAME = 'BTC-BYRM'
### Path
LOG_DIR = './BTC_log/'

### Value
WHILE_INTERVAL_SECOND = 10
REGULAR_REPORT_INTERVAL_SECOND = 10#3600/2
BUY_YEN = 1000

def info_tweepy():
    dic={
        'consumer_key':'',
        'consumer_secret':'',
        'access_token':'',
        'access_token_secret':'',
        }
    return dic

def info_bitflyer():
    dic={
        'api_key':'',
        'api_secret':''
        }
    return dic
