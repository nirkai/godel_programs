#!/usr/bin/env python

import math
def is_prime(n):
    if n < 2:
	return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def nextprime(n):
	n += 1
	while (not is_prime(n)):
		n += 1
	return n

def proce_prime(n):
	p = 2
	p_p = 2
	while (p < n):
		p_p = p
		p = nextprime(p)
	return p_p

def godel(n):
	primes = list()
	fuct = list()
	godel_list = list()
	f_count = 0
	p = proce_prime(n+1)
	flag = False
	while (n > 0):
		while (n >= p and n % p == 0):
			f_count += 1
			n = n / p
			flag = True
		if flag:
			primes.append(p)
			fuct.append(f_count)
			tup = p, f_count
			godel_list.insert(0,tup)
		if p == 2:
			break
		f_count = 0
		p = proce_prime(p-1)
	print primes
	print fuct
	print godel_list

godel(65)
#print nextprime(1)
#print proce_prime(2)
#print nextprime(24)

