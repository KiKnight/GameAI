#coding:utf-8

import os, sys, time ,random
reload(sys)
sys.setdefaultencoding("utf-8")
from numpy import *
import start, events, mysys


Map = start.MapCreate()


AI = start.AICreate()
AI2 = start.SubGen(Map,AI)


mysys.clearTestLog()#清除测试log，保证观测

mysys.writeLog0(AI['Name'],AI['Feed'],AI['Intention'])

testcnt = 10
#while(len(AI['Name'])>0):
while(testcnt>0):

    testcnt -= 1

    #time.sleep(1)

    deadAIkey = events.FeedUpdate(AI['Feed'],AI['Intention'])

    events.removeDeadAI(AI['Name'],AI['Feed'],AI['Intention'],deadAIkey)

    mysys.writeLog0(AI['Name'],AI['Feed'],AI['Intention'])

















