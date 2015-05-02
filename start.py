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

def MapCreate():
    '''生成地图初始属性：地名，大小，稀有度'''
    Mapcnt = 6
    Map = {}
    City = []
    Form, Scale, Rare, Build, Belong = zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt]),zeros([Mapcnt,Mapcnt])

    for i in range(Mapcnt):
        for j in range(Mapcnt):

            #随机出地形
            Form[i][j] = random.randint(0,2)

            #随机地块尺寸大小，决定容纳建筑和种群多少
            Scale[i][j] = int(abs(random.normalvariate(0,1))*10)
            Scale[i][j] = randgen.DataRestric(Scale[i][j])
            #生成城市
            if Scale[i][j] > 6 and random.randint(1,5)>2:#尺寸够大，可建城，60%概率
                key = 'C'+str(i).zfill(3)+str(j).zfill(3)
                City.append(key)

            #随机地块稀有度，决定物产的珍贵性
            Rare[i][j] = int(abs(random.normalvariate(0,1))*10)
            Rare[i][j] = randgen.DataRestric(Rare[i][j])

    # print City
    # print len(City)
    Map['Form'] = Form
    Map['Scale'] = Scale
    Map['City'] = City
    Map['Rare'] = Rare
    return Map



def AICreate(AIcnt):
    '''生成AI初始属性：性别，姓名'''
    AIcnt = random.randint(200,500)
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

        test[key] = key
        Feed[key] = random.randint(50,100)
        Intention[key] = random.choice(['睡觉','走路','交谈','吃饭','学习','玩耍'])

    AI['Name'] = Name
    AI['Sex'] = Sex
    AI['Age'] = Age
    AI['Feed'] = Feed
    AI['Intention'] = Intention
    AI['test'] = test

    # for key in AI['Name']:
    #     print '\t'+AI['Name'][key].ljust(10)+'\t'+ str(AI['Location'][key])
    return AI

def SubGen(Map,AI):
    '''由随机的地图和AI生成次级信息'''
    AI2 = {}
    Belong, Relation= {},{}

    #按城市数量划定AI归属
    citycnt = len(Map['City'])
    city_hum = {}
    for key in Map['City']:
        city_hum[key] = []
    for key in AI['Name']:
        citynum = random.randint(0,citycnt-1)
        Belong[key] = citynum#AI随机分配到城市
        citykey = Map['City'][citynum]
        city_hum[citykey].append(key)
    # for citykey in Map['City']:
    #     print city_hum[citykey]


    for citykey in Map['City']:
        Temp1 = []
        Temp2 = []
        for key in city_hum[citykey]:
            if AI['Sex'][key] == '男':
                Temp1.append(key)
            else:
                Temp2.append(key)
        print key + str(Temp1)
        print Temp2
        while(len(Temp1)!=0):
            for i in range(len(Temp2)):
                if (AI['Age'][Temp1[0]]-AI['Age'][Temp2[i]]>=0) and (AI['Age'][Temp1[0]]-AI['Age'][Temp2[i]]<=30):#满足匹配条件
                    if random.randint(1,3)>1:#匹配成功
                        Relation[Temp1[0]] = Temp2[i]
                        Relation[Temp2[i]] = Temp1[0]
                        del Temp2[i]
                    else:#未匹配成功
                        Relation[Temp1[0]] = None
                    break
            del Temp1[0]
        for key in Temp2:
            Relation[key] = None
    #
    print Relation
    AI['Belong'] = Belong
    AI['Relation'] = Relation

    # for key in Map['City']:
    #     print city_hum[key]