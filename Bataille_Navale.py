from tkinter import *

def initialisation() :
    """
    Initialisation des varibles globales nécessaires au fonctionement de jeu, pas de paramètres d'entré ou de sortie.

    grille_1/2 : Matrice de 10 x 10 représentant la grille de jeu de chaque joueur, 0 représente une case vide
    tour_joueur_1 : Boolean indiquant si c'est le tour du joueur 1 ou non (et par éxtension si c'est celui du joueur 2)
    partie_en_cour : Boolean indiquant si la partie est en cour ou non
    placement_en_cour : Boolean indiquant si c'est la phase de placement des bateau
    bateaux1/2 : liste d'entiers indiquant la longueur des différents bateaux de chaque joueurs
    horizontal : Boolean indiquant si le bateau que l'on souhaite placer est horizontal ou vertical
    """
    global grille_1 
    global grille_2
    global tour_joueur_1
    global partie_en_cour
    global placement_en_cour
    global bateaux1
    global bateaux2
    global horizontal

    grille_1 = [[0] * 10 for x in range(10)]
    grille_2 = [[0] * 10 for x in range(10)]
    tour_joueur_1 = True
    partie_en_cour = True
    placement_en_cour = True
    bateaux1 = [5,4,3,3,2]
    bateaux2 = [5,4,3,3,2]
    horizontal = True

def dessin_grille() :
    """
    Dessin des lignes verticales et horizontale de la grille dans la fenêtre de jeu à l'aide de tkinter.

    Pas de paramètre d'entrée ou de sortie.
    """
    # dessin des lignes verticales
    écart = 4
    for x in range(11):
        haut = 100
        bas = 700
        Zone.create_line (écart, haut, écart, bas, width=4, fill="blue")
        écart += 60

    # dessin des lignes horizontales
    écart = 100
    for x in range(11):
        gauche = 0
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
    for index in range(10) :
        print(grille[index])
    print("")

def direction(event):
    """
    Change la direction de placement du bateau en vertical ou horizontal en fonction de l'inverse du boolean associé a cet aspect

    Pas de paramètres d'entrée ou de sortie
    """
    global horizontal

    horizontal = not horizontal
    if horizontal :
        print("Horizontal")
    else :
        print("verical")

def coordonnees(event) :
    """
    Cette fonction est appelé à chaque clic et calcul la case choisie a partir des coordonnées de la souris

    Pas de paramètre en entrée ou sortie.
    """
    #détermination de la case avec une division euclidienne des coordonnées par la taille des cases en prenant en compte la marge de 100 pixels pour la ligne
    col = event.x // 60
    li = (event.y-100) // 60

    #verification que le clic est dans la grille et non la marge en haut
    if li >= 0 :
        placement(li, col)

    #message d'erreur si hors de la grille
    else :
        print("Clic en dehors de la grille")

def placement(li, col) :
    """
    Fonction de placement, gère le positionnement des bateaux et des bombardages sur la grille

    Prends en paramètre la ligne, la colonne choisie et la direction du bateaux, ne retourne rien. 
    """
    global tour_joueur_1
    global placement_en_cour
    global horizontal

    #assignage des variables en fonction du tour du joueur
    if tour_joueur_1 :
        grille = grille_1
        bateaux = bateaux1
    else :
        grille = grille_2
        bateaux = bateaux2

    #placment initial des bateaux
    if placement_en_cour :
        if horizontal :

            #vérification que le bateau ne dépasse pas de la grille horizontalement
            if (bateaux[0] + col) <= 10 :
                placer = bateaux.pop(0)
                for index in range(0, placer) :
                    grille[li][col + index] = len(bateaux) + 1
            else :
                print("Le bateau dépasse de la grille !")

        else :
            #vérification que le bateau ne dépasse pas de la grille verticalement
            if (bateaux[0] + li) <= 10 :
                placer = bateaux.pop(0)
                for index in range(0, placer) :
                    grille[li + index][col] = len(bateaux) + 1
            else :
                print("Le bateau dépasse de la grille !")

        affichage_grille()


        #changement de tour si les bateaux du joueur 1 sont placé et passage a la phase suivante si c'est l cas des bateaux du joueur 2
        if not bateaux1 :
            tour_joueur_1 = False
        if not bateaux2 :
            tour_joueur_1 = True
            placement_en_cour = False

    #phase de bombaradage des bateaux
    else :
        print("JEU")



    


"""================PROGRAMME PRINCIPAL================"""

fen=Tk()
fen.geometry ("606x702")
fen.title ("Bataille Navale")
fen.bind('<Button-1>',coordonnees)
fen.bind('<Button-3>',direction)
Zone=Canvas(fen,width=606,height=702,bg="grey")
Zone.place(x=0,y=0)


initialisation()
affichage_grille()
dessin_grille()
#while partie_en_cour :
    


fen.mainloop()