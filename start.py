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

def AICreate():
    #AIcnt = random.randint(1,100)
    AIcnt = 5
    AI_Name, AI_Feed, AI_Intention = {},{},{}
    for i in range(AIcnt):
        key = 'AI' + str(i).zfill(3)
        AI_Name[key]       = key
        AI_Feed[key]       = random.randint(50,100)
        AI_Intention[key]  = random.choice(['睡觉','走路','交谈','吃饭','学习','玩'])
    return AI_Name,AI_Feed,AI_Intention



















