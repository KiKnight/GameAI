#coding:utf-8

from numpy import *
import os, sys, time,pickle
reload(sys)
sys.setdefaultencoding("utf-8")
import random


def DataRestric(data):
    if data == 0:
        data = 1
    elif data > 20:
        data = 20
    else:
        pass
    return data
