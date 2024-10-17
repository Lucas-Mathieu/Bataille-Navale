from tkinter import *
import time
import random
import os

def initialisation() :
    """
    Initialisation des varibles globales nécessaires au fonctionement de jeu, pas de paramètres d'entré ou de sortie.

    Variables globales :
        grille_1, grille_2: Matrices 10x10 représentant la grille de chaque joueur. 0 indique une case vide.
        tour_joueur_1: Booléen indiquant si c'est le tour du joueur 1. Si faux, c'est le tour du joueur 2.
        placement_en_cour: Booléen indiquant si c'est la phase de placement des bateaux.
        bateaux1, bateaux2: Listes d'entiers indiquant la longueur des bateaux de chaque joueur.
        horizontal: Booléen indiquant si le bateau à placer est horizontal (True) ou vertical (False).
        placement1_fini: Booléen indiquant si le joueur 1 a fini de placer ses bateaux.
        saisie: Booléen indiquant si les fonctions associées aux clics de souris peuvent opérer.
        opposant: Entier définissant le type d'opposant: 0 pour joueur, 1 pour IA facile, 2 pour IA difficile.
        mode_chasse: Booléen indiquant si l'IA est en mode chasse.
        coord_bateau_touché: Tuple avec les coordonnées du bateau touché par l'IA.
        direction_IA: Entier indiquant la direction que l'IA difficile cible: 0 = haut, 1 = bas, 2 = gauche, 3 = droite.
    """
    global grille_1, grille_2, tour_joueur_1 #var jeu
    global bateaux1, bateaux2, horizontal, placement1_fini, saisie, placement_en_cour #var placement via souris
    global opposant, mode_chasse, coord_bateau_touché, direction_IA #var IA

    grille_1 = [[0] * 10 for x in range(10)]
    grille_2 = [[0] * 10 for x in range(10)]
    tour_joueur_1 = True
    placement_en_cour = True
    bateaux1 = [5,4,3,3,2]
    bateaux2 = [5,4,3,3,2]
    horizontal = True
    placement1_fini = False
    saisie = True
    opposant = 0
    mode_chasse = False
    coord_bateau_touché = (-1,-1)
    direction_IA = 0

def activation_ia_facile() :
    """
    Active ou désactive le mode IA facile, pas de paramètres d'entré ou de sortie.

    Variables Globales:
        opposant: Entier définissant le type d'opposant. 0 pour joueur, 1 pour IA facile.
        tour_joueur_1: Booléen indiquant si c'est le tour du joueur 1. Si faux, c'est le tour du joueur 2.
    """

    global opposant
    global tour_joueur_1

    if tour_joueur_1 : #ne change que si c'est le tour du joueur 1
        if opposant == 1 : #active l'IA si elle n'est pas déjà sélectionnée
            opposant = 0
            dessin_message("IA désactivée")
        else : #désactive l'IA si elle est déjà sélectionnée
            opposant = 1
            dessin_message("IA mode facile activé")
    else :
        dessin_message("Impossible de changer l'opposant lors de son tour")

def activation_ia_difficile() :
    """
    Active ou désactive le mode IA difficile, pas de paramètres d'entré ou de sortie.

    Variables Globales:
        opposant: Entier définissant le type d'opposant. 0 pour joueur, 2 pour IA difficile.
        tour_joueur_1: Booléen indiquant si c'est le tour du joueur 1. Si faux, c'est le tour du joueur 2.
    """
    
    global opposant
    global tour_joueur_1

    if tour_joueur_1 : #ne change que si c'est le tour du joueur 1
        if opposant == 2 : #active l'IA si elle n'est pas déjà sélectionnée
            opposant = 0
            dessin_message("IA désactivée")

        else : #désactive l'IA si elle est déjà sélectionnée
            opposant = 2
            dessin_message("IA mode difficile activé")
    else :
        dessin_message("Impossible de changer l'opposant lors de son tour")

def affichage_grille() :
    """
    Affichage de la grille du jouer dont c'est actuellement le tour dans la console, pas de paramètre d'entré ou de sortie.

    Légende des case :
        0 : vide
        1 : Torpilleur (2 cases)
        2 : Sous-marin (3 cases)
        3 : Contre torpilleur (3 cases)
        4 : Croiseur (4 cases)
        5 : Porte-avions (5 cases)
        6 : bombe raté
        7 : bombe touché

    Cette fonction est principalement utilisée pour des tests.
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
    Change la direction de placement du bateau en fonction de l'inverse du booléen associé, si la saisie est activée.

    Variables Globales:
        horizontal: Booléen indiquant si la direction actuelle est horizontale si True, verticale dans le cas contraire.
        saisie: Booléen indiquant si la saisie est permise par l'état actuel du jeu

    Pas de paramètres d'entrée (sauf l'événement imposé par tkinter pour les appels de fonction liés à des touches, bien qu'il ne soit pas utilisé) ou de sortie.
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
    Cette fonction est appelée à chaque clic et calcule la case choisie à partir des coordonnées de la souris si la saisie est activée.
    
    Variables Globales:
        saisie: Booléen indiquant si les fonctions associées aux clics de souris peuvent fonctionner.
        opposant: Entier définissant le type d'opposant: 0 pour joueur, 1 pour IA facile, 2 pour IA difficile.
    
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
    global mode_chasse
    global coord_bateau_touché
    global direction_IA

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
                        grille_1[li + index][col] = len(bateaux1) 
                    dessin_bateaux(li,col, False, bateaux1.pop(0))
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

        if not bateaux2 :
            saisie = False
            tour_joueur_1 = True
            placement_en_cour = False
            dessin_grille()
            dessin_message("Veillez choisir une case à bombarder.")
            saisie = True

    else : #phase de bombardage

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

            if opposant == 1 : #IA mode facile
                IA_facile(noms_bateaux)
                        
            else : #IA mode difficile
                coulé = False
                while not coulé :
                    if not mode_chasse :
                        coulé = IA_difficile_placage_semi_random(grille_1)
                    else :
                        li, col = coord_bateau_touché
                        directions_ciblage = [(li, col-1), (li, col+1), (li-1, col), (li+1, col)]
                        coulé = False

                        while not coulé:
                            li, col = directions_ciblage[direction_IA]
                            if 0 <= li < 10 and 0 <= col < 10:  # Vérification des limites de la grille

                                if grille_1[li][col] == 6 :
                                    direction_IA += 1
                                    if direction_IA == 4:
                                        direction_IA = 0
                                        mode_chasse = False
                                        coulé = True
                                        IA_difficile_placage_semi_random(grille_1)

                                elif grille_1[li][col] == 0:
                                    time.sleep(0.5)
                                    grille_1[li][col] = 6
                                    coulé = True
                                    dessin_message("L'IA a raté...")
                                    dessin_bombe(li, col, False)
                                    time.sleep(1)
                                    direction_IA += 1
                                    if direction_IA == 4:
                                        direction_IA = 0
                                        mode_chasse = False

                                else:
                                    time.sleep(0.5)
                                    bateau_touché = grille_1[li][col]
                                    grille_1[li][col] = 7
                                    dessin_bombe(li, col, True)

                                    # Mettre à jour directions_ciblage avec de nouvelles coordonnées dans la même direction
                                    if direction_IA == 0:
                                        directions_ciblage[direction_IA] = (li, col-1)
                                    elif direction_IA == 1:
                                        directions_ciblage[direction_IA] = (li, col+1)
                                    elif direction_IA == 2:
                                        directions_ciblage[direction_IA] = (li-1, col)
                                    elif direction_IA == 3:
                                        directions_ciblage[direction_IA] = (li+1, col)

                                    bateau_en_vie = False

                                    # Parcourt la matrice et vérifie si le bateau touché a entièrement coulé
                                    for ligne in grille_1:
                                        if bateau_touché in ligne:
                                            bateau_en_vie = True

                                    if bateau_en_vie:
                                        dessin_message("L'IA a touché un bateau !")
                                    else:
                                        dessin_message("Le " + noms_bateaux[bateau_touché - 1] + " a Coulé !")
                                        direction_IA = 0
                                        coulé = True
                                        mode_chasse = False
                                        bateaux_coulé = True
                                        
                                        # Parcourt la matrice et vérifie s'il reste au moins un bateau
                                        for ligne in grille_1:
                                            if any(cell in ligne for cell in [1, 2, 3, 4, 5]):
                                                bateaux_coulé = False

                                        if bateaux_coulé:  # Si plus de bateaux : victoire
                                            victoire(False)
                                            
                                        time.sleep(1)
                                        IA_difficile_placage_semi_random(grille_1)
                                    time.sleep(1)

                            else:
                                direction_IA += 1
                                if direction_IA == 4: # sors du mode chasse si toutes les directions ont été essayées
                                    direction_IA = 0
                                    mode_chasse = False  
                                    coulé = True
                                    IA_difficile_placage_semi_random(grille_1)

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

def IA_facile(noms_bateaux) :
    """
    Fonction de l'IA facile qui effectue des tirs aléatoires sur la grille de jeu du joueur.

    Prend en paramètre la liste des noms de bateaux.

    Variables Globales:
        grille_1: Matrice 10x10 représentant la grille de jeu du joueur 1.
    """

    global grille_1

    coulé = False
    while not coulé : #tant qu'aucun tir n'a manqué, continuer de jouer
        li = random.randint(0, 9)
        col = random.randint(0, 9)

        if grille_1[li][col] == 0 : #si case vide
            time.sleep(0.5)
            grille_1[li][col] = 6
            coulé = True
            dessin_message("L'IA a raté...")
            dessin_bombe(li, col, False)
            time.sleep(1)

        elif grille_1[li][col] in [1, 2, 3, 4, 5]: #si la case abrite un bateau
            bateau_touché = grille_1[li][col]
            grille_1[li][col] = 7
            bateau_en_vie = False

            for ligne in range(len(grille_1)) : #parcour la matrice et vérifie si le bateau touché a entièrement coulé
                if bateau_touché in grille_1[ligne] :
                    bateau_en_vie = True

            if bateau_en_vie :
                time.sleep(0.5)
                dessin_message("L'IA a touché un bateau !")
                dessin_bombe(li, col, True)
                time.sleep(0.75)
            else :
                dessin_message("Le " + noms_bateaux[bateau_touché - 1] +" a Coulé !")
                bateaux_coulé = True
                for li in range(len(grille_1)) : #parcour la matrice et vérifie si il reste au moins un bateau
                    if any(cell in grille_1[li] for cell in [1, 2, 3, 4, 5]) :
                        bateaux_coulé = False
                if bateaux_coulé : #si plus de bateaux : victoire
                    victoire(False)

def IA_difficile_placage_semi_random(grille) :
    """
    Fonction de l'IA difficile qui effectue des tirs semi-aléatoires sur la grille de jeu en ciblant les cases impaires.

    Prend en paramètre la grille de jeu.

    Variables Globales:
        mode_chasse: Booléen indiquant si l'IA est en mode chasse.
        coord_bateau_touché: Tuple avec les coordonnées du bateau touché par l'IA.
    """
    global mode_chasse
    global coord_bateau_touché

    #choisi une case au hasard
    li = random.randint(0, 9)
    col = random.randint(0, 9)

    if (li + col) % 2 == 1 : #on ne cible que les cases impaires 
    
        if grille[li][col] == 0 : #si la case est vide
            time.sleep(0.5)
            grille[li][col] = 6
            dessin_message("L'IA a raté...")
            dessin_bombe(li, col, False)
            time.sleep(1)
            return True #on stop la boucle while
        elif grille[li][col] in [1, 2, 3, 4, 5]:
            time.sleep(0.5)
            grille[li][col] = 7 #bombe touchée
            mode_chasse = True #déstruction bateau priorisée
            coord_bateau_touché = (li, col)
            dessin_message("L'IA a touché un bateau !")
            dessin_bombe(li, col, True)
            time.sleep(1)

def victoire(tour_joueur1) :
    """
    Affiche le message de victoire en fonction du joueur gagnant.

    Variables Globales:
        saisie: Booléen indiquant si les fonctions associées aux clics de souris peuvent fonctionner.
        tour_joueur1: Booléen indiquant si c'est le tour du joueur 1. Si faux, c'est le tour du joueur 2.
    """

    global saisie

    #vérification du tour
    if tour_joueur1 :
        gagnant = "Joueur 1"
    else :
        gagnant = "Joueur 2"

    dessin_message("Le " + gagnant + " a gagné la partie !")
    saisie = False

def dessin_grille() :
    """
    Dessine les lignes verticales et horizontales de la grille dans la fenêtre de jeu à l'aide de tkinter.
    
    Pas de paramètre d'entrée ou de sortie.
    """

    Zone.create_rectangle (0, 100, 606, 702, fill="grey", outline="grey") #remplissage du fond en gris

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
    """
    Affiche dans l'interface graphique le tour du joueur en cours.

    Paramètres:
        joueur1: Booléen indiquant si c'est le tour du joueur 1. Si faux, c'est le tour du joueur 2.
    """

    #vérification du tour
    if joueur1 :
        txt = "Joueur 1"
    else :
        txt = "Joueur 2"
 
    Zone.create_rectangle (0, 0, 606, 50, fill="grey", outline="grey") #efface le message de tour précedant
    Zone.create_text(310, 25, text="Tour du " + txt, font=("Arial", 14), fill="black") #déssine le message de tour actuel

def dessin_message(txt):
    Zone.create_rectangle (0, 50, 606, 96, fill="grey", outline="grey") #efface le message précedant
    Zone.create_text(310, 75, text=txt, font=("Arial", 14), fill="black") #déssine le message
    Zone.update () #met a jour la fenêtre pour que les changements soient déssinés

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

    #parcour de la matrice afin de déssiner les bombes si présente en fonction de si elles ont touché un bateau ou non
    for li in range(len(grille)) :
        for col in range (len(grille[li])) :
            if grille[li][col] == 6 :
                dessin_bombe(li, col, False)  
            elif grille[li][col] == 7 :
                dessin_bombe(li, col, True) 

def dessin_bateaux(li,col, horizontal, long) :
    """
    Dessine le bateau selon les paramètres d'entrée suivants:
    
    Paramètres:
        li: int indiquant la ligne du bateau.
        col: int indiquant la colonne du bateau.
        horizontal: Boolean indiquant l'horizontalité ou non du bateau.
        long: int indiquant la longueur du bateau.
    """

    if horizontal :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61 + (60*(long-1)), li*60 + 157, width=2 ,outline="black",fill="cyan")
    else :
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157 + (60*(long-1)), width=2 ,outline="black",fill="cyan")
    Zone.update () #met a jour la fenêtre pour que les changements soient déssinés

def dessin_bombe(li, col, touche) :
    """
    Dessine une bombe sur la grille, rouge si elle touche un bateau, blanche sinon.
    
    Paramètres:
        li: int indiquant la ligne de la bombe.
        col: int indiquant la colonne de la bombe.
        touche: Boolean indiquant si la bombe a touché un bateau (True) ou non (False).
    """

    if touche : #si la bombe touche un bateau
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157, width=2 ,outline="black",fill="red")
    else : #si la bombe rate
        Zone.create_oval(col*60 + 6 , li*60 + 102, col*60 + 61, li*60 + 157, width=2 ,outline="black",fill="white")
    Zone.update () #met a jour la fenêtre pour que les changements soient déssinés

def sauvegarde() :
    """
    Sauvegarde les données de la partie dans un fichier texte..
    """
    global grille_1, grille_2, tour_joueur_1, placement_en_cour
    global bateaux1, bateaux2, horizontal, placement1_fini, saisie, opposant
    global mode_chasse, coord_bateau_touché, direction_IA

    # Obtenir le répertoire courant
    current_directory = os.path.dirname(os.path.abspath(__file__))
    fichier = os.path.join(current_directory, "sauvegarde.txt")

    #enregistrement de toutes les variables globales
    if not placement_en_cour :
        with open(fichier, 'w') as f:
            f.write(f"grille_1: {grille_1}\n")
            f.write(f"grille_2: {grille_2}\n")
            f.write(f"tour_joueur_1: {tour_joueur_1}\n")
            f.write(f"placement_en_cour: {placement_en_cour}\n")
            f.write(f"bateaux1: {bateaux1}\n")
            f.write(f"bateaux2: {bateaux2}\n")
            f.write(f"horizontal: {horizontal}\n")
            f.write(f"placement1_fini: {placement1_fini}\n")
            f.write(f"saisie: {saisie}\n")
            f.write(f"opposant: {opposant}\n")
            f.write(f"mode_chasse: {mode_chasse}\n")
            f.write(f"coord_bateau_touché: {coord_bateau_touché}\n")
            f.write(f"direction_IA: {direction_IA}\n")
    else : 
        dessin_message("Vous devez placer les bateaux pour pouvoir sauvegarder.")

def chargement():
    """ 
    Charge les données de la partie à partir du fichier texte.
    """
    global grille_1, grille_2, tour_joueur_1, placement_en_cour
    global bateaux1, bateaux2, horizontal, placement1_fini, saisie, opposant
    global mode_chasse, coord_bateau_touché, direction_IA

    # Obtenir le répertoire courant
    current_directory = os.path.dirname(os.path.abspath(__file__))
    fichier = os.path.join(current_directory, "sauvegarde.txt")

    # Chargement de toutes les variables globales
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            lines = f.readlines()
            grille_1 = eval(lines[0].split(": ")[1].strip())
            grille_2 = eval(lines[1].split(": ")[1].strip())
            tour_joueur_1 = eval(lines[2].split(": ")[1].strip())
            placement_en_cour = eval(lines[3].split(": ")[1].strip())
            bateaux1 = eval(lines[4].split(": ")[1].strip())
            bateaux2 = eval(lines[5].split(": ")[1].strip())
            horizontal = eval(lines[6].split(": ")[1].strip())
            placement1_fini = eval(lines[7].split(": ")[1].strip())
            saisie = eval(lines[8].split(": ")[1].strip())
            opposant = eval(lines[9].split(": ")[1].strip())
            mode_chasse = eval(lines[10].split(": ")[1].strip())
            coord_bateau_touché = eval(lines[11].split(": ")[1].strip())
            direction_IA = eval(lines[12].split(": ")[1].strip())
        dessin_tour(tour_joueur_1)
        dessin_autre_joueur()
        dessin_message("Veillez choisir une case à bombarder.")
    else:
        dessin_message("Aucune sauvegarde trouvée.")

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

sauvegarder=Button(fen, text="Sauvegarder",command=sauvegarde)
sauvegarder.place(x=527, y=5)

charger=Button(fen, text="Charger",command=chargement)
charger.place(x=527, y=35)

initialisation()
dessin_grille()
dessin_tour("Joueur 1")
dessin_message("Veuillez placer le Porte-avions (5 cases)")

fen.mainloop()