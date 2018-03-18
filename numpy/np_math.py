#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.int)
y = np.array([[5, 6], [7, 8]], dtype=np.int)

# 加法
print(x + y)
print(np.add(x, y))
# print
# [[ 6  8]
#  [10 12]]

# 减法
print(x - y)
print(np.subtract(x, y))
# print
# [[-4 -4]
#  [-4 -4]]

# 乘法
print(x * y)
print(np.multiply(x, y))
# print
# [[ 5 12]
#  [21 32]]

# 开方
print(np.sqrt(x))
# print
# [[1.         1.41421356]
#  [1.73205081 2.        ]]
