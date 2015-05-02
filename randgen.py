#coding:utf-8

from numpy import *
import os, sys, time,pickle
reload(sys)
sys.setdefaultencoding("utf-8")
import random


def DataRestric(data):
    '''随机正态分布地图尺寸和稀有度'''
    if data == 0:
        data = 1
    elif data > 20:
        data = 20
    else:
        pass
    return data

# def randpick(type,List):
#     '''按Type类型随机出List中的某个数值'''
#     if type == 1:#随机出地形

