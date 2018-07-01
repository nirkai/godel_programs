#!/usr/bin/env python

import sys
from sympy.ntheory import factorint
from sympy import nextprime

def fuctors(num):
	result = factorint(num)
	primes = list(result)
	factorials = result.values()
	return primes, factorials

def godel(p, f):
	p_list = list()
	f_list = list()
	last_p = p[len(p)-1]
	cur_p = p[0]
	next_p = nextprime(0)
	index = 0
	while (next_p <= last_p):
		if next_p < cur_p:
			p_list.append(0)
			f_list.append(0)
		else:
			p_list.append(p[index])
			f_list.append(f[index])
			index += 1
			if index < len(p):
				cur_p = p[index]
		next_p = nextprime(next_p)
		
	return p_list, f_list

num = sys.argv[1]
pr, fa = fuctors(int(num))
p, f = godel(pr, fa)
print 'primes:  ', p
print 'factors: ', f
