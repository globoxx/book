(prog_jeu.star_wars_simple)=

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
import pgzero
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
import pgzero
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

```{admonition} Changer la taille d'un acteur ?
:class: note
Il est possible de redimensionner une image d'acteur en lui donnant une échelle (scale). Par exemple, `player.scale = 2` rendrait le vaisseau deux fois plus grand que sa taille d'origine. A l'inverse, `player.scale = 0.5` le rendrait deux fois plus petit que sa taille d'origine.
```

````{dropdown} Voir le code complet à ce point
```python
import pgzero
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

Nous pouvons ajouter un attribut `speed` à notre objet `player` et lui donner la valeur `3`. Ainsi, vous n'avez ensuite plus qu'à modifier cette valeur pour accélérer ou ralentir votre vaisseau à votre guise.

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
import pgzero
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

## 5. Ajouter un astéroïde

Il est temps d'ajouter des astéroïdes pour pimenter un peu notre jeu. Ils apparaîtront en haut de l'écran et descendront vers le bas.

```{image} ../media/asteroid.png
```

Nous pouvons ensuite créer un objet `asteroid` et lui donner des coordonnées de départ (`x` aléatoire et `y` fixe en haut de l'écran). La fonction permettant de tirer un nombre entier aléatoire entre 2 bornes `a` et `b` se nomme `randint(a, b)`. Pour qu'elle fonctionne, nous devons également importer le module `random` qui contient cette fonction.

```python
from random import * # Importe tout un tas de fonctions pour faire de l'aléatoire

...

asteroid = Actor('asteroid') # Création de l'ennemi aux coordonnées aléatoires
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

Occupons-nous à présent du déplacement de notre astéroïde. Il va simplement "tomber" vers le bas de l'écran, c'est à dire que sa coordonnée `y` va augmenter au cours du temps tandis que sa coordonnée `x` restera fixe. Nous allons lui donner une vitesse de déplacement `speed` comme pour le vaisseau.

```python
...
asteroid.speed = 15 # Vitesse de déplacement de l'astéroïde

def update():
    ...
    asteroid.y += asteroid.speed # Déplacement de l'astéroïde vers le bas
```

````{dropdown} Voir le code complet à ce point
```python
import pgzero
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
asteroid.speed = 15

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

## 6. Faire tourner l'astéroïde sur lui-même et le faire réapparaître

Nous allons tenter d'ajouter un peu de mouvement à notre jeu en faisant tournoyer notre astéroïde sur lui même. Pour cela, nous allons progressivement modifier l'`angle` de l'image représentant notre astéroïde. Cet attribut `angle` vaut `0` par défaut et correspond à l'angle de rotation de l'image. En augmentant cette valeur, on fait tourner l'image.

```python
def update():
    ...
    asteroid.y += asteroid.speed
    asteroid.angle += 5 # Fait tourner l'astéroïde de 5 degrés à chaque tour de jeu
```

Pour faire réapparaître notre astéroïde une fois qu'il a disparu en bas de l'écran, il suffit de contrôler sa coordonnée `y` et de lui redonner une coordonnée `y` en haut de l'écran ainsi qu'une coordonnée `x` aléatoire.

```python
def update():
    ...
    asteroid.y += asteroid.speed
    asteroid.angle += 5
    if asteroid.y > HEIGHT: # Si l'astéroïde est complètement sorti de l'écran
        asteroid.x = randint(0, WIDTH) # On lui redonne une coordonnée x aléatoire
        asteroid.y = -50 # On le replace en haut de l'écran
```

````{dropdown} Voir le code complet à ce point
```python
import pgzero
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
asteroid.speed = 15

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
    if asteroid.y > HEIGHT:
        asteroid.x = randint(0, WIDTH)
        asteroid.y = -50

pgzrun.go()
```
````

## 7. Tirer des lasers

Il est temps de pouvoir tirer sur les astéroïdes ! Nous allons créer un nouvel acteur pour représenter un laser qui sera tiré en appuyant sur la touche `espace` et qui partira vers le haut.

Nous n'aurons pas qu'un seul laser à l'écran, mais potentiellement beaucoup ! Nous ne pouvons donc pas nous contenter de créer une variable `laser` pour représenter notre laser, il nous faut une liste de lasers qui pourra contenir tous les lasers présents à l'écran. Nous allons donc créer une liste `lasers` qui sera vide au départ.

```python
asteroid = Actor('asteroid')
...

lasers = [] # Création de la liste de lasers, elle est vide au départ
```

Nous voulons ajouter un laser à cette liste à chaque fois que l'utilisateur appuie sur la touche `espace`.

```python
def update():
    ...
    if keyboard.space: # Si la touche espace est enfoncée
        laser = Actor('laser') # Création d'un laser
        laser.x = player.x # Positionnement du laser sur le vaisseau en x
        laser.y = player.y # Positionnement du laser sur le vaisseau en y
        lasers.append(laser) # Ajout du laser à la liste des lasers
```

Il nous reste à afficher nos lasers dans la fonction `draw` et à les faire avancer dans la fonction `update` en modifiant leur coordonnée `y` pour les faire monter vers le haut de l'écran. On peut parcourir la liste des lasers avec une boucle `for`.

```python
def draw():
    ...
    for laser in lasers: # Pour chaque laser dans la liste des lasers
        laser.draw() # On dessine le laser

def update():
    ...
    for laser in lasers: # Pour chaque laser dans la liste des lasers
        laser.y -= laser.speed # On fait avancer le laser vers le haut de l'écran
```

````{dropdown} Voir le code complet à ce point
```python
import pgzero
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
asteroid.speed = 15

lasers = []

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
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

    asteroid.y += asteroid.speed
    asteroid.angle += 5

    if keyboard.space:
        laser = Actor('laser')
        laser.x = player.x
        laser.y = player.y
        laser.speed = 10
        lasers.append(laser)

    for laser in lasers:
        laser.y -= laser.speed

pgzrun.go()
```
````

## 8. Gérer les collisions

Il est temps de donner du pouvoir à nos lasers pour détruire les astéroïdes ! Mais également à nos astéroïdes pour détruire notre vaisseau !

```{image} ../media/collision.png
```

```{admonition} Rappel
:class: note
Un check de collision entre un acteur et un autre acteur se fait avec la méthode `acteur.collides_with(autre_acteur)` qui retourne `True` s'il y a collision entre les deux acteurs et `False` sinon.
```

Commençons par les collisions entre le vaisseau et les astéroïdes. Où ajouter ce check de collision ? Dans la fonction `update` !

```python
def update():
    ...
    if player.collides_with(asteroid): # Si le joueur est en contact avec l'astéroïde
        exit() # On quitte le jeu
```

Passons à présent aux collisions entre les lasers et les astéroïdes. Où ajouter le contrôle de collision ? Le plus logique est de le faire après le déplacement d'un laser, toujours dans la fonction `update`.

```python
def update():
    ...
    for laser in lasers: # Pour chaque laser dans la liste des lasers
        laser.y -= laser.speed
        if laser.collides_with(asteroid): # Si le laser est en contact avec un astéroïde
            lasers.remove(laser) # On supprime le laser de la liste des lasers
            # On fait réapparaître l'astéroïde comme vu précédemment
            asteroid.x = randint(0, WIDTH)
            asteroid.y = -50
```

```{admonition} Supprimer des acteurs
:class: warning
Notez que l'on peut supprimer un acteur d'une liste avec la méthode `remove` de la liste.
```

````{dropdown} Voir le code complet à ce point
```python
import pgzero
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
asteroid.speed = 15

lasers = []

def draw():
    screen.blit('space_background', (0, 0))
    player.draw()
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

    asteroid.y += asteroid.speed
    asteroid.angle += 5
    if player.collides_with(asteroid):
        exit()

    if keyboard.space:
        laser = Actor('laser')
        laser.x = player.x
        laser.y = player.y
        laser.speed = 10
        lasers.append(laser)

    for laser in lasers:
        laser.y -= laser.speed
        if laser.collides_with(asteroid):
            lasers.remove(laser)
            asteroid.x = randint(0, WIDTH)
            asteroid.y = -50
pgzrun.go()
```
````

## Idées d'améliorations

```{admonition} Travail à rendre
* Au moins 1 amélioration facile
* Réfléchir au contenu de votre jeu en remplissant le document fourni.
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Ajouter au moins un bruitage (ex: tir ou destruction d'astéroïde) et de la musique.
* Faire en sorte que le vaisseau ne puisse pas sortir de l'écran.
* Ajouter un compteur d'astéroïdes détruits (score) et l'afficher à l'écran.
* Détruire automatiquement les lasers qui sortent de l'écran pour éviter d'avoir des listes qui se remplissent à l'infini et qui ralentissent le jeu.

**Un peu plus complexe (moyen):**

* Ajouter plusieurs astéroïdes à l'écran en même temps. Vous pouvez les stocker dans une liste `asteroids` de la même manière que les lasers.
* Faire en sorte qu'en cas de collision avec un astéroïde, le vaisseau perd de la vie et l'astéroïde est détruit. La vie du vaisseau est affichée à l'écran.
* Faire en sorte que les astéroïdes doivent recevoir plusieurs tirs avant d'être détruits (en leur donnant une vie qui diminue à chaque tir).
* Permettre au vaisseau de ramasser des objets pour augmenter son score ou sa vitesse.
* Ajouter une image d'explosion qui apparaît puis disparaît lorsqu'un astéroïde est détruit.
* Ajouter un second joueur qui pourra se déplacer et tirer avec d'autres touches.
* Ajouter un nouveau type d'ennemi qui se comporte différemment que les astéroïdes.
* Empêcher le spam de lasers en faisant en sorte que le joueur ne puisse tirer qu'une fois tous les 0.5 secondes par exemple.
* Faire en sorte que le personnage ne se déplace pas plus rapidement en diagonal qu'à l'horizontal ou à la verticale.

**Challenging (difficile):**

* Faire en sorte que le monde bouge autour du personnage afin qu'il puisse se balader librement dans toutes les directions sans jamais toucher un bord. Indice: le joueur ne se déplace plus, mais déplacez tous les acteurs du jeu dans la direction inverse au déplacement du joueur.
* Ajouter un ennemi capable de tirer des lasers vers le joueur.
* Créer un second niveau atteignable en passant un certain score où les ennemis sont différents et plus coriaces.
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
* Autres idées..?

## Comment faire pour ... ?

### Afficher du texte à l'écran ?
Il existe une fonction `screen.draw.text` qui permet d'afficher du texte à l'écran. Par exemple, `screen.draw.text('Score: 10', (10, 10), fontsize=30, color='white')` affichera le texte "Score: 10" en blanc avec une taille de police de 30 aux coordonnées (10, 10) de la fenêtre.

### Ajouter une variable dans du texte affiché à l'écran ?
Si vous voulez afficher une variable dans du texte, vous pouvez utiliser les f-strings de Python. Par exemple, si vous avez une variable `score` qui vaut 10, vous pouvez l'afficher avec le texte "Score: 10" en écrivant `screen.draw.text(f'Score: {score}', (10, 10), fontsize=30, color='white')`.

### Tirer un nom d'image aléatoire ?
Vous pouvez utiliser le module `random` de Python pour tirer un nom d'image aléatoire. Par exemple, si vous avez plusieurs images d'astéroïdes nommées `asteroid1.png`, `asteroid2.png`, etc., vous pouvez choisir une image aléatoire avec `random.choice(['asteroid1', 'asteroid2', 'asteroid3'])`.

### Mesurer le temps entre 2 événements ?
Vous pouvez utiliser la fonction `time.time()` du module `time` pour mesurer le temps écoulé entre 2 événements. Par exemple, vous pouvez stocker le temps du dernier tir dans une variable `last_shot_time = time.time()` et ensuite vérifier si suffisamment de temps s'est écoulé avant de permettre un nouveau tir avec `if time.time() - last_shot_time > 0.5:`.

### Détecter un clic de souris ?
Pygame Zero offre une fonction spéciale `on_mouse_down(pos)` qui est appelée automatiquement à chaque fois que l'utilisateur clique avec la souris. La variable `pos` correspond aux coordonnées du clic de souris. Vous pouvez donc ajouter cette fonction à votre code et y mettre le code que vous voulez exécuter à chaque clic de souris.
Exemple:
```python
def on_mouse_down(pos):
    print(f'Vous avez cliqué aux coordonnées {pos}')    
```

### Ajouter un bouton ?
Pgzhelper vous fournit une classe `Button` qui permet de créer facilement des boutons cliquables. Vous pouvez créer un bouton avec `button = Button('mon_texte', (x, y), (largeur, hauteur))` et ensuite vérifier s'il a été cliqué dans la fonction `on_mouse_down(pos)` avec `if button.collidepoint(pos):`. Important: n'oubliez pas d'appeler la méthode `button.draw()` dans la fonction `draw` pour que le bouton soit visible à l'écran.
Exemple:
```python
button = Button('Cliquez-moi', (100, 100), (200, 50))
def on_mouse_down(pos):
    if button.collidepoint(pos):
        print('Le bouton a été cliqué !')

def draw():
    button.draw() # Affiche le bouton
```

### Déplacer un acteur dans une direction donnée ?
Si vous voulez déplacer un acteur dans une direction donnée, vous pouvez lui donner un attribut `direction` qui correspond à un angle en degrés (0 = vers la droite, 90 = vers le bas, 180 = vers la gauche, 270 = vers le haut). Ensuite, dans la fonction `update`, vous pouvez simplement appeler `acteur.move_in_direction(speed)` qui déplacera l'acteur à la vitesse `speed` dans la direction indiquée par son attribut `direction`. Cela remplace donc `acteur.x += ...` et `acteur.y += ...`.

### Calculer l'angle / la direction entre 2 acteurs ?
Vous pouvez utiliser la fonction `angle_to` d'un acteur pour calculer l'angle entre lui et un autre acteur. Par exemple, `player.angle_to(asteroid)` vous donnera l'angle en degrés entre le joueur et l'astéroïde. Cela peut être utile pour faire un ennemi qui poursuit le joueur ou pour faire des tirs qui partent dans la direction du joueur.
Exemple:
```python
laser_enemi.direction = laser_enemi.angle_to(player)
laser_enemi.move_in_direction(speed)
```

## Travailler en dehors des TP

`````{admonition} Comment travailler en dehors du TP
:class: danger
````{dropdown} Depuis la maison
1. Téléchargez et installez [Python 3.12](https://www.python.org/downloads/). Prenez bien la version 3.12 car les versions plus récentes ne sont pas encore compatibles avec Pygame Zero.
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
