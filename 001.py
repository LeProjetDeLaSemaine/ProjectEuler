#/usr/bin/python
# -*- coding: utf-8 -*-

def p001(N):
	gen = (i for i in range(N) if i%3==0 or i%5==0) #vive les générateurs
	return sum(gen)
	#<troll>return sum((i for i in range(N) if i%3==0 or i%5==0))</troll>

print(p001(1000))