#coding:utf-8

def DataRestric(data):
    if data == 0:
        data = 1
    elif data > 20:
        data = 20
    else:
        pass
    return data
