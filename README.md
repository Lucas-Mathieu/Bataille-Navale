# BATAILLE NAVALE 1.1

## Notes :
>Les commits initiaux présente un autre compte que l'actuel, 
>Il s'agit de mon ancien compte auquel je n'ai plus accès 
>J'ai malgrès tout pu lier mon git à cet ancien compte en entrant mon email perso sans authentification pour une quelconque raison...

## Exécution :

Ce programe python de bataille navale peut être simplement éxecuté avec un IDE supportant python ou bien en l'ouvrant avec python via la commande suivante dans CMD :

```
python "chemin d'accès du fichier"/Bataille_Navale.py
```

## Usage :

### 2 joueurs :

Une fois éxécuté, une fenêtre Tkinter affichant la grille de jeu s'ouvrira, les joueurs plaçant tour à tour leurs bateaux avant de passer a la phase de bombardement. Les bateaux peuvent êtres placé verticalement en changeant le sens de placement avec clic droit.

Une fois la première phase finie, les joueur bombarde chacun leur tour la grille ennemie afin de couler ses bateaux, un point blanc indique un tir dans le vide et un point rouge un tir ayant touché un bateaux, le 1er joueur a couler tout les bateaux ennemis gagne.

### adversaire IA :

Tant que c'est au tour du joueur 1, ce dernier peut choisir de jouer contre une intelligence artificielle en tant que joueur 2. Il éxiste 2 niveau de difficulté :

- Facile : L'IA attaque de manière aléatoire
- Difficile : L'IA quadrille la zone et achève le bateau une fois trouvé

Le joueur 1 peux a tout moment choisir de repasser en mode 2 joueur en re-cliquant sur le bouton de l'IA active.

### Sauvegarde / chargement :

Une fois la phase de placement des bateaux finie, le jeu offre la possibilité de sauvegarder l'état du jeu pour ensuite pouvoir le charger avec les boutons appopriés en haut a droite de la fenêtre.

## Modules utilisé :

- Tkinter
- Time
- Random
- OS