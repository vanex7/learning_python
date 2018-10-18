#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# height = 1.75
# weight = 70

# bmi = weight / (height * 2)
# print(bmi)

# names = ['A', 'B', 'C']

# for name in names:
# 	print(name)


# sum = 0
# for i in range(101):
# 	sum = sum + i
# print(sum)

# l = ['a', 'b', 'c']
# d = {str(l):'test'}
# print(d)

# n1 = 255
# print(hex(001))

# l 在函数初始化时就定义了
# def add_end(l = []):
# 	l.append("END")
# 	return l
# print(add_end())
# print(add_end())

# 解决方案
# def add_end2(l = None):
# 	if l == None :
# 		l = []
# 	l.append("END")
# 	return l
# print(add_end2())
# print(add_end2())
# print(add_end2())


def calc(first, *nums):
	sum = first
	for num in nums:
		sum = num + sum
	print(sum)
calc(1, 2, 3, 4, 5, 6, *range(100))