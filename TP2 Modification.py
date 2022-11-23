#Jeu de devinette
#29 septembre 2022
#Créé par Fabrice Bouchard

from random import*

# Défnition des variables et de la fonction de début de jeu

def debutJeu():
    nb_essai == 0
    fin_jeu == False
    rejouer == None

    choix_borne = input("Voulez-vous décider des bornes? Entrer Y pour oui et N pour non")

    if choix_borne == "Y":
        borneUn = int(input("Entrez la première borne:"))

        borneDeux = int(input("Entrez la deuxième borne:"))

    elif choix_borne == "N":
        borneUn = 0
        borneDeux = 1000

    nombre_aleatoire = randint(borneUn, borneDeux)

    print("J’ai choisi un nombre au hasard entre", borneUn, "et", borneDeux, ". À vous de le deviner...")
#Défnition de la fonction principale

def jeu():
    debutJeu()
    #Mise en place de la boucle dans laquelle le jeu prend place
    while fin_jeu == False:
        nb_joueur = int(input("Entrez votre essai :_"))
        nb_essai = nb_essai + 1

        # Si le nombre est plus petit
        if nb_joueur > nombre_aleatoire:
            print("Mauvais choix, le nombre est plus petit que" ,nb_joueur,)

        # Si le nombre est plus grand
        elif nb_joueur < nombre_aleatoire:
            print("Mauvaise réponse, le nombre est plus grand que" ,nb_joueur,)

        elif nb_joueur == nombre_aleatoire:     #Si l'essai est le bon
            print("Bravo! Bonne réponse! Vous avez réussi en:", nb_essai, "essais")

            rejouer = input("Voulez rejouer? Entrer n pour quitter et o pour continuer.")

            # Si le joueur veut quitter
            if rejouer == "n":
                print("Merci et au revoir...")
                fin_jeu = True

            # Si le joueur veut rejouer
            elif rejouer == "o":
              debut_jeu()
jeu()