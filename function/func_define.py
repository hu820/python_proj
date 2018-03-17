# coding=utf-8
# python function define
## python函数使用'def'关键词进行定义
def sign(x):
    if (x > 0):
        return 'positive'
    elif x < 0:
        return 'negitive'
    else:
        return 'zero'


for x in range(-10, 10, 2):
    print('%x:%s' %(x,sign(x)))
