import socket
import sys
from Addition import *
from Soustraction import *
from Division import *
from Multiplication import *

hote = "127.0.0.1"
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

Valeur1 = ""
Calcul = None
Valeur2 = ""

while 1:
	
	entree = connexion_avec_client.recv(1).decode()              	# j annalyse (concatainer?) les donée envoyé par le client : invoque entree
	
	try :
		
		if Calcul == None:											# si le signe est inchangé je modifi Valeur1
			int(entree)
			Valeur1 = Valeur1 + entree
		else:														# sinn je modifi Valeur2
			int(entree)
			Valeur2 = Valeur2 + entree

	except ValueError: 												# si entre n 'est pas un entier'
		
		if entree == "+" or entree == "-" or entree == "*" or entree == "/":		# si c'est un signe je modifie Calcul 
			Calcul = entree
		else:
			break


if Calcul == "+":
	
	resultat = calcul_addition(int(Valeur1),int(Valeur2))
	connexion_avec_client.send("{} moins {} est égale à {}".format(Valeur1, Valeur2, resultat).encode())			# jenvoi au client (.format mdifié plusieur variable)
	print (Valeur1, " plus ", Valeur2, "est égale à: ", resultat)											# jaffiche sur le serveur


elif Calcul == "-":
	
	resultat = calcul_soustraction(int(Valeur1),int(Valeur2))
	connexion_avec_client.send("{} moins {} est égale à {}".format(Valeur1, Valeur2, resultat).encode())		# j envoi au clent en concatainant{}>>() et j'encode
	print ("{} moins {} est égale à {}".format(Valeur1, Valeur2, resultat))										# jaffiche sur le serveur


elif Calcul == "*":
	
	resultat = calcul_multiplication(int(Valeur1),int(Valeur2))
	connexion_avec_client.send("{} multiplé par {} est égale à {}".format(Valeur1, Valeur2, resultat).encode())			# j envoi au clent
	print ("{} multiplé par {} est égale à {}".format(Valeur1, Valeur2, resultat))							# j'affiche sur le serveur


elif Calcul == "/":

	resultat = calcul_division(int(Valeur1),int(Valeur2))
	connexion_avec_client.send("{} divisé par {} est égale à {}".format(Valeur1, Valeur2, resultat).encode())	# j envoi au client
	print ("{} divisé par {} est égale à {}".format(Valeur1, Valeur2, resultat))								# jaffiche sur le serveur


else:

	
	connexion_avec_client.send(b"dsl gars mais cette calculatrice n est pas assez soffistiquee pour calculer ca")		
	print ("dsl gars mais cette calculatrice n'est pas assez soffistiquée pour calculer ca!")
