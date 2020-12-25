
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
        'consumer_key':'wDnhkTMmnLes8xR56IgJtr3bC',
        'consumer_secret':'WiMqsXmqzOgeDrglzVYCNEqfoqWRToQGEVxZK297dI1PQ4QdDZ',
        'access_token':'1324335665157349377-mqPodJGp8LLYU7vDod2HAHGosqU8mO',
        'access_token_secret':'43fejRpJqJhk33KQE2NBZIGZo4wTggv9jm7e2cG46kMS2',
        }
    return dic

def info_bitflyer():
    dic={
        'api_key':'5pEGBK4QpXNX2mHbPdTwqH',
        'api_secret':'ONloS+6gr1TZ9gPJYtWEbUiijJ+7e9NWiUumNGQHhsM='
        }
    return dic
