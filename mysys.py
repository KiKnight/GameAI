#coding:utf-8

import os, sys, time
from numpy import *
import operator

def clearTestLog():
    file = 'myTest.log'
    if os.path.exists(file):
        os.remove(file)
    else:
        print 'no such file!'

def writeLog0(AI_Name,AI_Feed,AI_Intention):
    with open('myTest.log','a') as myfile:
        myfile.write(str(time.time())+ '\n')
        myfile.write('Name'.ljust(10) + '|' + 'Feed'.ljust(10) + '|' + 'Intention'.ljust(10) + '\n')
        AI_Feed_sorted = sorted(AI_Feed.iteritems(), key=operator.itemgetter(0), reverse = False )
        for i in range(len(AI_Feed_sorted)):
            key = AI_Feed_sorted[i][0]
        # for key in AI_Feed:
            myfile.write(str(AI_Name[key]).ljust(10) + '|' + str(AI_Feed[key]).ljust(10)\
                         + '|' + str(AI_Intention[key]).ljust(10) + '\n' )
        myfile.write('\n')
    myfile.close()
    return None
