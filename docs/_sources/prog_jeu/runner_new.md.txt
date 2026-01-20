(prog_jeu.runner_new)=

# 3. Running Ninja (runner)

Dans cette introduction, nous allons développer un premier jeu simple étape par étape. Le jeu consiste en un ninja devant sauter par dessus des obstacles. Le jeu est terminé si le ninja touche un obstacle.

{download}`Téléchargement des ressources du jeu<../data/prog_2d/runner.zip>`.

```{image} ../media/runner.gif
```

## 1. Faire apparaître une fenêtre

La première étape est de définir le nom de notre jeu dans la variable `TITLE`, ainsi que la largeur `WIDTH` et la hauteur `HEIGHT` de notre fenêtre. Nous allons également importer `pgzrun` et des fonctions de `pgzhelper` afin de nous faciliter la vie. Pygame Zero s'occupe du reste !

```python
import pgzero
import pgzrun
from pgzhelper import *

TITLE = 'Runner'

WIDTH = 800
HEIGHT = 600

pgzrun.go() # Lance le jeu
```

```{image} ../media/pygame_fenetre.png
```

Pygame Zero fonctionne avec 2 fonctions principales:
- `draw` s'occupe **d'afficher des choses à l'écran du jeu**
- `update` s'occupe de **faire évoluer la logique jeu**

Elles sont toutes deux exécutées en boucle automatiquement dès qu'on lance le jeu.

```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

def draw():
    pass # Ajouter ici tout ce qui concerne l'affichage
    # pass est une instruction qui ne fait rien, à remplacer par du code par la suite

def update():
    pass # Ajouter ici tout ce qui concerne l'évolution du jeu

pgzrun.go()
```

## 2. S'occuper du fond d'écran

Tous les dessins de notre jeu se feront via la fonction `draw` de Pygame. Il nous faut donc lui ajouter l'instruction permettant de colorier le fond et faire un carré d'herbe.

`screen` est un objet accessible grâce à Pygame qui représente la fenêtre de notre jeu.  
Nous allons faire un ciel bleu ainsi que de l'herbe verte.

```python
def draw():
    screen.fill((163, 232, 254)) # Colorie le fond en bleu ciel (valeurs RGB)
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152)) # Dessine un rectangle vert
    # Rect(x, y, largeur, hauteur)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))

def update():
    pass

pgzrun.go()
```
````

## 3. Ajouter le joueur

Il est temps d'ajouter notre joueur. Il sera représenté par un `acteur`. Chaque `acteur` sera également représenté par une image (que nous appelerons un sprite) et une position (`x`, `y`). Chaque sprite doit être sauvegardé dans le dossier `images`.

```{image} ../media/run__003.png
```

La plateforme <a href="https://kenney.nl/assets" target="_blank">Kenny</a> contient énormément de sprites gratuits à utiliser pour vos jeux.

Pour créer un `acteur`, nous allons utiliser la classe `Actor` fournie par Pygame. Voyez un `acteur` comme une super variable pouvant contenir ses propres variables (que l'on appelle `attributs`) et ses propres fonctions (que l'on appelle `méthodes`).

```python
player = Actor('run__000', (100, 400)) # Création du joueur
# A sa création, on lui fournit le nom de son image et sa position (x, y)
```

Afin de dessiner notre joueur (qui est donc représenté par la variable `player`), il faut appeler la méthode `player.draw()` dans la fonction principale `draw` de Pygame.

```python
def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw() # On dessine le joueur ici !
```

`draw` est une méthode possèdée par tous les `acteurs`.

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()

def update():
    pass

pgzrun.go()
```
````

## 4. Animer le joueur

Notre joueur est statique pour le moment. Nous allons donc ajouter une animation pour le faire courir. Dans un jeu, une animation est une suite d'images qui se succèdent rapidement pour donner l'illusion du mouvement.

```{image} ../media/run__000.png
```

```{image} ../media/run__003.png
```

```{image} ../media/run__009.png
```

Il nous faut commencer par définir la liste des images qui composent notre animation. Pour cela, nous ajoutons un attribut `images` à notre `player` qui contiendra toutes les images de notre animation.

```python
player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)] # Liste des images de l'animation (run__000 à run__009)
# Raccourci pour ['run__000', 'run__001', ..., 'run__009']
```

Pour faire avancer l'animation à chaque tour, il nous faut encore appeler `player.animate()` dans la fonction `update` principale. Par défaut, l'animation se fait à 5 fps (images par seconde) mais on peut choisir une autre valeur.

```python
def update():
    player.animate(20) # On anime le joueur à 20 fps (images par seconde)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()

def update():
    player.animate(20)

pgzrun.go()
```
````

## 5. Ajouter des obstacles

Nous allons ajouter des obstacles qui vont défiler de droite à gauche. Pour cela, nous allons créer un nouvel `acteur` nommé `obstacle`. Les obstacles seront représentés par des cactus.

```{image} ../media/cactus.png
```

```python
obstacle = Actor('cactus', (850, 430)) # Création d'un obstacle en dehors de l'écran à droite
```

Notre `obstacle` est créé en dehors de l'écran à droite (`x = 850`). Nous allons le faire défiler de droite à gauche en le déplaçant de `10` pixels à chaque tour du jeu.

**Il s'agit de logique de jeu !** C'est donc du code que l'on écrira dans la fonction `update`.

Dans notre cas, il faut déplacer l'`obstacle` de quelques pixels vers la gauche (disons `10`) et le faire réapparaître à droite une fois qu'il est sorti de l'écran.

```python
def update():
    player.animate(20)

    obstacle.x -= 10 # Déplacement de l'obstacle de 10 pixels vers la gauche en diminuant sa position en x
    if obstacle.x < -50: # Si l'obstacle sort de l'écran à gauche
        obstacle.x = 850 # Il réapparaît à droite
```

A ce point, il ne reste plus qu'à appeler la méthode `obstacle.draw()` dans la fonction `draw` et le tour est joué !

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]

obstacle = Actor('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()

def update():
    player.animate(20)

    obstacle.x -= 10
    if obstacle.x < -50:
        obstacle.x = 850

pgzrun.go()
```
````

## 6. Permettre au joueur de sauter

Pour pouvoir sauter et retomber, notre personnage doit posséder une vitesse verticale. Nous allons donc ajouter un attribut `vy` à notre  `player` qui représente la vitesse verticale du joueur.

```python
player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0 # Vitesse verticale à 0 par défaut
```

Sauter correspond à une action de notre joueur que nous allons coder dans la fonction `update`. Mais avant de s'occuper du saut, occupons nous d'appliquer la **gravité**. La gravité augmente la vitesse verticale `vy` du joueur. Ensuite, il faut appliquer cette vitesse verticale pour mettre à jour la position verticale `y` du joueur.

```python
def update():
    ...
    player.vy += 1 # Augmentation de la vitesse verticale (gravité)
    player.y += player.vy # Mise à jour de la position verticale du joueur
    ...
```

Oups, notre personnage tombe du jeu et disparaît ! Pour éviter cela, nous allons devoir ajouter une condition (`if`) pour détecter le sol (coordonnée `y` à `400`) et remettre la vitesse verticale à `0`.

```python
def update():
    ...
    player.vy += 1
    player.y += player.vy
    if player.y > 400: # Si le joueur touche le sol (est trop bas sur l'axe y)
        player.y = 400 # Le joueur est remis sur le sol
        player.vy = 0 # La vitesse verticale est remise à 0
    ...
```

Bon et maintenant il faut pouvoir sauter ! Nous allons donc ajouter une condition pour détecter si la touche `space` (espace) est pressée. Si c'est le cas, nous allons donner une vitesse verticale (`vy`) négative au joueur pour le faire aller vers le haut. Pygame Zero nous offre un objet `keyboard` qui nous permet de détecter les touches pressées.

```python
def update():
    ...
    player.vy += 1
    player.y += player.vy
    if player.y > 400:
        player.y = 400
        player.vy = 0

    if keyboard.space: # Si la touche espace est pressée
        player.vy = -15 # Le joueur saute avec une vitesse négative (vers le haut)
    ...
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0

obstacle = Actor('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()

def update():
    player.animate(20)

    player.vy += 1
    player.y += player.vy
    if player.y > 400:
        player.y = 400
        player.vy = 0

    if keyboard.space: # Si la touche espace est pressée
        player.vy = -15

    obstacle.x -= 10
    if obstacle.x < -50:
        obstacle.x = 850

pgzrun.go()
```
````

## 7. Détecter un game over

Notre joueur est invincible ! Il est temps d'ajouter la détection de collision entre le joueur et les obstacles. Si le joueur touche un obstacle, c'est la fin du jeu.

Pour détecter une collision, nous allons utiliser la méthode `collides_with(actor)` que tous les `acteurs` possèdent. Cette méthode retourne `True` si l'`acteur` est en collision avec un autre `acteur`.

Nous allons l'utiliser pour détecter une collision entre le `player` et l'`obstacle`. Nous devons aussi créer une variable `game_over` pour savoir si le jeu est terminé. Par souci de simplicité, nous pouvons définir `game_over` comme un attribut de notre `player`.

```python
player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0
player.game_over = False # Ajout de l'attribut game_over

def update():
    ...
    player.vy += 1
    player.y += player.vy
    if player.y > 400:
        player.y = 400
        player.vy = 0

    if keyboard.space:
        player.vy = -15

    if player.collides_with(obstacle): # Si le joueur touche l'obstacle
        player.game_over = True # Le jeu est terminé
    ...
```

Bien, nous avons maintenant un attribut `game_over` qui est `True` si le joueur touche un obstacle. Il ne reste plus qu'à ajouter une condition dans la fonction `update` du programme principal pour arrêter le jeu si `game_over` est `True`. Il suffit de faire les mises à jours des acteurs **uniquement si** `game_over` est `False`.

```python
def update():
    if not player.game_over: # Si le jeu n'est pas terminé
        # Reste du code que l'on a fait jusqu'ici
```

Nous pouvons également ajouter un message de game over à l'écran si `game_over` est `True`. C'est de l'affichage, cela se fait donc dans la fonction `draw`.

```python
def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()
    if player.game_over: # Si le jeu est terminé
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0
player.game_over = False

obstacle = Actor('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    player.draw()
    obstacle.draw()
    if player.game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)

def update():
    if not player.game_over:
        player.animate(20)

        player.vy += 1
        player.y += player.vy
        if player.y > 400:
            player.y = 400
            player.vy = 0

        if keyboard.space:
            player.vy = -15

        if player.collides_with(obstacle):
            player.game_over = True

        obstacle.x -= 10
        if obstacle.x < -50:
            obstacle.x = 850

pgzrun.go()
```
````

## 8. Tenir et afficher un score

Le score est important dans les jeux ! Pour en tenir un, on peut définir un attribut `score` à notre `player` et l'initialiser à `0`.

```python
player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0
player.game_over = False
player.score = 0 # Initialisation du score à 0
```

Avant de nous occuper de l'augmentation du `score`, voyons déjà comment l'afficher. Afficher du texte à l'écran se fait via l'objet `screen` offert par Pygame. Nous l'utilisons dans la fonction `draw` du programme principal, juste après avoir défini l'image de fond.

```python
def draw():
    ...
    screen.draw.text(f'Score: {player.score}', (15,10), color=(0,0,0), fontsize=30) # Affichage du score
    ...
```

Le score va augmenter à chaque fois qu'un obstacle sort de l'écran. Il suffit donc de l'augmenter de `1` à chaque fois que cela se produit dans la fonction `update`.

```python
def update():
    ...
    obstacle.x -= 10
    if obstacle.x < -50:
        obstacle.x = 850
        player.score += 1 # Augmentation du score car l'obstacle est sorti de l'écran (le joueur l'a évité)
    ...
```

````{dropdown} Voir le code complet à ce point
```python
import pgzrun
from pgzhelper import *

TITLE = 'Runner'
WIDTH = 800
HEIGHT = 600

player = Actor('run__000', (100, 400))
player.images = [f'run__00{i}' for i in range(10)]
player.vy = 0
player.game_over = False
player.score = 0

obstacle = Actor('cactus', (850, 430))

def draw():
    screen.fill((163, 232, 254))
    screen.draw.filled_rect(Rect(0,400,800,200), (88, 242, 152))
    screen.draw.text(f'Score: {player.score}', (15,10), color=(0,0,0), fontsize=30)
    player.draw()
    obstacle.draw()
    if player.game_over:
        screen.draw.text('Game Over', centerx=400, centery=270, color=(255,255,255), fontsize=60)

def update():
    if not player.game_over:
        player.animate(20)

        player.vy += 1
        player.y += player.vy
        if player.y > 400:
            player.y = 400
            player.vy = 0

        if keyboard.space:
            player.vy = -15

        if player.collides_with(obstacle):
            player.game_over = True

        obstacle.x -= 10
        if obstacle.x < -50:
            obstacle.x = 850
            player.score += 1

pgzrun.go()
```
````

## 9. Ajouter un son de saut

Ajouter un bruitage est très simple. La première étape consiste à ajouter le fichier `.wav` souhaité dans le dossier `sounds` (à créer si nécessaire). Vous trouverez des sons `wav` sur <a href="https://mixkit.co/free-sound-effects/game/" target="_blank">Mixkit</a>. Privilégiez les sons courts pour éviter des problèmes de performance.

Pygame nous offre l'objet `sounds` qui nous permet de facilement lancer un bruitage. Dans notre cas, nous souhaitons lancer un son lorsque le joueur saute. Nous allons donc ajouter une ligne `sounds.jump.play()` quand on appuie sur la touche espace.

```python
def update():
    ...
    if keyboard.space:
        player.vy = -15
        sounds.jump.play() # Ajout du son de saut
    ...
```

`sounds.jump.play()` fait ici référence au nom du fichier son: `jump.wav`.

## 10. Ajouter une musique de fond

Ajouter une musique de fond est tout aussi simple ! Il suffit d'ajouter un fichier `.mp3` dans le dossier `music` (à créer) et d'utiliser l'objet `music` offert par Pygame. Vous trouverez des musiques `mp3` libres de droits sur <a href="https://incompetech.com/music/royalty-free/music.html" target="_blank">Incompetech</a>.

Pour lancer notre musique `ninja_music.mp3` au début du jeu, il reste qu'à appeler `music.play('ninja_music')` au début du programme principal.

```python
music.play('ninja_music') # Ajout de la musique ici !
player = Actor('run__000', (100, 400))
...
```

## 11. Améliorations possibles

```{admonition} Travail à rendre
Votre travail consiste à ajouter au minimum les améliorations suivantes au jeu:

* 2 améliorations faciles
* 1 amélioration moyenne
```

Voici plusieurs idées d'amélioration du jeu.  
Vous pouvez bien sûr me proposer d'autres idées et je vous dirai leur difficulté.

**Totalement dans vos cordes (facile):**

* Corriger le bug des sauts infinis. Le joueur ne devrait pouvoir sauter que s'il est au sol.
* Changer/Stopper l'animation du joueur en cours de saut.
* Créer un vrai écran de game over dans lequel on ne voit plus le jeu derrière mais un écran noir par exemple.
* Permettre de mettre le jeu en pause en appuyant sur une touche.
* Faire en sorte que les obstacles accélèrent progressivement quand le score augmente.
* Faire en sorte que l'on puisse changer la taille de la fenêtre de jeu dans le code (`WIDTH` et `HEIGHT`) et que tout s'adapte automatiquement.

**Un peu plus complexe (moyen):**

* Permettre de relancer le jeu du début après un game over en appuyant sur une touche.
* Ajouter un nouveau type d'obstacle pour lequel il faut rester au sol pour l'éviter.
* Changer aléatoirement l'image de l'obstacle à chaque fois qu'il réapparaît. Piochez dans les images fournies ou trouvez-en d'autres.
* Plusieurs obstacles peuvent apparaître en même temps. Indice: créez une liste d'obstacles.
* Permettre au joueur de ramasser des objets pour augmenter son score, par exemple des pièces.

**Challenging (difficile):**

* Permettre au joueur de tirer sur les obstacles pour les détruire.
* Donner de la vie au joueur lui permettant de prendre un certain nombre de coups avant de mourir. La vie du joueur est affichée et à chaque coup, le joueur est invincible pendant un courts laps de temps.
* Créer un menu avant le début du jeu qui permet de choisir la difficulté ou d'autres options.
* Créer un système de sauvegarde du score.
* Autres idées..?

## Travailler en dehors du TP

`````{admonition} Comment travailler en dehors du TP
:class: danger
````{dropdown} Depuis la maison
1. Téléchargez et installez [Python](https://www.python.org/downloads/).
2. Téléchargez et installez [Pycharm Community](https://www.jetbrains.com/fr-fr/pycharm/download/). Faites attention à prendre la version **Community** (en bas de la page) qui est gratuite.
3. Ouvrez Pycharm et créez un nouveau projet.
4. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet (PycharmProject).
5. Installez le package `pgzero`. Pour cela, ajoutez la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
````{dropdown} Depuis l'école
1. Ouvrez Pycharm et créez un nouveau projet.
2. Déplacez les fichiers et dossiers du jeu dans le dossier de votre projet (PycharmProject). **Attention**, si vous prenez votre dossier de travail depuis votre disque réseau (pxxxxx), il faudra le copier sur le bureau avant de le déplacer dans Pycharm.
3. Installez le package `pgzero`. Pour cela, ajoutez la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
`````
