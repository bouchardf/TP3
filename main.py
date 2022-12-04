#TP3 - Jeu de combat de monstres
#Fabrice Bouchard - 401
#Novembre/Décembre 2022

import random


# Définition des variables
niveau_monstre = random.randint(2, 11)
lance_des = random.randint(2, 12)
jeu = True
vie_joueur = 20
nb_combat = 0
nb_victoire = 0
nb_defaite = 0
nb_victoire_consecutive = 0

#Fonction du menu
def menu():
    global choix_joueur
    choix_joueur = int(input("Que voulez-vous faire \n 1- Combattre cet adversaire\n 2- Contourner cet adversaire et aller ouvrir une autre porte\n 3- Afficher les règles du jeu\n 4- Quitter la partie"))

#Fonction du combat avec un monstre
def combat():
    global nb_combat
    global vie_joueur
    global nb_victoire
    global nb_defaite
    global nb_victoire_consecutive
    nb_combat = nb_combat + 1
    print("Vous avez choisi de combattre cet adversaire")
    print(" Adversaire :", nb_combat, "\n Force de l’adversaire :", niveau_monstre, "\n Niveau de vie de l’usager :", vie_joueur, "\n Combat", nb_combat, ":", nb_victoire, "victoire et", nb_defaite, "défaite")
    print("Lancer du dé:", lance_des)
    #Victoire
    if lance_des >= niveau_monstre:
        print("Vous avez gagné! Votre vie est augmenté de", niveau_monstre)
        vie_joueur = vie_joueur + niveau_monstre
        nb_victoire = nb_victoire +1
        nb_victoire_consecutive = nb_victoire_consecutive + 1

    #Défaite
    elif lance_des <= niveau_monstre:
        print("Vous avez perdu... Votre vie est réduite de", niveau_monstre)
        vie_joueur = vie_joueur - niveau_monstre
        nb_defaite = nb_defaite + 1
        nb_victoire_consecutive = 0

    print("Niveau de vie :", vie_joueur, "\n Nombre de victoires consécutives :", nb_victoire_consecutive)

#Fonction pour contourner l'adversaire
def contourner():
    if choix_joueur == 2:
        print("Vous avez choisi de contourner cet adversaire \n Votre vie est réduite de 1")

#Fonction pour afficher les règles
def regle():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire. \n Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \n La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

#Fonction pour quitter le jeu
def quitter():
    print("Merci et au revoir...")
    global jeu
    jeu = False

#Fonction du Boss après 3 victoires
def boss():
    global niveau_monstre
    niveau_monstre = 11
    combat()

#Fonction de si le joueur à perdue
def fin_partie():
    print("La partie est terminé. \n Vous avez vaincu", nb_victoire, "monstres")

#Boucle du jeu
while jeu == True:
    niveau_monstre = random.randint(2, 11)
    print("Vous tombez face à face avec un adversaire de difficulté :", niveau_monstre)
    menu()
    if choix_joueur == 1:
        combat()

    elif choix_joueur == 2:
        contourner()

    elif choix_joueur == 3:
        regle()

    elif choix_joueur == 4:
        quitter()

    elif nb_victoire == 3:
        boss()

    elif vie_joueur <= 0:
        fin_partie()
