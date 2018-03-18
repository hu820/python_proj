#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(type(a))  # Prints "<class 'numpy.ndarray'>"
print(a.shape)  # Prints "(3,)"
print(a[0], a[1], a[2])  # Prints "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)  # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])  # Prints "1 2 4"

a = np.zeros((2, 3))  # 创建一个2*3的数组
print(a)

b = np.ones((1, 2))  # 创建一个1*2的全是0的数组
print(b)

c = np.full((2, 9), 5)  # 创建一个2*9的全是5的数组
print(c)

d = np.eye(4)  # 创建一个4*4的单位矩阵
print(d)

e = np.random.random(5 * 5)  # 创建一个5*5的随机数组
print(e)
