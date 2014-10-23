#/usr/bin/python
# -*- coding: utf-8 -*-

def p002(N):
	u0, u1 = 0, 1 #premiers termes
	S = 0
	while u1 < N:
		S += (u1 if u1%2==0 else 0) #s'il est pair on l'ajoute, sinon on ajoute rien
		u0, u1 = u1, u0+u1 #on passe au rang suivant (Un-1 = Un, Un = Un+1)
	return(S)

print(p002(4000000))

#12 premieres valeurs :
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
#leurs modulos 2 donnent :
#0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0
#On peut montrer par récurrence (cf bout de papier et crayon)
#que Fib(n) est pair ssi n % 3 = 0
#apres, j'sais pas encore quoi en faire donc je reste sur la 1ere méthode ^^