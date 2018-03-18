#!/usr/bin/python
# -*- coding: UTF-8 -*-

# A tuple is an (immutable) ordered list of values.
# A tuple is in many ways similar to a list;
# one of the most important differences is that tuples can be used as keys in dictionaries
# and as elements of sets, while lists cannot.

d = {(x, x * 2): x for x in range(10)}
print(d)
print(type(d))
t = (1, 2)
print(type(t))
print(d[t])

tuple_data = (5, 2, 3,)
print(type(tuple_data))

print "tup[0:2]: ", tuple_data[0:2]  # print tup[0:2]:  (5, 2)
# tuple_data[1] =10  元组数据不允许修改
print(tuple_data)

# 元组数据加法
tup_1 = (1, 2, 3)
tup_2 = (4, 5, 6)
tup_3 = tup_1 + tup_2
print(tup_3)  # print (1, 2, 3, 4, 5, 6)

# 元组不支持修改数据，但可以用del删除整个元组
del tup_3
# print(tup_3) 将报错

# 循环
for item in tup_1:
    print(item)
# 复制
tup_4 = tup_1 * 3
print(tup_4)
