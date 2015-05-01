#coding:utf-8

from numpy import *

def FeedUpdate(AI_Feed,AI_Intention):
    deadAIkey = []

    for key in AI_Feed:
        AI_Feed[key] -= 10
        if AI_Feed[key] < 50:
            if AI_Feed[key] > 0:
                AI_Intention[key] = '吃饭'
            else:
                AI_Feed[key] = 0
                deadAIkey.append(key)
        else:
            pass
    return deadAIkey

def removeDeadAI(AI_Name,AI_Feed,AI_Intention,deadAIkey):
    for key in deadAIkey:
        del AI_Name[key],AI_Feed[key],AI_Intention[key]
    return None

