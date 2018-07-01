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

num = sys.argv[1]
x,y = fuctors(int(num) + 1)
print '<',x,',',y,'>'
