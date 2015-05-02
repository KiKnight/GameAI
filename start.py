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
    Mapcnt = 10
    Map = {}
    Form, Scale, Rare, Build, Belong = zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt])

    #为保证地图延续性，分为上下左右四块
    #随机出基础地形
    Mapcnt = Mapcnt+2
    Tope = zeros([Mapcnt,Mapcnt])
    for i in range(1,Mapcnt/2):
        for j in range(1,Mapcnt/2):
            key = 'MAP' + str(i).zfill(3)+str(j).zfill(3)
            #随机出地形0水域 1平原 2山地
            Tope[i][j] =  abs(int((Tope[i-1][j] + Tope[i][j-1])/2) + random.choice([-1,0,1]))
            if Tope[i][j]>=3:
                Tope[i][j] = 3 - Tope[i][j]
            if Tope[i][j] == 0 and random.randint(1,5)>3:
                Tope[i][j] = random.randint(1,2)
    for i in range(Mapcnt-2,Mapcnt/2-1,-1):
        for j in range(1,Mapcnt/2):
            key = 'MAP' + str(i).zfill(3)+str(j).zfill(3)
            #随机出地形0水域 1平原 2山地
            Tope[i][j] =  abs(int((Tope[i-1][j] + Tope[i][j+1])/2) + random.choice([-1,0,1]))
            if Tope[i][j]>=3:
                Tope[i][j] = 3 - Tope[i][j]
            if Tope[i][j] == 0 and random.randint(1,5)>3:
                Tope[i][j] = random.randint(1,2)
    for i in range(Mapcnt-2,Mapcnt/2-1,-1):
        for j in range(Mapcnt-2,Mapcnt/2-1,-1):
            key = 'MAP' + str(i).zfill(3)+str(j).zfill(3)
            #随机出地形0水域 1平原 2山地
            Tope[i][j] =  abs(int((Tope[i+1][j] + Tope[i][j+1])/2) + random.choice([-1,0,1]))
            if Tope[i][j]>=3:
                Tope[i][j] = 3 - Tope[i][j]
            if Tope[i][j] == 0 and random.randint(1,5)>3:
                Tope[i][j] = random.randint(1,2)
    for i in range(1,Mapcnt/2):
        for j in range(Mapcnt-2,Mapcnt/2-1,-1):
            key = 'MAP' + str(i).zfill(3)+str(j).zfill(3)
            #随机出地形0水域 1平原 2山地
            Tope[i][j] =  abs(int((Tope[i+1][j] + Tope[i][j-1])/2) + random.choice([-1,0,1]))
            if Tope[i][j]>=3:
                Tope[i][j] = 3 - Tope[i][j]
            if Tope[i][j] == 0 and random.randint(1,5)>3:
                Tope[i][j] = random.randint(1,2)


    for i in range(1,Mapcnt-1):
        for j in range(1,Mapcnt-1):
            Form[i-1][j-1] = Tope[i][j]

        # key = 'MAP' + str(i).zfill(3)
        # #Name[key]     = key
        #
        # #随机尺寸大小，尺度越大，种群和建筑越丰富
        # Scale[key]    = int(abs(random.normalvariate(0,1))*10)
        # Scale[key] = randgen.DataRestric(Scale[key])
        #
        # #随机稀有度，稀有度越高，产物越珍贵
        # Rare[key] = int(abs(random.normalvariate(0,1))*10)
        # Rare[key] = randgen.DataRestric(Rare[key])
        #
        #
        # Build[key]    = 0
        # Belong[key]   = 0
    #Map['Name'] = Name
    # Map['Feed'] = Scale
    # Map['Intention'] = Rare
    # return Map



def AICreate():
    '''生成AI初始属性：性别，姓名'''
    AIcnt = random.randint(1,100)
    AI = {}
    Sex, Name, Feed, Intention, test, Age, Location = {},{},{},{},{},{}, {}

    #随机生成姓名
    nameLib = open('NameLib/name.pkl','rb')
    NameLib = pickle.load(nameLib)
    nameLib.close()

    for i in range(AIcnt):
        key = 'AI' + str(i).zfill(4)

        #初始随机性别
        Sex[key] = random.choice(['男','女'])

        #姓氏
        nameRare = random.randint(1,10)
        if nameRare > 9:
            Fname = random.choice(NameLib['Fname']['R'])#生僻姓氏,占1成
        elif nameRare >7:
            j = random.randint(0,55)
            Fname = NameLib['Fname']['D'][j*2] + NameLib['Fname']['D'][j*2+1]#复姓氏,占2成
        else:
            Fname = random.choice(NameLib['Fname']['P'])#常用姓氏，占7成
        #名字
        if Sex[key]=='男':#按性别挑选名字
            Sname = random.choice(NameLib['Sname']['M'])
        else:
            Sname = random.choice(NameLib['Sname']['F'])

        Name[key] = Fname + Sname

        #随机生成年龄：
        Age[key] = random.randint(20,100)

        #随机分配到地图
        test[key] = key
        Feed[key] = random.randint(50,100)
        Intention[key] = random.choice(['睡觉','走路','交谈','吃饭','学习','玩耍'])

    AI['Name'] = Name
    AI['Sex'] = Sex
    AI['Age'] = Age
    AI['Feed'] = Feed
    AI['Intention'] = Intention
    AI['test'] = test
    for key in AI['Name']:
        print '\t'+AI['Name'][key].ljust(10)+'\t'+ AI['test'][key]+'\t'+ AI['Sex'][key]+'\t'+ str(AI['Feed'][key]) +'\t'+ AI['Intention'][key]
    return AI

