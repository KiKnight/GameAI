#coding:utf-8

import os, sys, time ,random
from numpy import *
import start, events, mysys

AI_Name,AI_Feed,AI_Intention = start.AICreate()

mysys.clearTestLog()#清除测试log，保证观测

mysys.writeLog(AI_Name,AI_Feed,AI_Intention)

while(len(AI_Name)>0):

    #time.sleep(1)

    deadAIkey = events.FeedUpdate(AI_Feed,AI_Intention)

    events.removeDeadAI(AI_Name,AI_Feed,AI_Intention,deadAIkey)

    mysys.writeLog(AI_Name,AI_Feed,AI_Intention)

















