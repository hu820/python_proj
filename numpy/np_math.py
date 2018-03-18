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

# This works; however when the matrix x is very large, computing an explicit loop in Python could be slow. Note that
# adding the vector v to each row of the matrix x is equivalent to forming a matrix vv by stacking multiple copies of
# v vertically, then performing elementwise summation of x and vv. We could implement this approach like this:

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
print(vv)  # Prints "[[1 0 1]
#          [1 0 1]
#          [1 0 1]
#          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
#          [ 5  5  7]
#          [ 8  8 10]
#          [11 11 13]]"

# Numpy broadcasting allows us to perform this computation without actually creating multiple copies of v. Consider
# this version, using broadcasting:
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)  # Prints "[[ 2  2  4]
#          [ 5  5  7]
#          [ 8  8 10]
#          [11 11 13]]"

# Broadcasting two arrays together follows these rules:
#
# If the arrays do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have
# the same length.
# The two arrays are said to be compatible in a dimension if they have the same size in the
# dimension, or if one of the arrays has size 1 in that dimension.
# The arrays can be broadcast together if they are compatible in all dimensions. After broadcasting,
# each array behaves as if it had shape equal to the elementwise
# maximum of shapes of the two input arrays.
# In any dimension where one array had size 1 and the other array had size
#  greater than 1, the first array behaves as if it were copied along that dimension

# 让所有输入数组都向其中shape最长的数组看齐，shape中不足的部分都通过在前面加1补齐
# 输出数组的shape是输入数组shape的各个轴上的最大值
# 如果输入数组的某个轴和输出数组的对应轴的长度相同或者其长度为1时，这个数组能够用来计算，否则出错
# 当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值
