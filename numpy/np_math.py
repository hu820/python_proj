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

# 求和
print(np.sum(x))
# print 10
print(np.sum(x, axis=0))  # Compute sum of each column
# print [4,6]
print(np.sum(x, axis=1))  # Compute sum of each row;
# print [3,7]

# Broadcasting
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)  # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v  # 相当于取出X的每一行元素，加V

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)
