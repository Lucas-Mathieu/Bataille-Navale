from tkinter import *
import time
import random

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
    opposant : int définissant l'opposant : 0 = joueur, 1 : IA facile, 2 : IA difficile
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
    global opposant

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
    opposant = 0

def activation_ia_facile() :
    global opposant
    global tour_joueur_1

    if tour_joueur_1 :
        if opposant == 1 :
            opposant = 0
            dessin_message("IA désactivée")
        else :
            opposant = 1
            dessin_message("IA mode facile activé")
    else :
        dessin_message("Impossible de changer l'opposant lors de son tour")

def activation_ia_difficile() :
    global opposant
    global tour_joueur_1

    if tour_joueur_1 :
        if opposant == 2 :
            opposant = 0
            dessin_message("IA désactivée")

        else :
            opposant = 2
            dessin_message("IA mode difficile activé")
    else :
        dessin_message("Impossible de changer l'opposant lors de son tour")

def affichage_grille() :
    """
    Affichage de la grille du jouer dont c'est actuellement le tour dans la console, pas de paramètre d'entré ou de sortie.

    0 : vide
    1 : Torpilleur (2 cases)
    2 : Sous-marin (3 cases)
    3 : Contre torpilleur (3 cases)
    4 : Croiseur (4 cases)
    5 : Porte-avions (5 cases)
    6 : bombe raté
    7 : bombe touché

    Cette fonction est surtout présente pour des raisons de tests
    """
    #vérification du tour
    if tour_joueur_1 :
        grille = grille_2
    else :
        grille = grille_2

    #affichage dans la console des 10 lignes de la matrice
    for ligne in grille :
        print(ligne)
    print("")

def direction(event):
    """
    Change la direction de placement du bateau en vertical ou horizontal en fonction de l'inverse du boolean associé a cet aspect is la saisie est activée

    Pas de paramètres d'entrée (sauf event imposé par tkinter pour les appels de fonction lié a des touches malgrès qu'il ne soit pas utilisé) ou de sortie
    """
    global horizontal
    global saisie

    if saisie : # vérifie si la saisie est activée
        horizontal = not horizontal
        if horizontal :
            dessin_message("Placement horizontal")
        else :
            dessin_message("Placement vertical")

def coordonnees(event) :
    """
    Cette fonction est appelé à chaque clic et calcul la case choisie a partir des coordonnées de la souris si la saisie est activée

    Pas de paramètre en entrée ou sortie.
    """
    global saisie
    global opposant

    if saisie :
        if saisie : # vérifie si la saisie est activée
            col = event.x // 60 #détermination de la colonne avec une division euclidienne des coordonnées verticales par la taille des cases
            li = (event.y-100) // 60 #détermination de la ligne avec une division euclidienne des coordonnées horizontales par la taille des cases en prenant en compte la marge de 100 pixels pour la ligne

            if li >= 0 : #verification que le clic est dans la grille et non la marge en haut
                if opposant == 0 :
                    placement_joueurs(li, col)
                else :
                    placement_ia(li, col)

            else :  #message d'erreur si hors de la grille
                dessin_message("Clic en dehors de la grille")

def placement_joueurs(li, col) :
    """
    Fonction de placement, gère le positionnement des bateaux tant que la phase de placement est active puis le bombardage sur la grille ennemie

    Prends en paramètre la ligne et la colonne choisie, ne retourne rien. 
    """
    global tour_joueur_1
    global placement1_fini
    global placement_en_cour
    global horizontal
    global saisie

    dessin_message("")
    noms_bateaux = ["Torpilleur (2 cases)", "Sous-marin (3 cases)", "Contre torpilleur (3 cases)", "Croiseur (4 cases)", "Porte-avions (5 cases)"]

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

                for index in range(0, bateaux[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                        if grille[li][col + index] != 0 :
                            champs_libre = False

                if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux[0]) :
                        grille[li][col + index] = len(bateaux) 
                    dessin_bateaux(li,col, True, bateaux.pop(0))

                    dessin_message("Veuillez placer le " + noms_bateaux[len(bateaux)-1])

                else :
                    dessin_message("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                dessin_message("Le bateau dépasse de la grille !")

        else : #si le placment est vertical
            if (bateaux[0] + li) <= 10 : #vérification que le bateau ne dépasse pas de la grille verticalement
                champs_libre = True

                for index in range(0, bateaux[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                        if grille[li + index][col] != 0 :
                            champs_libre = False

                if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux[0]) :
                        grille[li + index][col] = len(bateaux) 
                    dessin_bateaux(li,col, False, bateaux.pop(0))
                else :
                    dessin_message("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                dessin_message("Le bateau dépasse de la grille !")

        if not bateaux1 and not placement1_fini: #changement de tour si les bateaux du joueur 1 sont placé et passage a la phase suivante si c'est l cas des bateaux du joueur 2
            tour_joueur_1 = False
            placement1_fini = True
            dessin_message("Placement des bateaux du joueur 1 fini")
            saisie = False
            time.sleep(0.7)
            dessin_message("")
            dessin_grille()
            dessin_tour(tour_joueur_1)
            dessin_message("Veuillez placer le Porte-avions (5 cases)")
            saisie = True
        if not bateaux2 :
            tour_joueur_1 = True
            placement_en_cour = False
            dessin_message("Placement des bateaux du joueur 2 fini")
            saisie = False
            time.sleep(0.7)
            dessin_message("")
            dessin_grille()
            dessin_tour(tour_joueur_1)
            dessin_message("Veillez choisir une case à bombarder.")
            saisie = True

    else : #phase de bombaradage des bateaux

        #assignage du tableau en fonction du tour du joueur
        if tour_joueur_1 :
            grille = grille_2
        else :
            grille = grille_1

        #vérification de l'etat de la case et assignage de son nouvel état après bombardement
        if grille[li][col] == 0 : #bombardement raté si la case est vide
            saisie = False
            grille[li][col] = 6
            dessin_bombe(li, col, False)
            dessin_message("Coulé...")
            time.sleep(0.5)
            tour_joueur_1 = not tour_joueur_1
            dessin_tour(tour_joueur_1)
            dessin_autre_joueur()
            dessin_message("Veillez choisir une case à bombarder.")
            saisie = True

        elif grille[li][col] == 6 or grille[li][col] == 7 : #message d'erreur si la case à déjà été bombardée
            dessin_message("Vous avez déja bombardé cette case")

        else : #bombardement touché car dernier cas possible : case occupée par bateau
            bateau_touché =  grille[li][col]
            grille[li][col] = 7
            dessin_bombe(li, col, True)

            bateau_en_vie = False
            for li in range(len(grille)) : #parcour la matrice et vérifie si le bateau touché a entièrement coulé
                if bateau_touché in grille[li] :
                    bateau_en_vie = True

            if bateau_en_vie :
                dessin_message("Touché !")
            else :
                dessin_message("Le " + noms_bateaux[bateau_touché - 1] +" a Coulé !")
                bateaux_coulé = True
                for li in range(len(grille)) : #parcour la matrice et vérifie si il reste au moins un bateau
                    if any(cell in grille[li] for cell in [1, 2, 3, 4, 5]) :
                        bateaux_coulé = False
                if bateaux_coulé : #si plus de bateaux : victoire
                    victoire(tour_joueur_1)

def placement_ia(li, col) :
    global tour_joueur_1
    global placement1_fini
    global placement_en_cour
    global horizontal
    global saisie

    dessin_message("")
    noms_bateaux = ["Torpilleur (2 cases)", "Sous-marin (3 cases)", "Contre torpilleur (3 cases)", "Croiseur (4 cases)", "Porte-avions (5 cases)"]

    #phase de placement initial des bateaux
    if placement_en_cour :

        #assignage des variables en fonction du tour du joueur
        if horizontal : #si le placment est horizontal
            if (bateaux1[0] + col) <= 10 : #vérification que le bateau ne dépasse pas de la grille horizontalement
                champs_libre = True

                for index in range(0, bateaux1[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                        if grille_1[li][col + index] != 0 :
                            champs_libre = False

                if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux1[0]) :
                        grille_1[li][col + index] = len(bateaux1) 
                    dessin_bateaux(li,col, True, bateaux1.pop(0))

                    dessin_message("Veuillez placer le " + noms_bateaux[len(bateaux1)-1])

                else :
                    dessin_message("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                dessin_message("Le bateau dépasse de la grille !")

        else : #si le placment est vertical
            if (bateaux1[0] + li) <= 10 : #vérification que le bateau ne dépasse pas de la grille verticalement
                champs_libre = True

                for index in range(0, bateaux1[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                        if grille_1[li + index][col] != 0 :
                            champs_libre = False

                if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                    for index in range(0, bateaux1[0]) :
                        grille_1[li + index][col] = len(bateaux) 
                    dessin_bateaux(li,col, False, bateaux.pop(0))
                else :
                    dessin_message("Le bateau est bloqué par un autre bateau déjà placé !")
            else :
                dessin_message("Le bateau dépasse de la grille !")
                
        if not bateaux1 and not placement1_fini: #changement de tour si les bateaux du joueur 1 sont placé et passage a la phase suivante si c'est l cas des bateaux du joueur 2
            tour_joueur_1 = False
            placement1_fini = True
            dessin_message("Placement des bateaux du joueur 1 fini")
            saisie = False
            time.sleep(0.7)
            saisie = True
            dessin_message("")
            dessin_grille()

            while bateaux2 :
                li = random.randint(0, 9)
                col = random.randint(0, 9)
                hor = random.randint(0, 1) 
                if hor == 0 :
                    hor = True
                else :
                    hor = False
                if hor : #si le placment est horizontal
                    if (bateaux2[0] + col) <= 10 : #vérification que le bateau ne dépasse pas de la grille horizontalement
                        champs_libre = True

                        for index in range(0, bateaux2[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                                if grille_2[li][col + index] != 0 :
                                    champs_libre = False

                        if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                            for index in range(0, bateaux2[0]) :
                                grille_2[li][col + index] = len(bateaux2) 
                            bateaux2.pop(0)
                else : #si le placment est vertical
                    if (bateaux2[0] + li) <= 10 : #vérification que le bateau ne dépasse pas de la grille verticalement
                        champs_libre = True

                        for index in range(0, bateaux2[0]) : #vérification qu'un autre bateau ne bloque pas celui qu'on place, je sais que c'est pas beau mais c'est la meilleure idée que j'ai...
                                if grille_2[li + index][col] != 0 :
                                    champs_libre = False

                        if champs_libre : #placement du bateau sans oublier de le retirer de la liste des bateaux a placer
                            for index in range(0, bateaux2[0]) :
                                grille_2[li + index][col] = len(bateaux2) 
                            bateaux2.pop(0)

            affichage_grille()

        if not bateaux2 :
            saisie = False
            tour_joueur_1 = True
            placement_en_cour = False
            dessin_grille()
            dessin_message("Veillez choisir une case à bombarder.")
            saisie = True

    else :
        #vérification de l'etat de la case et assignage de son nouvel état après bombardement
        if grille_2[li][col] == 0 : #bombardement raté si la case est vide
            saisie = False
            grille_2[li][col] = 6
            dessin_bombe(li, col, False)
            dessin_message("Coulé...")
            time.sleep(0.5)
            tour_joueur_1 = False
            dessin_tour(tour_joueur_1)
            dessin_autre_joueur()

            li = -1
            col = -1
            coulé = False

            if opposant == 1 :
                while not coulé :
                    li = random.randint(0, 9)
                    col = random.randint(0, 9)
                    if grille_1[li][col] == 0 :
                        grille_1[li][col] = 6
                        coulé = True
                        time.sleep(0.5)
                        dessin_message("L'IA a raté...")
                        dessin_bombe(li, col, False)
                        time.sleep(1)
                    elif grille_1[li][col] in [1, 2, 3, 4, 5]:
                        bateau_touché = grille_1[li][col]
                        grille_1[li][col] = 7
                        bateau_en_vie = False

                        for ligne in range(len(grille_1)) : #parcour la matrice et vérifie si le bateau touché a entièrement coulé
                            if bateau_touché in grille_1[ligne] :
                                bateau_en_vie = True

                        if bateau_en_vie :
                            time.sleep(0.5)
                            dessin_message("L'IA a touché !")
                            print(li, col)
                            dessin_bombe(li, col, True)
                            time.sleep(0.75)
                        else :
                            dessin_message("Le " + noms_bateaux[bateau_touché - 1] +" a Coulé !")
                            bateaux_coulé = True
                            for li in range(len(grille_1)) : #parcour la matrice et vérifie si il reste au moins un bateau
                                if any(cell in grille_1[li] for cell in [1, 2, 3, 4, 5]) :
                                    bateaux_coulé = False
                            if bateaux_coulé : #si plus de bateaux : victoire
                                victoire(tour_joueur_1)

                        
            else :
                print("test lol")

            tour_joueur_1 = True
            dessin_tour(tour_joueur_1)
            dessin_autre_joueur()
            saisie = True


        elif grille_2[li][col] == 6 or grille_2[li][col] == 7 : #message d'erreur si la case à déjà été bombardée
            dessin_message("Vous avez déja bombardé cette case")

        else : #bombardement touché car dernier cas possible : case occupée par bateau
            bateau_touché =  grille_2[li][col]
            grille_2[li][col] = 7
            dessin_bombe(li, col, True)

            bateau_en_vie = False
            for li in range(len(grille_2)) : #parcour la matrice et vérifie si le bateau touché a entièrement coulé
                if bateau_touché in grille_2[li] :
                    bateau_en_vie = True

            if bateau_en_vie :
                dessin_message("Touché !")
            else :
                dessin_message("Le " + noms_bateaux[bateau_touché - 1] +" a Coulé !")
                bateaux_coulé = True
                for li in range(len(grille_2)) : #parcour la matrice et vérifie si il reste au moins un bateau
                    if any(cell in grille_2[li] for cell in [1, 2, 3, 4, 5]) :
                        bateaux_coulé = False
                if bateaux_coulé : #si plus de bateaux : victoire
                    victoire(tour_joueur_1)

def victoire(tour_joueur1) :
    global saisie

    if tour_joueur1 :
        gagnant = "Joueur 1"
    else :
        gagnant = "Joueur 2"

    dessin_message("Le " + gagnant + " a gagné la partie !")
    saisie = False

def dessin_grille() :
    """
    Dessin des lignes verticales et horizontale de la grille dans la fenêtre de jeu à l'aide de tkinter.

    Pas de paramètre d'entrée ou de sortie.
    """
    #remplissage du fond en gris
    Zone.create_rectangle (0, 100, 606, 702, fill="grey", outline="grey")
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

def dessin_tour(joueur1) :
    if joueur1 :
        txt = "Joueur 1"
    else :
        txt = "Joueur 2"

    Zone.create_rectangle (0, 0, 606, 50, fill="grey", outline="grey")
    Zone.create_text(310, 25, text="Tour du " + txt, font=("Arial", 14), fill="black")

def dessin_message(txt):
    Zone.create_rectangle (0, 50, 606, 96, fill="grey", outline="grey")
    Zone.create_text(310, 75, text=txt, font=("Arial", 14), fill="black")
    Zone.update ()

def dessin_autre_joueur() :
    """
    Dessine dans l'interface graphique la grille de l'autre joueur lors des changement de tour,

    Pas de paramètre d'entrée ou de sortie
    """
    dessin_grille()
    dessin_message("")
    #assignage du tableau en fonction du tour du joueur
    if tour_joueur_1 :
        grille = grille_2
    else :
        grille = grille_1

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
    Zone.update ()

"""================PROGRAMME PRINCIPAL================"""

fen=Tk() #initialisation de la méthode Tkinter avec l'objet fen
fen.geometry ("606x702") #dimensions de la fenêtre de l'interface graphique
fen.title ("Bataille Navale") #nom de la fenêtre de l'interface graphique
fen.bind('<Button-1>',coordonnees) #assignage de la fontion coordonnees au clic gauche
fen.bind('<Button-3>',direction) #assignage de la fonction direction au clic droit
Zone=Canvas(fen,width=606,height=702,bg="grey") #création du fond gris servant de référentiel pour les coordonnées
Zone.place(x=0,y=0) #initialisation du référentiel pour les coordonnées

slection_ia_facile=Button(fen, text="IA Facile",command=activation_ia_facile)
slection_ia_facile.place(x=5, y=5)

slection_ia_dificile=Button(fen, text="IA Difficile",command=activation_ia_difficile)
slection_ia_dificile.place(x=5, y=35)

initialisation()
dessin_grille()
dessin_tour("Joueur 1")
dessin_message("Veuillez placer le Porte-avions (5 cases)")

fen.mainloop()