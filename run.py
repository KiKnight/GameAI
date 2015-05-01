#coding:utf-8

import os, sys, time ,random
reload(sys)
sys.setdefaultencoding("utf-8")
from numpy import *
import start, events, mysys

AI = start.AICreate()
Map = start.MapCreat()

mysys.clearTestLog()#清除测试log，保证观测

mysys.writeLog0(AI['Name'],AI['Feed'],AI['Intention'])

while(len(AI['Name'])>0):

    #time.sleep(1)

    deadAIkey = events.FeedUpdate(AI['Feed'],AI['Intention'])

    events.removeDeadAI(AI['Name'],AI['Feed'],AI['Intention'],deadAIkey)

    mysys.writeLog0(AI['Name'],AI['Feed'],AI['Intention'])

















