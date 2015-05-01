#coding:utf-8

#姓名：随机从姓名库里选一
#性别：随机从男女中选一
#年龄：随机从0~100中选一+时间增添
#关系：初始+事件增添
#职业：随机从职业中选N：等级选N
#归属：随机从国家、组织选1：地位选1
#属性：力敏智：0~20选，10为正常人，事件增添
#技能：初始+事件增添
#物品：初始+事件增添
#位置：城池及建筑位置
#状态：事件触发


from numpy import *
import random
import randgen

def AICreate():
    '''生成AI初始属性：姓名，饥饱度，想法'''
    #AIcnt = random.randint(1,100)
    AIcnt = 20
    AI = {}
    Name, Feed, Intention = {},{},{}
    for i in range(AIcnt):
        key = 'AI' + str(i).zfill(3)
        Name[key]       = key
        Feed[key]       = random.randint(50,100)
        Intention[key]  = random.choice(['睡觉','走路','交谈','吃饭','学习','玩'])
    AI['Name'] = Name
    AI['Feed'] = Feed
    AI['Intention'] = Intention
    return AI

def MapCreat():
    '''生成地图初始属性：地名，大小，稀有度'''
    Mapcnt = 20
    Map = {}
    Name, Scale, Rare, Build, Belong = {},{},{},{},{}
    for i in range(Mapcnt):
        key = 'MAP' + str(i).zfill(3)
        #Name[key]     = key
        Scale[key]    = int(abs(random.normalvariate(0,1))*10)
        Scale[key] = randgen.DataRestric(Scale[key])
        Rare[key] = int(abs(random.normalvariate(0,1))*10)
        Rare[key] = randgen.DataRestric(Rare[key])
        Build[key]    = 0
        Belong[key]   = 0
    #Map['Name'] = Name
    Map['Feed'] = Scale
    Map['Intention'] = Rare
    for key in Map:
        print Map[key]
    #return Map




















