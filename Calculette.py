
import sys
from Addition import *
from Soustraction import *
from Division import *
from Multiplication import *


	

Valeur1 = ""
Calcul = None
Valeur2 = ""

while 1:
	
	entree = sys.stdin.read(1)
	try :
		if Calcul == None :
			int(entree)
			Valeur1 = Valeur1 + entree
		else:
			int(entree)
			Valeur2 = Valeur2 + entree

	except ValueError: 
		if entree == "+" or entree == "-" or entree == "*" or entree == "/":
			Calcul = entree
		else:
			break


if Calcul == "+":
	calcul_addition(int(Valeur1),int(Valeur2))
elif Calcul == "-":
	calcul_soustraction(int(Valeur1),int(Valeur2))
elif Calcul == "*":
	calcul_multiplication(int(Valeur1),int(Valeur2))
elif Calcul == "/":
	calcul_division(int(Valeur1),int(Valeur2))
else:
	print ("dsl gars mais cette calculatrice n'est pas assez soffistiquée pour calculer ca!")

	
	
