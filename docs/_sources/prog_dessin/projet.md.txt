(prog_dessin.projet)=

# Projet de dessin

Il est temps de mettre en pratique vos connaissances pour réaliser un dessin libre (avec quelques contraintes).
Le projet peut être réalisé par groupe de 2 ou seul.

## Template

Voici le template (fichier de base) à utiliser pour votre projet. Il vous aidera à structurer correctement votre code.

{download}`Télécharger ici<../data/template_projet_dessin.py>`

## Consignes

Le cahier des charges est le suivant:

- créer un dessin concret (pas juste des formes abstraites) sur un sujet libre
- au moins 4 objets **différents** et **inédits** (3 si élève seul)
- chaque objet est défini à l'aide d'une fonction possédant au minimum 2 paramètres (ex: taille, couleur, position, etc)
- les objets complexes sont découpés en sous-fonctions (ex: un objet "maison" peut être découpé en fonctions "toit", "porte", "fenêtre", etc)
- des boucles sont utilisées pour répéter des instructions
- au moins un élément aléatoire (module `random`) est présent dans votre dessin
- le code est bien structuré (les définitions de fonctions d'abord, puis les appels sont faits en dessous)

Suivre l'ensemble des critères du cahier des charges vous donnera la note de 5.5.
La note maximale est n'atteignable qu'en ajoutant des éléments bonus.

- (bonus) dessiner plus d'objets que le minimum requis
- (bonus) intégrer un objet particulièrement bien réalisé ou complexe
- (bonus) ajouter des animations ou des mécanismes interactifs
- (bonus) utiliser des concepts avancés de programmation non vus en cours

```{admonition} Plagiat et tricherie
:class: attention
Vous n'êtes pas autorisé à simplement copier-coller du code trouvé dans les exercices, sur Internet où dans d'autres groupes.

Il est cependant autorisé de s'inspirer de code d'autrui et de le modifier pour le faire sien. Dans ce cas, il vous est demandé d'ajouter un commentaire dans le code indiquant sa source. Attention, vos objets ne doivent cependant pas être de légères modifications (ex: couleur ou taille) d'un objet présent dans les exercices.

L'utilisation d'IA génératives telles que ChatGPT est autorisée à des fins d'assistance uniquement. Tout code produit par une IA doit être compris par les membres du groupe et indiqué comme tel dans un commentaire.

Enfin, **chaque ligne de code doit pouvoir être expliquée et défendue par le groupe**. L'enseignant se réserve le droit d'interroger le groupe sur leur code en cas de doute. Un membre du groupe peut avoir une note différente de son binôme s'il est révélé que sa contribution est nettement inférieure.
```

## Exemple

L'exemple ci-dessous satisfait toutes les contraintes du cahier des charges.

![projet](../media/dessin_exemple.png)

````{dropdown} Voir le code
```python
from turtle import *
from random import *

speed(0) # Permet d'accélérer le dessin

# -----------------------------------
# Définissez ici toutes vos fonctions
# -----------------------------------

def triangle(d, c):
    # Dessine un triangle équilatéral de longueur d et de couleur c
    down()
    fillcolor(c)
    begin_fill()
    for i in range(3):
        forward(d)
        left(120)
    end_fill()
    up()
        
def rectangle(w, h, c):
    # Dessine un rectangle de largeur w, de hauteur h et de couleur c
    down()
    fillcolor(c)
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()
    up()
        
def montagne(d, c):
    # Dessine une montagne de taille d et de couleur c
    down()
    triangle(d, c)
    left(60)
    forward(2*d/3)
    right(60)
    triangle(d/3, 'white')
    right(120)
    forward(2*d/3)
    left(120)
    up()
    
def rayons(n, d):
    # Dessine n rayons de soleil de longueur d
    down()
    color('yellow')
    width(5)
    for i in range(n):
        forward(d)
        backward(d)
        left(360/n)
    color('black')
    up()
    
def soleil(r, n, d):
    # Dessine un soleil de rayon r avec n rayons de longueur d
    down()
    dot(r*2, 'yellow')
    rayons(n, d)
    up()
    
def nuage(d, n):
    # Dessine un nuage composé aléatoirement de n cercles de diamètre d
    down()
    for i in range(n):
        dot(d, 'white')
        left(randint(0, 360))
        up()
        forward(20)
        down()
    up()
    
def fleur(d, n, c_centre, c_petale):
    # Dessine une fleur avec un centre de diamètre d et de couleur c_centre avec n pétales de couleur c_petale
    up()
    for i in range(n):
        dot(d, c_petale)
        forward(d*0.8)
        left(360/n)
    left(60)
    forward(d*0.7)
    dot(d*0.7, c_centre)

# --------------------------------------------------------
# Ecrivez ici les appels de fonctions pour faire le dessin
# --------------------------------------------------------

dot(10000, 'green') # Background vert
up()
goto(-500, 0)
down()
rectangle(1000, 1000, 'lightblue') # Ciel

# Dessin des 4 montagnes
montagne(200, 'grey')
forward(150)
montagne(150, 'light grey')
forward(200)
montagne(250, 'silver')
backward(80)
montagne(100, 'grey')

# Dessin du soleil
goto(300, 200)
soleil(50, 10, 80)

# Dessin des nuages aux coordonnées prédéfinies dans une liste
for coords in [(-400, 250), (-350, 300), (-320, 200), (-250, 250), (-100, 300)]:
    goto(coords)
    nuage(40, 5)

# Dessin de 50 fleurs disposées aléatoirement dans l'herbe
for i in range(50):
    x = randint(-400, 400)
    y = randint(-350, -50)
    taille = randint(5, 15)
    goto(x, y)
    fleur(taille, 5, 'gold', 'red')

hideturtle() # Cache la tortue
done()
```
````

## Plus d'exemples

Ces exemples ont été créés par des élèves en 3M, en option complémentaire informatique. Ils sont plus complexes que ce que vous allez faire mais peuvent servir d'inspiration.

### Jeu vidéo

![projet](../media/projets_dessin/projet_alex.png)

### Maison de campagne

![projet](../media/projets_dessin/projet_alice.png)

### Cadre des Pyrénées

![projet](../media/projets_dessin/projet_andi.png)

### Japon

![projet](../media/projets_dessin/projet_arthur.png)

### Swiss space

![projet](../media/projets_dessin/projet_emilien.png)

### Maison meublée

![projet](../media/projets_dessin/projet_enrico.png)

### Casque d'astronaute

![projet](../media/projets_dessin/projet_florent.png)

### Urbain et rural

![projet](../media/projets_dessin/projet_garance.png)

### Star Trek

![projet](../media/projets_dessin/projet_gregory.png)

### Loup sous la lune

![projet](../media/projets_dessin/projet_hugo.jpg)

### Fantaisie psychédélique

![projet](../media/projets_dessin/projet_samuel.png)

### Bateaux de pêche

![projet](../media/projets_dessin/projet_walid.png)
