
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

class DataAnalysis():

    def __init__(self):
        pass

    def JudgeBuy(self):
        confidence = random.random()
        if confidence < 0.1:
            return True
        else:
            return False

    def JudgeSell(self):

        confidence = random.random()
        if confidence < 0.1:
            return True
        else:
            return False






