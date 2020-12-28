
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
import h5py
import numpy as np
### original library
from BTC_setting import Settings
from BTC_analysis import DataAnalysis
from BTC_bitflyer import bitflyer
from BTC_Util import PrintLog
from BTC_Util import makeTweet

class AcquisitionDataMachine():

    ### bitflyer API用のクラス
    BTCbitflyer = bitflyer.bitflyer()
    ### データ取得のインターバル[s]
    WhileInterval = Settings.WHILE_INTERVAL_ACQUISITION
    ### データ長さ
    DataLength = Settings.ACQUISITION_LENGTH
    DataUnit = Settings.ACQUISITION_UNIT
    
    ### H5 ファイルパス
    H5File = Settings.H5FILE_PATH
    ### 保存データ
    SaveDataKey = Settings.SAVE_DATA_KEY
    SaveKeyNum = len(SaveDataKey)-1
    
    def __init__(self):
        ### 保存ユニットの準備
        try_num = 0
        DataBuf = np.zeros((self.DataUnit,len(self.SaveDataKey)-1))
        ### H5 ファイルの初期化
        ofile = h5py.File(self.H5File, 'w')
        timestamp = ofile.create_dataset('timestamp', data=[str(i) for i in range(self.DataLength)])
        value = ofile.create_dataset('value',data=np.zeros((self.DataLength,self.SaveKeyNum)))
        
        while True:
            print(try_num)
            ### データ取得
            price = self.BTCbitflyer.getBTCPrices()
            for i in range(self.SaveKeyNum):
                #DataBuf[try_num,i] = price[self.SaveDataKey[i+1]]
                value[try_num,i] = price[self.SaveDataKey[i+1]]

            ### 保存ユニットに達したら保存
            if try_num == self.DataUnit - 1:
                try_num = 0
            else:
                try_num += 1
            ### インターバル    
            time.sleep(self.WhileInterval)

        ofile.close()
if __name__=='__main__':
    AcquisitionDataMachine()
