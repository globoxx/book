(prog_jeu.star_wars)=

# 4. Star wars (shooter)

Le jeu consiste en un vaisseau pouvant se déplacer dans une fenêtre et tirer des projectiles vers des astéroïdes qui se déplacent vers le bas de l'écran. Le but est de détruire les astéroïdes en les touchant avec les projectiles tout en les évitant.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/star_wars.zip>`.

```{image} ../media/star_wars.gif
```

## 1. Faire apparaître une fenêtre

La première étape est de définir le nom de notre jeu dans la variable `TITLE`, ainsi que la largeur `WIDTH` et la hauteur `HEIGHT` de notre fenêtre. Nous allons également importer des fonctions de `pgzhelper` afin de nous faciliter la vie. Pygame Zero s'occupe du reste !

```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Star Wars'

WIDTH = 1000
HEIGHT = 800

pgzrun.go() # Lance le jeu
```

```{image} ../media/pygame_fenetre.png
```

Pygame Zero fonctionne avec 2 fonctions principales: `draw` et `update`. Tandis que `draw` est appelée pour afficher des choses à l'écran, `update` est appelée pour faire évoluer le jeu. Elles sont toutes 2 appelées en boucle automatiquement.

```python
import pgzrun
from pgzhelper import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

def draw():
    pass # Ajouter ici tout ce qui concerne l'affichage
    # pass est une instruction qui ne fait rien, à remplacer par du code par la suite

def update():
    pass # Ajouter ici tout ce qui concerne l'évolution du jeu

pgzrun.go()
```

## 2. S'occuper du fond d'écran

`screen` est un objet accessible grâce à Pygame qui représente la fenêtre de notre jeu.  
On va y attacher cette image de fond.

```{image} ../media/space_background.png
```

Voici comment faire:

```python
def draw():
    screen.blit('space_background', (0, 0)) # Dessine l'image 'space_background' aux coordonnées (0, 0)
```

La méthode `blit(image, (x, y))` de `screen` permet de dessiner une image sur la fenêtre aux coordonnées (x, y) correspondant au coin supérieur gauche de l'image. Comme l'image est plus grande que la fenêtre, elle la recouvre entièrement.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

def draw():
    screen.blit('space_background', (0, 0))

def update():
    pass

pgzrun.go()
```
````

## 3. Ajouter le vaisseau

Il est temps d'ajouter notre vaisseau (que nous continuerons d'appeler `player`). Il s'agit bien sûr du Faucon Millenium, le vaisseau emblématique de Han Solo !

```{image} ../media/ship.png
```

```python
player = Actor('ship') # Création du vaisseau
player.x = WIDTH/2 # Positionnement du vaisseau au centre de l'écran en x
player.y = HEIGHT/2 # Positionnement du vaisseau au centre de l'écran en y
```

Afin de dessiner notre vaisseau, il faut en dernier lieu appeler la méthode `player.draw()` dans la fonction principale `draw` de Pygame.

```python
def draw():
    screen.blit('space_background', (0, 0))
    player.draw() # On dessine le vaisseau ici !
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()

def update():
    pass

pgzrun.go()
```
````

## 4. Déplacer le vaisseau

Nous allons déplacer le vaisseau grâce aux touches `w, a, s, d`. On va utiliser l'objet `keyboard` pour récupérer les touches enfoncées par l'utilisateur et modifier les coordonnées `x` et `y` du vaisseau.

```python
def update():
    if keyboard.a: # Si la touche a est enfoncée
        player.x -= 3 # Déplace le vaisseau à gauche
```

Il nous suffit donc de contrôler quelles touches sont enfoncées et de modifier les coordonnées de notre vaisseau en conséquence:

```python
def update():
    if keyboard.a:
        player.x -= 3 # Déplacement à gauche
    if keyboard.d:
        player.x += 3 # Déplacement à droite

    if keyboard.w:
        player.y -= 3 # Déplacement en haut
    if keyboard.s:
        player.y += 3 # Déplacement en bas
```

Vous remarquez que nous bougeons de `3` pixels par "tour de jeu". Afin de pouvoir facilement modifier la vitesse de notre vaisseau par la suite, il serait plus judicieux de lui définir une vitesse.

Nous pouvons ajouter un attribut `speed` à notre objet `player` et lui donner la valeur `3`. Ainsi, nous n'aurons ensuite plus qu'à modifier cette valeur pour accélérer ou ralentir notre personnage à notre guise.

```python
player = Actor('ship', (WIDTH/2, HEIGHT/2))
player.speed = 3 # Nouvel attribut speed pour régler la vitesse du vaisseau

...

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

pgzrun.go()
```
````

## 5. Ajouter un astéroide

Il est temps d'ajouter des astéroïdes pour pimenter un peu notre jeu. Ils apparaîtront en haut de l'écran et descendront vers le bas.

```{image} ../media/asteroid.png
```

Nous pouvons ensuite créer un objet `asteroid` et lui donner des coordonnées de départ (`x` aléatoire et `y` fixe en haut de l'écran). La foncton permettant de tirer un nombre entier aléatoire entre 2 bornes `a` et `b` se nomme `randint(a, b)`. Pour qu'elle fonctionne, nous devons également importer le module `random` qui contient cette fonction.

```python
from random import * # Importe tout un tas de fonctions pour faire de l'aléatoire

...

asteroid = Ennemy('asteroid') # Création de l'ennemi aux coordonnées aléatoires
asteroid.x = randint(0, WIDTH) # Positionnement aléatoire en x
asteroid.y = -50 # Positionnement en haut de l'écran
```

N'oublions pas d'appeler la méthode `asteroid.draw()` dans la fonction `draw`.

```python
def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    asteroid.draw() # On dessine l'astéroïde !
```

Occupons nous à présent du déplacement de notre astéroïde. Il va simplement "tomber" vers le bas de l'écran, c'est à dire que sa coordonnée `y` va augmenter au cours du temps tandis que sa coordonnée `x` restera fixe. Nous allons lui donner une vitesse de déplacement `speed` comme pour le vaisseau.

```python
...
asteroid.speed = 5 # Vitesse de déplacement de l'astéroïde

def update():
    ...
    asteroid.y += asteroid.speed # Déplacement de l'astéroïde vers le bas
```

```{admonition} L'astéroïde sort de l'écran ?
:class: warning
Une fois arrivé en bas de l'écran, l'astéroïde disparaît pour toujours. C'est voulu dans ce tutoriel, mais vous pourriez faire réapparaître l'astéroïde en haut de l'écran quand il sort (comme dans le jeu du running ninja de la dernière fois).
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroid = Actor('asteroid')
asteroid.x = randint(0, WIDTH)
asteroid.y = -50
asteroid.speed = 5

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    asteroid.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    asteroid.y += asteroid.speed

pgzrun.go()
```
````

## 6. Faire tourner l'astéroïde sur lui-même

Nous allons tenter d'ajouter un peu de mouvement à notre jeu en faisant tournoyer notre astéroïde sur lui même. Pour cela, nous allons progressivement modifier l'`angle` de l'image représentant notre astéroïde. Cet attribut `angle` vaut `0` par défaut et correspond à l'angle de rotation de l'image. En modifiant cette valeur jusqu'à `360` degrés, on fait tourner l'image.

```python
def update():
    ...
    asteroid.y += asteroid.speed
    asteroid.angle += 5 # Fait tourner l'astéroïde de 5 degrés à chaque tour de jeu
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroid = Actor('asteroid')
asteroid.x = randint(0, WIDTH)
asteroid.y = -50
asteroid.speed = 5

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    asteroid.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    asteroid.y += asteroid.speed
    asteroid.angle += 5

pgzrun.go()
```
````

## 7. Ajouter plusieurs astéroïdes

````{admonition} Partie importante
:class: important
Ce chapitre et le suivant sont particulièrement importants car ils expliquent comment gérer une grande quantité d'acteurs dans votre jeu. Jusqu'ici, nous avons créé un seul astéroïde que nous avons appelé `asteroid` et un `player`. Mais dans un vrai jeu, il y a souvent des dizaines d'acteurs à gérer en même temps. Comment faire pour les gérer tous ? Avec des *listes* !
````

Pour avoir plusieurs astéroïdes en même temps dans le jeu, nous pourrions créer `asteroid1`, `asteroid2`, `asteroid3`, etc. mais cela deviendrait rapidement ingérable. A la place, nous allons remplir une **liste d'astéroïdes**. Nous allons donc remplacer notre unique objet `asteroid` par une liste nommée `asteroids` que nous remplirons au départ avec 3 astéroïdes.

```python
asteroids = [] # Création de la liste d'astéroïdes, elle est vide au départ (d'où les crochets vides)
for i in range(3): # On crée une boucle qui tourne 3 fois pour créer 3 astéroïdes
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid) # On ajoute l'astéroïde créé à la liste des astéroïdes
```

````{admonition} Attention
:class: danger
Il faut mettre à jour les fonctions `draw` et `update` car au lieu de dessiner `asteroid`, nous voulons à présent parcourir la liste `asteroids` et dessiner chacun d'eux. Un parcours de liste se fait avec une boucle `for`.

```python
def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    for asteroid in asteroids: # Parcourt la liste des astéroïdes
        asteroid.draw() # Dessine chacun d'eux

def update():
    ...

    for asteroid in asteroids: # Parcourt la liste des astéroïdes
        asteroid.y += asteroid.speed # Fait descendre chacun d'eux
        asteroid.angle += 5 # Fait tourner chacun d'eux
```
````

Nous avons à présent une liste d'astéroïdes qui contient `3` astéroïdes. Mais comment remplir cette liste au cours du jeu ?

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroids = []
for i in range(3):
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid)

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    for asteroid in asteroids:
        asteroid.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    for asteroid in asteroids:
        asteroid.y += asteroid.speed
        asteroid.angle += 5

pgzrun.go()
```
````

# 8. Ajouter des astéroïdes au cours du jeu

Commençons par définir une nouvelle fonction qui va s'occuper d'ajouter un nouvel astéroïde à la liste. Dans cet exemple, je vais la nommer `add_asteroid`, mais vous pouvez lui donner le nom que vous voulez car ce n'est pas une fonction spéciale comme `update` ou `draw`.

```python
for i in range(3):
    add_asteroid() # Appelle la fonction add_asteroid 3 fois pour ajouter 3 astéroïdes au départ

def add_asteroid():
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid) # Ajoute l'astéroïde à la liste des astéroïdes
```

La question est: quand appeler cette fonction ? Quand voulons-nous ajouter un astéroïde ? Ici, disons que nous aimerions ajouter un astéroïde toutes les 5 secondes. (Mais nous pourrions aussi choisir d'en ajouter un à chaque fois qu'un astéroïde est détruit ou sort de l'écran, ou à chaque fois que le joueur atteint un certain score, etc.)

Pour appler notre fonction toutes les 5 secondes, Pygame nous offre pour ceci un objet très utile: `clock`. **Cet objet permet d'agender des appels de fonction dans le temps**.

```python
...

clock.schedule_interval(add_asteroid, 5.0)

def add_asteroid():
    ...
```

La méthode `schedule_interval(f, x)` permet d'appeler automatiquement une fonction `f` toutes les `x` secondes. Nous l'avons donc réglée pour appeler `add_asteroid` toutes les `5` secondes, mais vous pouvez modifier cette valeur.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroids = []
for i in range(3):
    add_asteroid()

clock.schedule_interval(add_asteroid, 5.0)

def add_asteroid():
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid)

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    for asteroid in asteroids:
        asteroid.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    for asteroid in asteroids:
        asteroid.y += asteroid.speed
        asteroid.angle += 5

pgzrun.go()
```
````

## 9. Tirer des lasers

Il est temps de pouvoir tirer sur les astéroïdes ! Nous allons créer un nouvel acteur pour représenter un laser qui sera tiré en appuyant sur la touche `espace` et qui partira vers le haut.

Commençons par créer une liste de lasers (vide au départ) qui se remplira à chaque fois que le joueur appuiera sur la touche `espace` pour tirer.  Il nous faut également une fonction `add_laser` qui s'occupera de créer un nouveau laser et de l'ajouter à la liste.

```python
...

lasers = [] # Création de la liste vide de lasers

def add_laser():
    laser = Actor('laser') # Création du laser
    laser.x = player.x # Positionnement du laser à l'emplacement du joueur en x
    laser.y = player.y # Positionnement du laser à l'emplacement du joueur en y
    laser.speed = 10 # Vitesse de déplacement du laser
    lasers.append(laser) # Ajout du laser à la liste des lasers
```

Nous voulons appeler cette fonction `add_laser` à chaque fois que le joueur appuie sur la touche `espace`. Cette détection doit se faire dans la fonction `update`.

```python
def update():
    ...
    if keyboard.space: # Si la touche espace est enfoncée
        add_laser() # On ajoute un laser
```

Il nous reste à afficher nos lasers en les ajoutant à la fonction `draw` et à les faire avancer dans la fonction `update` en modifiant leur coordonnée `y` pour les faire monter vers le haut de l'écran.

```python
def draw():
    ...
    for laser in lasers: # Parcourt les lasers
        laser.draw() # Dessine chacun d'eux

def update():
    ...
    for laser in lasers: # Parcourt les lasers
        laser.y -= laser.speed # Fait monter chacun d'eux
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroids = []
for i in range(3):
    add_asteroid()

lasers = []

clock.schedule_interval(add_asteroid, 5.0)

def add_asteroid():
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid)

def add_laser():
    laser = Actor('laser')
    laser.x = player.x
    laser.y = player.y
    laser.speed = 10
    lasers.append(laser)

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    for asteroid in asteroids:
        asteroid.draw()
    for laser in lasers:
        laser.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    for asteroid in asteroids:
        asteroid.y += asteroid.speed
        asteroid.angle += 5

    if keyboard.space:
        add_laser()

    for laser in lasers:
        laser.y -= laser.speed

pgzrun.go()
```
````


## 10. Gérer les collisions

Il est temps de donner du pouvoir à nos lasers pour détruire les astéroïdes ! Mais également à nos astéroïdes pour détruire notre vaisseau !

```{image} ../media/collision.png
```

```{admonition} Rappel
:class: note
Un check de collision entre un acteur et un autre acteur se fait avec la méthode `acteur.collides_with(autre_acteur)` qui retourne `True` s'il y a collision entre les deux acteurs et `False` sinon.
```

Commençons par les collisions entre le vaisseau et les astéroïdes. Où ajouter ce check de collision ? Nous allons parcourir la liste des astéroïdes et contrôler si l'un d'eux est en contact avec le vaisseau.

```python
def update():
    ...
    for asteroid in asteroids:
        if player.collides_with(asteroid): # Si le joueur est en contact avec un astéroïde
            exit() # On quitte le jeu
```

Passons à présent aux collisions entre les lasers et les astéroïdes. Où ajouter le contrôle de collision ? Le plus simple est de le faire après le déplacement d'un laser: on parcourt la liste des astéroïdes et on contrôle si le laser est en contact avec l'un d'eux.

```python
def update():
    ...
    for laser in lasers:
        laser.y -= laser.speed
        for asteroid in asteroids:
            if laser.collides_with(asteroid): # Si le laser est en contact avec un astéroïde
                asteroids.remove(asteroid) # On supprime l'astéroïde de la liste des astéroïdes
                lasers.remove(laser) # On supprime le laser de la liste des lasers
```

```{admonition} Supprimer des acteurs
:class: warning
Notez que l'on peut supprimer un acteur d'une liste avec la méthode `remove` de la liste.
```


````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *
from random import *

TITLE = 'Star Wars'
WIDTH = 1000
HEIGHT = 800

player = Actor('ship')
player.x = WIDTH/2
player.y = HEIGHT/2
player.speed = 3

asteroids = []
for i in range(3):
    add_asteroid()

lasers = []

clock.schedule_interval(add_asteroid, 5.0)

def add_asteroid():
    asteroid = Actor('asteroid')
    asteroid.x = randint(0, WIDTH)
    asteroid.y = -50
    asteroid.speed = 5
    asteroids.append(asteroid)

def add_laser():
    laser = Actor('laser')
    laser.x = player.x
    laser.y = player.y
    laser.speed = 10
    lasers.append(laser)

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
    for asteroid in asteroids:
        asteroid.draw()
    for laser in lasers:
        laser.draw()

def update():
    if keyboard.a:
        player.x -= player.speed
    if keyboard.d:
        player.x += player.speed

    if keyboard.w:
        player.y -= player.speed
    if keyboard.s:
        player.y += player.speed

    for asteroid in asteroids:
        asteroid.y += asteroid.speed
        asteroid.angle += 5

    if keyboard.space:
        add_laser()

    for laser in lasers:
        laser.y -= laser.speed

pgzrun.go()
```
````

## 10. Idées d'améliorations

```{admonition} Travail à rendre
Votre travail consiste à ajouter au minimum les améliorations suivantes au jeu:

* 2 améliorations faciles
* 1 amélioration moyenne
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Ajouter des bruitages (ex: tir + destruction d'astéroïde) et de la musique.
* Faire en sorte que le vaisseau ne puisse pas sortir de l'écran.
* Ajouter un compteur d'astéroïdes détruits (score) et l'afficher à l'écran.
* Les astéroïdes ne se déplacent pas tous à la même vitesse, certains sont plus rapides que d'autres (aléatoirement).
* Détruire automatiquement les lasers et astéroïdes qui sortent de l'écran pour éviter d'avoir des listes qui se remplissent à l'infini et qui ralentissent le jeu.
* Les astéroïdes n'ont pas tous la même taille ou image (aléatoirement).

**Un peu plus complexe (moyen):**

* Faire en sorte qu'en cas de collision avec un astéroïde, le vaisseau perd de la vie et l'astéroïde est détruit. La vie du vaisseau est affichée à l'écran.
* Faire en sorte que les astéroïdes doivent recevoir plusieurs tirs avant d'être détruits (en leur donnant une vie qui diminue à chaque tir).
* Permettre au vaisseau de ramasser des objets pour augmenter son score ou sa vitesse.
* Ajouter une image d'explosion qui apparaît puis disparaît lorsqu'un astéroïde est détruit.
* Ajouter un second joueur qui pourra se déplacer et tirer avec d'autres touches.
* Ajouter un nouveau type d'ennemi qui se comporte différemment que les astéroïdes.
* Faire en sorte que le personnage ne se déplace pas plus rapidement en diagonal qu'à l'horizontal ou à la verticale.

**Challenging (difficile):**

* Faire en sorte que le monde bouge autour du personnage afin qu'il puisse se balader librement dans toutes les directions sans jamais toucher un bord. Indice: le joueur ne se déplace plus, mais déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
* Ajouter un ennemi capable de tirer des lasers vers le joueur.
* Créer un second niveau atteignable en passant un certain score où les ennemis sont différents et plus coriaces.
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
* Autres idées..?

## Travailler en dehors des TP

`````{admonition} Comment travailler en dehors du TP
:class: danger
````{dropdown} Depuis la maison
1. Téléchargez et installez [Python](https://www.python.org/downloads/).
2. Téléchargez et installez [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/download/). Faites attention à sélectionner la version qui correspond à votre système d'exploitation (Windows, MacOS, Linux).
3. Ouvrez Pycharm et créez un nouveau projet. (Bouton "New Project" sur l'écran d'accueil ou via le menu "File" -> "New Project").
4. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet (PythonProject par défaut).
5. Installez le package `pgzero`. Pour cela, assurez-vous d'avoir la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
````{dropdown} Depuis l'école
1. Ouvrez Pycharm et créez un nouveau projet.
2. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet. **Attention**, si vous prenez votre dossier de travail depuis votre disque réseau (pxxxxx), il faudra le copier sur le bureau avant de le déplacer dans Pycharm.
3. Installez le package `pgzero`. Pour cela, assurez-vous d'avoir la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
`````
