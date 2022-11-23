import random

niveau_montre = random.randint(1, 5)
lance_des = random.randint(1, 6)
jeu = True
vie_joueur = 20

def menu():
    choix_joueur = int(input("Que voulez-vous faire \n 1- Combattre cet adversaire\n 2- Contourner cet adversaire et aller ouvrir une autre porte\n 3- Afficher les règles du jeu\n 4- Quitter la partie"))
    if choix_joueur == 1:
        print("Vous avez choisi de combattre cet adversaire")

    elif choix_joueur == 2:
        print("Vous avez choisi de contourner cet adversaire")

    elif choix_joueur == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")


while jeu == True:
    niveau_montre = random.randint(1, 5)
    print("Vous tombez face à face avec un adversaire de difficulté :", niveau_montre)
    menu()
