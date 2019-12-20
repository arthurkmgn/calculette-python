import socket
import sys

hote = "127.0.0.1"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


msg_a_envoyer = ""

print ("tu veux calculer quoi?")


Valeur1 = ""
Calcul = False
Valeur2 = ""

while 1:
	
	entree = sys.stdin.read(1)              	# j annalyse (concatainer?) les donée envoyé par le client : invoque entree
	
	try :
		
		if not Calcul:											# si le signe est inchangé je modifi Valeur1
			int(entree)
			Valeur1 = Valeur1 + entree
		else:														# sinn je modifi Valeur2
			int(entree)
			Valeur2 = Valeur2 + entree

	except ValueError: 												# si entre n 'est pas un entier'
		
		if entree == "+" or entree == "-" or entree == "*" or entree == "/":		# si c'est un signe je modifie Calcul 
			connexion_avec_serveur.send(Valeur1)
			connexion_avec_serveur.send(entree)
			Calcul = True
		else:
			connexion_avec_serveur.send(Valeur2)


msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()