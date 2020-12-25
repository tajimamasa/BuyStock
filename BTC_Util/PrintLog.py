
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 # テキストをコンソールに出力するともに、
 # 内容を日付のログファイル記録します
 #
 #

"""
import datetime
from BTC_setting import Settings

def printlog(text):
    ### テキストに時間情報を付随させます
    dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S ')
    print(dt_now+'\n'+text)   
    
    ## 内容をテキストファイルに記録
    logtext = Settings.LOG_DIR + \
      datetime.datetime.now().strftime('%Y%m%d.txt')
    try:
        with open(logtext, "a") as f:
            f.write(dt_now +'\n'+ text + "\n")
    except:
        print(dt_now + '-Worning- Log cannot be written!!!')

if __name__=='__main__':
    pass
    
