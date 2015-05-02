#coding:utf-8

import os, sys, time
reload(sys)
sys.setdefaultencoding("utf-8")
from numpy import *
import operator
import urllib2,re


def clearTestLog():
    file = 'myTest.log'
    if os.path.exists(file):
        os.remove(file)
    else:
        print 'no such file!'

def writeLog0(AI_Name,AI_Feed,AI_Intention):
    with open('myTest.log','a') as myfile:
        myfile.write(str(time.time())+ '\n')
        myfile.write('Name'.ljust(10,'*') + '|' + 'Feed'.ljust(10) + '\t' + 'Intention'.ljust(10) + '\n')
        AI_Name_sorted = sorted(AI_Name.iteritems(), key=operator.itemgetter(0), reverse = False )
        for i in range(len(AI_Name_sorted)):
            key = AI_Name_sorted[i][0]
            if(len(AI_Name[key])==9):
                myfile.write(AI_Name[key].ljust(10,'*') + '|' + str(AI_Feed[key]).ljust(10)\
                             + '\t' + str(AI_Intention[key]).ljust(10) + '\n' )
            else:
                myfile.write(AI_Name[key].ljust(7,'*') + '|' + str(AI_Feed[key]).ljust(10)\
                             + '\t' + str(AI_Intention[key]).ljust(10) + '\n' )

        myfile.write('\n')
    myfile.close()
    return None

def grabName():
    import pickle

    NameLib = {}
    NameLib['Fname'] = {}
    NameLib['Sname'] = {}

    with open('AIname.txt','r') as myfile:
        lines = myfile.readlines()
    myfile.close()

    #获取姓氏
    NameLib['Fname']['P'] = []
    for i in range(0,len(lines[0])-2,2):#读取常用姓氏
        word= lines[0][i:i+2].decode('gbk', 'utf-8')
        NameLib['Fname']['P'].extend(word)

    NameLib['Fname']['D'] = []
    for i in range(0,len(lines[1])-4,4):#读取复姓
        word= lines[1][i:i+4].decode('gbk', 'utf-8')
        NameLib['Fname']['D'].extend(word)

    NameLib['Fname']['R'] = []
    temp = []
    for i in range(0,len(lines[2])-2,2):#读取生僻姓氏
        word= lines[1][i:i+2].decode('gbk', 'utf-8')
        temp.extend(word)
    for word in temp:
        if word not in NameLib['Fname']['P']:
            NameLib['Fname']['R'].extend(word)

    NameLib['Sname']['M'] = []
    NameLib['Sname']['F'] = []
    for i in range(0,7,2):
        if i == 0:
            URL = 'http://www.7mingzi.com/cn-ming-xb-1-zs-2/'
        else:
            URL = 'http://www.7mingzi.com/cn-ming-xb-1-zs-2/'+str(i+1)+'/'

        html = urllib2.urlopen(URL).read()
        reg1 = '<li class=\"ys\">(.*?)</li><li>'
        NameLib['Sname']['M'].extend(re.compile(reg1).findall(html))
        reg2 = '</li><li>(.*?)</li><li class=\"ys\">'
        NameLib['Sname']['M'].extend(re.compile(reg2).findall(html))

    print len(NameLib['Sname']['M'])

    for i in range(0,7,2):
        if i == 0:
            URL = 'http://www.7mingzi.com/cn-ming-xb-2-zs-2/'
        else:
            URL = 'http://www.7mingzi.com/cn-ming-xb-2-zs-2/'+str(i+1)+'/'

        html = urllib2.urlopen(URL).read()
        reg1 = '<li class=\"ys\">(.*?)</li><li>'
        NameLib['Sname']['F'].extend(re.compile(reg1).findall(html))
        reg2 = '</li><li>(.*?)</li><li class=\"ys\">'
        NameLib['Sname']['F'].extend(re.compile(reg2).findall(html))
    print len(NameLib['Sname']['F'])

    namelib = open('NameLib/name.pkl','wb')
    pickle.dump(NameLib,namelib)
    namelib.close()
