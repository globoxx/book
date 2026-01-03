(prog_jeu.intro_pygame)=

# 2. Introduction à Pygame
Pygame est une bibliothèque Python permettant de créer des jeux vidéo en 2D. Elle fournit des fonctionnalités pour gérer les fenêtres, les événements, les images, les sons, et bien plus encore.
Voici un exemple simple de code Pygame qui dessine un paysage avec des montagnes, un soleil, des nuages et des fleurs aléatoires.

```{codeplay}
:file: p00_4.py
import pygame
import random
from pygame.locals import *
from sys import exit
# Initialisation de Pygame
pygame.init()
# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paysage avec Pygame")
# Fonction pour dessiner un rectangle
def rectangle(x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
# Fonction pour dessiner une montagne
def montagne(base, color):
    points = [(0, 600), (base/2, 600 - base), (base, 600)]
    pygame.draw.polygon(screen, color, points)
# Fonction pour dessiner le soleil
def soleil(radius, rayons, distance):
    pygame.draw.circle(screen, (255, 255, 0), (700, 100), radius)
    for i in range(rayons):
        angle = i * (360 / rayons)
        x_end = 700 + distance * pygame.math.cos(pygame.math.radians(angle))
        y_end = 100 + distance * pygame.math.sin(pygame.math.radians(angle))
        pygame.draw.line(screen, (255, 255, 0), (700, 100), (x_end, y_end), 2)
# Fonction pour dessiner un nuage
def nuage(radius, n):
    for i in range(n):
        offset_x = random.randint(-radius, radius)
        offset_y = random.randint(-radius//2, radius//2)
        pygame.draw.circle(screen, (255, 255, 255), (offset_x + 0, offset_y + 0), radius)
# Fonction pour dessiner une fleur
def fleur(d, n, c_centre, c_petale):
    # Dessine une fleur avec un centre de diamètre d et de couleur c_centre avec n pétales de couleur c_petale
    center_x, center_y = 400, 500
    for i in range(n):
        angle = i * (360 / n)
        petal_x = center_x + (d * 0.8) * pygame.math.cos(pygame.math.radians(angle))
        petal_y = center_y + (d * 0.8) * pygame.math.sin(pygame.math.radians(angle))
        pygame.draw.circle(screen, c_petale, (int(petal_x), int(petal_y)), d // 2)
    pygame.draw.circle(screen, c_centre, (center_x, center_y), d // 2)
# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    # Dessin du paysage
    screen.fill((135, 206, 235))  # Ciel bleu
    rectangle(0, 400, 800, 200, (34, 139, 34))  # Herbe verte
    montagne(200, (169, 169, 169))  # Montagne grise
    montagne(150, (211, 211, 211))  # Montagne claire
    montagne(250, (192, 192, 192))  # Montagne argentée
    soleil(50, 10, 80)  # Soleil
    nuage(40, 5)  # Nuage
    for i in range(50):  # 50 fleurs aléatoires
        x = random.randint(0, 800)
        y = random.randint(400, 600)
        fleur(20, 6, (255, 215, 0), (255, 0, 255))
    pygame.display.update()
```