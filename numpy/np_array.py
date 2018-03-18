#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Numpy offers several ways to index into arrays.
# Slicing: Similar to Python lists, numpy arrays can be sliced.
# Since arrays may be multidimensional, you must specify a slice for each dimension of the array:
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
