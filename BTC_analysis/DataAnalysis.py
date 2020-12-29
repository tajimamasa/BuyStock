
# -*- coding:utf-8 -*-
"""
Created in 20XX/XX/XX
@atthor : tajimamasa

 #
 #
 #
 #

"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt

from BTC_setting import Settings
from BTC_Util import PrintLog

class DataAnalysis():

    def __init__(self):
        pass

    def JudgeBuy(self,time,value):
        value = np.where(value<1e-6,None,value)

        plt.plot(value[:,0])
        plt.plot(value[:,1])
        plt.show()
        
        confidence = random.random()
        if confidence < 0.1:
            PrintLog.printlog('Buy!!!')
            return True
        else:
            return False

    def JudgeSell(self):

        confidence = random.random()
        if confidence < 0.1:
            return True
        else:
            return False






