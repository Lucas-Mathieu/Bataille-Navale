from tkinter import *

def initialisation() :
    """
    Initialisation des varibles globales nécessaires au fonctionement de jeu, pas de paramètres d'entré ou de sortie.

    grille_1/2 : Matrice de 10 x 10 représentant la grille de jeu de chaque joueur, 0 représente une case vide
    tour_joueur_1 : Boolean indiquant si c'est le tour du joueur 1 ou non (et par éxtension si c'est celui du joueur 2)
    partie_en_cour : Boolean indiquant si la partie est en cour ou non
    """
    global grille_1 
    global grille_2
    global tour_joueur_1
    global partie_en_cour

    grille_1 = [[0] * 10 for x in range(10)]
    grille_2 = [[0] * 10 for x in range(10)]
    tour_joueur_1 = True
    partie_en_cour = True

def dessin_grille() :
    """
    Dessin des lignes verticales et horizontale de la grille dans la fenêtre de jeu à l'aide de tkinter.

    Pas de paramètre d'entrée ou de sortie.
    """
    # dessin des lignes verticales
    écart = 100
    for i in range(11):
        haut = 0
        bas = 600
        Zone.create_line (écart, haut, écart, bas, width=4, fill="blue")
        écart += 60

    # dessin des lignes horizontales
    écart = 0
    for i in range(11):
        gauche = 100
        droite = 700
        Zone.create_line (gauche , écart , droite , écart ,width=4,fill="blue")
        écart += 60

def affichage_grille() :
    """
    Affichage de la grille du jouer dont c'est actuellement le tour dans la console, pas de paramètre d'entré ou de sortie.

    Cette fonction est surtout présente pour des raisons de tests
    """

    #vérification du tour
    if tour_joueur_1 :
        grille = grille_1
    else :
        grille = grille_2

    #affichage dans la console des 10 lignes de la matrice
    for x in range(10) :
        print(grille[x])
    print("")

def coordonnees(event) :
    #vérification du tour
    if tour_joueur_1 :
        grille = grille_1
    else :
        grille = grille_2

    #détermination de la case avec une division euclidienne des coordonnées par la taille des cases
    col = (event.x-100) // 60
    li = event.y // 60

    #verification que le clic est dans la grille et non la marge de gauche
    if col >= 0 :

        if grille[li][col] == 0 :
            grille[li][col] = 1
            affichage_grille()
        else :
            grille[li][col] = 0
            affichage_grille()

    #message d'erreur si hors de la grille
    else :
        print("Clic en dehors de la grille")




"""================PROGRAMME PRINCIPAL================"""

fen=Tk()
fen.geometry ("700x600")
fen.title ("Bataille Navale")
fen.bind('<Button-1>',coordonnees)
Zone=Canvas(fen,width=700,height=600,bg="grey")
Zone.place(x=0,y=0)


initialisation()
affichage_grille()
dessin_grille()
#while partie_en_cour :
    


fen.mainloop()