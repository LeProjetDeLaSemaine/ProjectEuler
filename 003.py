#/usr/bin/python
# -*- coding: utf-8 -*-

def p003(N):
	d = 2
	while N % d:
		d = d+1
	return N if N==d else p003(N//d)

print(p003(600851475143))