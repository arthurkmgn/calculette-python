import socket
import sys

hote = "127.0.0.1"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


msg_a_envoyer = ""

print ("tu veux calculer quoi? (ESPACE pour valider)")


Valeur1 = ""
Calcul = 0
Valeur2 = ""

while 1:
	
	entree = sys.stdin.read(1)              	# j annalyse  les donée envoyé par le client : invoque entree
	print(entree)
	try :
		int(entree)
		if Calcul == 0:											# si le signe est inchangé je modifi Valeur1
			Valeur1 = Valeur1 + entree
		else:														# sinn je modifi Valeur2
			Valeur2 = Valeur2 + entree

	except ValueError: 												# si entre n 'est pas un entier'
		
		if entree == "+" or entree == "-" or entree == "*" or entree == "/":		# si c'est un signe je modifie Calcul 
			Calcul = entree

		else:
			connexion_avec_serveur.send(str(Valeur1).encode())
			connexion_avec_serveur.send(str(Calcul).encode())
			connexion_avec_serveur.send(str(Valeur2).encode())
			connexion_avec_serveur.send(str(" ").encode())
			break


msg_recu = connexion_avec_serveur.recv(1024)
print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()