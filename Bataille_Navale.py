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
    placement1_fini : Boolean indiquant si le joueur 1 a finis de placer ses bateaux 
    saisie : Boolean indiquant au fonctions associés aux clics de la souris si elle peuvent fonctionner
    """
    global grille_1 
    global grille_2
    global tour_joueur_1
    global partie_en_cour
    global placement_en_cour
    global bateaux1
    global bateaux2
    global horizontal
    global placement1_fini
    global saisie

    grille_1 = [[0] * 10 for x in range(10)]
    grille_2 = [[0] * 10 for x in range(10)]
    tour_joueur_1 = True
    partie_en_cour = True
    placement_en_cour = True
    bateaux1 = [5,4,3,3,2]
    bateaux2 = [5,4,3,3,2]
    horizontal = True
    placement1_fini = False
    saisie = True

def dessin_grille() :
    """
    Dessin des lignes verticales et horizontale de la grille dans la fenêtre de jeu à l'aide de tkinter.

    Pas de paramètre d'entrée ou de sortie.
    """
    #remplissage du fond en gris
    Zone.create_rectangle (0, 0, 606, 702, fill="grey")
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

    0 : vide
    1 : bateau 1X2
    2 : bateau 1X3
    3 : bateau 1X3
    4 : bateau 1X4
    5 : bateau 1X5
    6 : bombe raté
    7 : bombe touché

    Cette fonction est surtout présente pour des raisons de tests
    """
    #vérification du tour
    if tour_joueur_1 :
        grille = grille_2
    else :
        grille = grille_1

    #affichage dans la console des 10 lignes de la matrice
    for index in range(10) :
        print(grille[index])
    print("")

def direction(event):
    """
    Change la direction de placement du bateau en vertical ou horizontal en fonction de l'inverse du boolean associé a cet aspect is la saisie est activée

    Pas de paramètres d'entrée ou de sortie
    """
    global horizontal
    global saisie

    if saisie : # vérifie si la saisie est activée
        horizontal = not horizontal
        if horizontal :
            print("Horizontal")
        else :
            print("vertical")

def coordonnees(event) :
    """
    Cette fonction est appelé à chaque clic et calcul la case choisie a partir des coordonnées de la souris si la saisie est activée

    Pas de paramètre en entrée ou sortie.
    """
    if saisie : # vérifie si la saisie est activée
        col = event.x // 60 #détermination de la colonne avec une division euclidienne des coordonnées verticales par la taille des cases
        li = (event.y-100) // 60 #détermination de la ligne avec une division euclidienne des coordonnées horizontales par la taille des cases en prenant en compte la marge de 100 pixels pour la ligne

        if li >= 0 : #verification que le clic est dans la grille et non la marge en haut
            placement(li, col)

        else :  #message d'erreur si hors de la grille
            print("Clic en dehors de la grille")

def placement(li, col) :
    """
    Fonction de placement, gère le positionnement des bateaux tant que la phase de placement est active puis le bombardage sur la grille ennemie

    Prends en paramètre la ligne et la colonne choisie, ne retourne rien. 
    """
    global tour_joueur_1
    global placement1_fini
    global placement_en_cour
    global horizontal

    #phase de placement initial des bateaux
    if placement_en_cour :

        #assignage des variables en fonction du tour du joueur
        if tour_joueur_1 :
            grille = grille_1
            bateaux = bateaux1
        else :
            grille = grille_2
            bateaux = bateaux2

        if horizontal : #si le placment est horizontal
            if (bateaux[0] + col) <= 10 : #vérification que le bateau ne dépasse pas de la grille horizontalement
                champs_libre = True

                #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                for index in range(0, bateaux[0]) :
                        if grille[li][col + index] != 0 :
                            champs_libre = False
                if champs_libre :

                    #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux[0]) :
                        grille[li][col + index] = len(bateaux) 
                    dessin_bateaux(li,col, True, bateaux.pop(0)) 
                else :
                    print("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                print("Le bateau dépasse de la grille !")

        else : #si le placment est vertical
            if (bateaux[0] + li) <= 10 : #vérification que le bateau ne dépasse pas de la grille verticalement
                champs_libre = True

                #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                for index in range(0, bateaux[0]) :
                        if grille[li + index][col] != 0 :
                            champs_libre = False
                if champs_libre :
                    #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux[0]) :
                        grille[li + index][col] = len(bateaux) 
                    dessin_bateaux(li,col, False, bateaux.pop(0))
                else :
                    print("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                print("Le bateau dépasse de la grille !")

        #changement de tour si les bateaux du joueur 1 sont placé et passage a la phase suivante si c'est l cas des bateaux du joueur 2
        if not bateaux1 and not placement1_fini:
            tour_joueur_1 = False
            placement1_fini = True
            dessin_grille()
        if not bateaux2 :
            tour_joueur_1 = True
            placement_en_cour = False
            dessin_grille()

    else : #phase de bombaradage des bateaux

        #assignage du tableau en fonction du tour du joueur
        if tour_joueur_1 :
            grille = grille_2
        else :
            grille = grille_1

        #vérification de l'etat de la case et 
        if grille[li][col] == 0 :
            grille[li][col] = 6
            dessin_bombe(li, col, False)   
        elif grille[li][col] == 6 or grille[li][col] == 7 :
            print("Vous avez déja bombardé cette case")
        else :
            grille[li][col] = 7
            dessin_bombe(li, col, True)    

        tour_joueur_1 = not tour_joueur_1
        dessin_autre_joueur()

def dessin_autre_joueur() :
    """
    Dessine dans l'interface graphique la grille de l'autre joueur lors des changement de tour,

    Pas de paramètre d'entrée ou de sortie
    """
    dessin_grille()
    #assignage du tableau en fonction du tour du joueur
    if tour_joueur_1 :
        grille = grille_2
        print("TOUR JOUEUR 1")
    else :
        grille = grille_1
        print("TOUR JOUEUR 2")

    for li in range(len(grille)) :
        for col in range (len(grille[li])) :
            if grille[li][col] == 6 :
                dessin_bombe(li, col, False)  
            elif grille[li][col] == 7 :
                dessin_bombe(li, col, True) 

def dessin_bateaux(li,col, horizontal, long) :
    """
    Dessine le bateaux selon les paramètres d'entré suivants :

    li : int indiquant la ligne du bateaux
    col : int indiquant la colone du bateaux
    horizontal : Boolean indiquant l'horizontalité ou non du bateau
    long : int indiquant la longueur du bateau
    """
    if horizontal :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61 + (60*(long-1)), li*60 + 157, width=2 ,outline="black",fill="cyan")
    else :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157 + (60*(long-1)), width=2 ,outline="black",fill="cyan")
    Zone.update ()

def dessin_bombe(li, col, touche) :
    if touche :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157, width=2 ,outline="black",fill="red")
    else :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157, width=2 ,outline="black",fill="white")


"""================PROGRAMME PRINCIPAL================"""

fen=Tk()
fen.geometry ("606x702")
fen.title ("Bataille Navale")
fen.bind('<Button-1>',coordonnees) #assignage de la fontion coordonnees au clic gauche
fen.bind('<Button-3>',direction) #assignage de la fonction direction au clic droit
Zone=Canvas(fen,width=606,height=702,bg="grey") #création du fond gris servant de référentiel pour les coordonnées
Zone.place(x=0,y=0) #initialisation du référentiel pour les coordonnées

initialisation()
dessin_grille()



fen.mainloop()