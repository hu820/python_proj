#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Numpy offers several ways to index into arrays.
# Slicing: Similar to Python lists, numpy arrays can be sliced.
# Since arrays may be multidimensional, you must specify a slice for each dimension of the array:
# 切片和索引的同异（：与，）
# 切片和索引都是访问多维数组中元素的方法，这是两者的共同点，不同之处有:
#
# 切片得到的是原多维数组的一个 视图(view) ，修改切片中的内容会导致原多维数组的内容也发生变化
# 切片得到在多维数组中连续(或按特定步长连续)排列的值，而索引可以得到任意位置的值，自由度更大一些

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[0:2, 1:3]  # 选取前两行，第2，3列
print(b)
print(a[0, 2])

b[0:1] = 55
print(a)

b[0, 1] = 55
print(a)  # 注意区分b[0,1]与b[0:1]

# array indexing
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])  # 对a取第1，2，3行，然后分别取第1，2，1列，print [1 4 5]

# Boolean index
arr = np.array([[1, 2, 3, 4],
                [2, 4, 6, 8],
                [3, 6, 9, 12],
                [4, 8, 12, 16]])
mask = arr > 5

print 'boolean mask is:'
print mask
print arr[mask]

# 取一些特定位置
# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
#                [ 4,  5,  6],
#                [ 7,  8,  9],
#                [10, 11, 12]])"
# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
# 去一个等差数据，【0，1，2，3】然后在取第1，3，1，2列
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# 做一些特殊的加法等
# Mutate one element from each row of a using the indices in b
# 先取出前4行，然后取第第1，3，1，2列，在这些数据上加10
a[np.arange(4), b] += 10
print(a)  # prints "array([[11,  2,  3],
#                [ 4,  5, 16],
#                [17,  8,  9],
#                [10, 21, 12]])
