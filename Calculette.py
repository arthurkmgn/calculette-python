

from Addition import *
from Soustraction import *
from Division import *
from Multiplication import *


	

Valeur1 = int(input())
Calcul = input()
Valeur2 = int(input())

while entree = read(1):
	entree = sys.stdin.read(1)
		try :
			int(entree)
			Valeur1 = Valeur1 + entree 
		except: 
			if entree == "+" or entre == "-" or entre == "*" or entree == "entree":
				Calcul = entree

while 1:
	if Calcul == "+":
		calcul_addition(Valeur1,Valeur2)
	elif Calcul == "-":
		calcul_soustraction(Valeur1,Valeur2)
	elif Calcul == "*":
		calcul_multiplication(Valeur1,Valeur2)
	elif Calcul == "/":
		calcul_division(Valeur1,Valeur2)
	else:
		print ("dsl gars mais cette calculatrice n'est pas assez soffistiquée pour calculer ca!")

	
	
