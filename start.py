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
import os, sys, time,pickle
reload(sys)
sys.setdefaultencoding("utf-8")
import random
import randgen

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
    return Map



def AICreate():
    '''生成AI初始属性：姓名，饥饱度，想法'''
    #AIcnt = random.randint(1,100)
    AIcnt = 2
    AI = {}
    Sex, Name, Feed, Intention = {},{},{},{}

    nameLib = open('NameLib/name.pkl','rb')
    NameLib = pickle.load(nameLib)
    nameLib.close()

    for i in range(AIcnt):
        key = 'AI' + str(i).zfill(3)

        #初始随机性别
        Sex[key] = random.choice(['男','女'])


        #姓氏
        # nameLib = open('NameLib/name.pkl','rb')
        # NameLib = pickle.load(nameLib)
        # nameLib.close()
        nameRare = random.randint(1,10)
        if nameRare > 9:
            Fname = random.choice(NameLib['Fname']['R'])#生僻姓氏,占1成
        elif nameRare >7:
            j = random.randint(0,55)
            Fname = NameLib['Fname']['D'][j*2] + NameLib['Fname']['D'][j*2+1]#复姓氏,占2成
        else:
            Fname = random.choice(NameLib['Fname']['P'])#常用姓氏，占7成
        #
        #名字
        if Sex[key]=='男':#按性别挑选名字
            Sname = random.choice(NameLib['Sname']['M'])
        else:
            Sname = random.choice(NameLib['Sname']['F'])

        Name[key] =  Sname
        NameLib = None#释放变量内存

        Feed[key]       = random.randint(50,100)
        Intention[key]  = random.choice(['睡觉','走路','交谈','吃饭','学习','玩耍'])
    AI['Name'] = Name
    AI['Sex'] = Sex
    AI['Feed'] = Feed
    AI['Intention'] = Intention
    for key in AI['Name']:
        print '\t'+AI['Name'][key].ljust(10)+'\t'+ AI['Sex'][key]+'\t'+ str(AI['Feed'][key]) +'\t'+ AI['Intention'][key]
    return AI






















