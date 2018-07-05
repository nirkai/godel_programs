#!/usr/bin/env python

import sys
#from sympy.ntheory import factorint

def even_x(num):
	x = 0
	while(num % 2 == 0):
		x += 1
		num = num / 2
	return num, x

def fuctors(num):
	y, x = even_x(num)
	if y > 0:
		y = y - 1
		y = y / 2
	return x, y

def code_to_num(a, b):
	result = (2**a) * (2*b + 1) - 1
	return result

def code_to_num2(mytuple):
	return code_to_num(mytuple[0], mytuple[1])

num = sys.argv[1]
x,y = fuctors(int(num) + 1)
print '<',x,',',y,'>'
print code_to_num(x,y)
c = x, y
print code_to_num2(c)
