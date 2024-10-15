

def initialisation() :
    """
    Initialisation des varibles globales nécessaires au fonctionement de jeu, pas de paramètres d'entré ou de sortie.

    grille_1/2 : Matrice de 10 x 10 représentant la grille de jeu de chaque joueur
    tour_joueur_1 : Boolean indiquant si c'est le tour du joueur 1 ou non (et par éxtension si c'est celui du joueur 2)
    partie_en_cour : Boolean indiquant si la partie est en cour ou non
    """
    global grille_1 
    global grille_2
    global tour_joueur_1
    global partie_en_cour

    grille_1 = [[1] * 10 for i in range(10)]
    grille_2 = [[2] * 10 for i in range(10)]
    tour_joueur_1 = True
    partie_en_cour = True

def affichage_grille() :
    """
    Affichage de la grille du jouer dont c'est actuellement le tour, pas de paramètre d'entré ou de sortie.
    """
    if tour_joueur_1 :
        grille = grille_1
    else :
        grille = grille_2

    for x in range(10) :
        print(grille[x])
    print("")


"""================PROGRAMME PRINCIPAL================"""

initialisation()
affichage_grille()
#while partie_en_cour :
