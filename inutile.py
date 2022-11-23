import arcade
from random import*

#Définir le décore
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WINDOW_TITLE = "Gros monstres pas fin avec des dés"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.start_render()

niveau_montre = randint(1, 5)

lance_des = randint(1, 6)

def decor():
    arcade.draw_rectangle_filled(600, 400, 1200, 400, arcade.color.GRAY)
    arcade.draw_rectangle_filled(20, 400, 50, 400, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(1180, 400, 50, 400, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(58, 380, 15, arcade.color.YELLOW_ORANGE)
    arcade.draw_circle_filled(1142, 380, 15, arcade.color.YELLOW_ORANGE)

def personnage():
    arcade.draw_rectangle_filled(200, 250, 50, 100, arcade.color.DARK_BLUE)

def enemie():
    arcade.draw_rectangle_filled(1000, 250, 50, 100, arcade.color.DARK_RED)
    arcade.draw_text(niveau_montre, 995, 250, arcade.color.BLACK)

def regles():
    arcade.draw_text(str("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."), 10, 775, arcade.color.PINK)
    arcade.draw_text(str("Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."), 10, 750, arcade.color.PINK)
    arcade.draw_text(str("Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."), 10, 725, arcade.color.PINK)
    arcade.draw_text(str("Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."), 10, 700, arcade.color.PINK)
    arcade.draw_text(str("La partie se termine lorsque les points de vie de l’usager tombent sous 0."), 10, 675, arcade.color.PINK)
    arcade.draw_text(str("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie."), 10, 650, arcade.color.PINK)

def menu():
    arcade.draw_text(("Vous tombez face à face avec un adversaire de difficulté :",niveau_montre), 10, 180, arcade.color.PURPLE)
    arcade.draw_text(str("1- Combattre cet adversaire"), 10, 180, arcade.color.PURPLE)
    arcade.draw_text(str("2- Contourner cet adversaire et aller ouvrir une autre porte"), 15, 160, arcade.color.PURPLE)
    arcade.draw_text(str("3- Afficher les règles du jeu"), 10, 180, arcade.color.PURPLE)
    arcade.draw_text(str("4- Quitter la partie"), 10, 180, arcade.color.PURPLE)


decor()
personnage()
enemie()
regles()
menu()
arcade.finish_render()
arcade.run()