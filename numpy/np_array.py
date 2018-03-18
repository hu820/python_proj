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
