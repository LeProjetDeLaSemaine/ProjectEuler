#!/usr/bin/python
# -*- coding: utf-8 -*-

def p004bof():
    rng = range(900, 1000) #on suppose que les facteurs sont dans rng parce qu'on a du flair
    return max((x*y
                for x in rng #1er facteur
                    for y in rng #2e facteur
                        if str(x*y) == str(x*y)[::-1])) #test du palindrôme


#version optimisée (avec un peu de logique) :
#on établit que bestp = abccba (forcément, c'est un palindrôme)
#donc bestp = 100001a + 10010b + 1100c
#on factorise : bestp = 11 * (9091a + 910b + 100c)
#on en déduit alors qu'un des facteurs de bestp est divisible par 11
#ce qui rend le process plus rapide

def p004():
    bestp = 0
    for i in range(110, 1000, 11):#de 11 en 11
        for j in range(i, 1000):
            p = i *j
            if p > bestp and str(p) == str(p)[::-1]:#si p un palindrôme > à bestp
                bestp = p
    return bestp


print(p004bof()) #le marteau écrasant les mouches
print(p004())