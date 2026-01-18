(prog_jeu.rappels)=

# 1. Rappels de programmation

## Exercice 1 - Afficher du texte

Écrivez un programme qui affiche "Salut" suivi de votre prénom.
Rappel: la fonction `print(texte)` permet d'afficher un `texte` donné.

```{codeplay}



```

````{dropdown} Solution possible
```python
print("Salut Alice")  # Remplacez "Alice" par votre prénom
```
````

## Exercice 2 - Afficher le résultat d'un calcul

Écrivez un programme qui affiche le résultat de la multiplication de 15 et 27.

```{codeplay}



```

````{dropdown} Solution possible
```python
print(15 * 27)
```
````

## Exercice 3 - Utiliser une variable

Écrivez un programme qui stocke votre âge dans une variable `age` et qui affiche "J'ai X ans", où X est la valeur de la variable `age`.

La fonction `print()` peut afficher plusieurs éléments séparés par des virgules. Par exemple:

```python
print("Bonjour", "Bob", "!")  # Affiche "Bonjour Bob !"
```

````{dropdown} Aide sur les variables
Une variable est un nom qui permet de stocker une valeur. Par exemple, pour stocker le nombre 10 dans une variable nommée `nombre`, on écrit:

```python
nombre = 10
print(nombre) # Affiche 10
```
Cette variable peut ensuite évoluer dans le programme:
```python
nombre = nombre + 5  # On ajoute 5 à la valeur actuelle de la variable
print(nombre)  # Affiche 15
```
````

```{codeplay}



```

````{dropdown} Solution possible
```python
age = 25  # Remplacez 25 par votre âge
print("J'ai", age, "ans")
```
````

## Exercice 4 - Faire un calcul avec des variables

Écrivez un programme qui stocke dans une variable `largeur` la valeur 5 et dans une variable `hauteur` la valeur 10.  
Le programme doit ensuite calculer l'aire du rectangle (largeur × hauteur) et l'afficher. 

```{codeplay}



```

````{dropdown} Solution possible
```python
largeur = 5
hauteur = 10
aire = largeur * hauteur
print("L'aire du rectangle est", aire)
```
````

## Exercice 5 - Ajouter une condition

Écrivez un programme qui demande à l'utilisateur son âge et qui affiche "Vous êtes majeur" si l'âge est au moins 18 ans, ou "Vous êtes mineur" sinon.

La partie du code qui demande l'âge et stocke la réponsedans une variable `age` vous est fournie.

````{dropdown} Aide sur les conditions
Une condition permet d'exécuter un bout de code seulement si une certaine situation est vraie. Par exemple, pour vérifier si un nombre est positif:

```python
nombre = 10
if nombre > 0:  # Si le nombre est supérieur à 0
    print("Le nombre est positif")  # On affiche ce message
elif nombre < 0:  # Sinon si le nombre est inférieur à 0
    print("Le nombre est négatif")  # On affiche un autre message
else:  # Sinon (le nombre est forcément égal à 0)
    print("Le nombre est nul")  # On affiche un autre message
```

On peut utiliser les opérateurs de comparaison suivants:
- `==` : égal à
- `!=` : différent de
- `<`  : inférieur à
- `>`  : supérieur à
- `<=` : inférieur ou égal à
- `>=` : supérieur ou égal à

On peut aussi combiner plusieurs comparaisons avec les opérateurs logiques:
- `and` : et
- `or`  : ou
- `not` : non   
````

```{codeplay}
age = int(input("Quel âge avez-vous ? "))


```

````{dropdown} Solution possible
```python
age = int(input("Quel âge avez-vous ? "))
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
```
````

## Exercice 6 - Utiliser une boucle pour parcourir des nombres

Écrivez un programme qui affiche les nombres de `0` à `49` en utilisant une boucle `for`.

````{dropdown} Aide sur les boucles qui parcourent des nombres
Une boucle permet de répéter un bout de code plusieurs fois. Par exemple, pour afficher les nombres de 0 à 4:

```python
for i in range(5):  # Pour chaque nombre i de 0 à 4
    print(i)        # On affiche i
```

La fonction `range(n)` génère les nombres de `0` à `n-1`.  
On peut aussi spécifier plus précisément un début et une fin:

```python
for i in range(3, 8):  # Pour chaque nombre i de 3 à 7
    print(i)           # On affiche i
```

La fonction `range(a, b)` génère les nombres de `a` à `b-1`.
`````

```{codeplay}



```

````{dropdown} Solution possible
```python
for i in range(50):
    print(i)
```
````

## Exercice 7 - Utiliser une boucle pour parcourir une liste

Écrivez un programme qui affiche chaque prénom d'une liste de prénoms. La liste est fournie dans la variable `prenoms`.

````{dropdown} Aide sur les boucles qui parcourent des listes
Une liste est une collection ordonnée d'éléments. Par exemple, pour créer une liste de mots:

```python
mots = ["pomme", "banane", "cerise"]
```
On peut parcourir chaque élément d'une liste avec une boucle `for`:

```python
for mot in mots:  # Pour chaque élément mot dans la liste mots
    print(mot)    # On affiche mot
```
````

```{codeplay}
prenoms = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

```

````{dropdown} Solution possible
```python
prenoms = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for prenom in prenoms:
    print(prenom)
```
````

## Exercice 8 - Utiliser une boucle while

Écrivez un programme qui demande à l'utilisateur de deviner un mot de passe (par exemple, "42"). Le programme doit continuer à demander tant que l'utilisateur n'a pas trouvé le bon mot de passe. Lorsqu'il trouve le bon, le programme doit afficher "Tu peux passer !".

````{dropdown} Aide sur les boucles while
Une boucle `while` permet de répéter un bout de code tant qu'une certaine condition est vraie. Par exemple, pour afficher les nombres de 0 à 4:

```python
i = 0
while i < 5:          # Tant que i est inférieur à 5
    print(i)         # On affiche i
    i = i + 1       # On augmente i de 1
```

Elle est utile lorsque l'on ne sait pas à l'avance combien de fois on devra répéter le code. C'est l'inverse d'une boucle `for` qui répète un nombre fixe de fois.
````

```{codeplay}



```

````{dropdown} Solution possible
```python
mot_de_passe = ""
while mot_de_passe != "42":          # Tant que le mot de passe est incorrect
    mot_de_passe = input("Entrez le mot de passe : ")  # On demande un nouveau mot de passe
print("Bravo")  # On affiche un message de félicitation
```
````

## Exercice 9 - Utiliser une fonction

Écrivez un programme qui définit une fonction `carre(x)` qui prend un nombre `x` en paramètre et qui affiche le carré de ce nombre (c'est-à-dire `x` multiplié par lui-même).

Testez la fonction `carre(x)` en l'appelant avec différentes valeurs pour `x`.

````{dropdown} Aide sur les fonctions
Une fonction est un bout de code que l'on peut réutiliser plusieurs fois. Par exemple, pour définir une fonction qui affiche un message de bienvenue:

```python
def bienvenue():  # Définition de la fonction bienvenue
    print("Bienvenue dans le programme !")

bienvenue()  # Appel de la fonction bienvenue
```

Pour définir une fonction qui prend des paramètres:

```python
def saluer(nom):  # Définition de la fonction saluer avec un paramètre
    print("Bonjour", nom)

saluer("Alice")  # Appel de la fonction saluer avec "Alice" comme paramètre
```
````

```{codeplay}



```

````{dropdown} Solution possible
```python
def carre(x):
    print(x * x)

carre(3)  # Affiche 9
carre(5)  # Affiche 25
carre(10) # Affiche 100
```
````

## Exercice 10 - Ecrire la fonction max

Écrivez un programme qui définit une fonction `max(a, b)` qui prend 2 nombres `a` et `b` en paramètres et qui affiche le plus grand des deux.

Testez la fonction `max(a, b)` en l'appelant avec différentes valeurs pour `a` et `b`.

```{codeplay}



```

````{dropdown} Solution possible
```python
def max(a, b):
    if a > b:
        print(a)
    else:
        print(b)

max(10, 5)  # Affiche 10
max(-3, -7)   # Affiche -3
max(4, 4)   # Affiche 4
```
````


## Exercice 11 - Ecrire la fonction somme

Écrivez un programme qui définit une fonction `somme(n)` qui prend un nombre entier `n` en paramètre et qui retourne la somme des entiers de 1 à `n`. Par exemple, `somme(5)` doit retourner `1 + 2 + 3 + 4 + 5 = 15`.

Vous pouvez utiliser une boucle `for` pour parcourir les entiers de 1 à `n`.

Testez la fonction `somme(n)` en l'appelant avec différentes valeurs pour `n`.

```{codeplay}



```

````{dropdown} Solution possible
```python
def somme(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(somme(5))  # Affiche 15
print(somme(10)) # Affiche 55
print(somme(1000))  # Affiche 500500
```
````

## Exercice 12 - Utiliser l'aléatoire
Écrivez un programme qui tire un nombre entier aléatoire entre 1 et 10 (inclus) et qui demande à l'utilisateur de deviner ce nombre. Le programme doit continuer à demander tant que l'utilisateur n'a pas trouvé le bon nombre. Lorsqu'il trouve le bon, le programme doit afficher "Bravo !".

````{dropdown} Aide sur l'aléatoire
Le module `random` permet de faire de l'aléatoire. Pour tirer un nombre entier aléatoire entre `a` et `b` (inclus), on utilise la fonction `random.randint(a, b)`.

```python
import random  # Pour utiliser l'aléatoire
nombre_aleatoire = random.randint(1, 100)  # Tire un nombre aléatoire entre 1 et 100
```

Pour tirer un élément aléatoire dans une liste, on utilise la fonction `random.choice(liste)`.

```python
import random  # Pour utiliser l'aléatoire
couleurs = ["rouge", "vert", "bleu"]
couleur_aleatoire = random.choice(couleurs)  # Tire une couleur aléatoire dans la liste
````

```{codeplay}
import random  # Pour utiliser l'aléatoire

```

````{dropdown} Solution possible
```python
import random  # Pour utiliser l'aléatoire
nombre_a_deviner = random.randint(1, 10)  # Tire un nombre aléatoire entre 1 et 10
nombre_devine = 0
while nombre_devine != nombre_a_deviner:
    nombre_devine = int(input("Devinez le nombre (entre 1 et 100) : "))
print("Bravo ! Vous avez trouvé le nombre", nombre_a_deviner)
```
````

## Challenges sans solution

Si vous pensez être à l'aise avec toutes les notions de l'année passée, vous pouvez faire vos premiers pas avec <a href="https://globox.pythonanywhere.com/static/prog_jeu/runner_new.html" target="_blank">Pygame</a>.

Sinon si vous cherchez des challenges plus intéressants, les exercices suivants sont un peu plus difficiles. Ils n'ont pas de solution fournie, mais vous pouvez me demander de vérifier votre solution en cas de doute.

### Choix 1 - Plus ou Moins
Écrivez un programme permettant de jouer au jeu du "Plus ou Moins". Le programme doit générer un nombre aléatoire entre 1 et 100 (inclus), puis demander à l'utilisateur de deviner ce nombre.  
Après chaque proposition de l'utilisateur, le programme doit indiquer si le nombre à deviner est plus grand ou plus petit que la proposition. Le jeu continue jusqu'à ce que l'utilisateur trouve le bon nombre.  
À la fin, le programme doit afficher le nombre de tentatives effectuées par l'utilisateur pour trouver le bon nombre.

### Choix 2 - Pierre, Feuille, Ciseaux
Écrivez un programme permettant de jouer au jeu du "Pierre, Feuille, Ciseaux" contre l'ordinateur. Le programme doit demander à l'utilisateur de choisir entre "pierre", "feuille" ou "ciseaux". L'ordinateur doit faire un choix aléatoire parmi ces trois options.  
Le programme doit ensuite déterminer le gagnant selon les règles suivantes:
- La pierre écrase les ciseaux (la pierre gagne)
- Les ciseaux coupent la feuille (les ciseaux gagnent)
- La feuille enveloppe la pierre (la feuille gagne)
Le programme doit afficher le choix de l'utilisateur, le choix de l'ordinateur, et le résultat de la partie (victoire, défaite ou égalité).  
Le jeu peut être répété autant de fois que l'utilisateur le souhaite et compte les points pour chaque joueur.

### Choix 3 - Jeu du pendu
Écrivez un programme permettant de jouer au jeu du pendu. Le programme doit choisir un mot aléatoire dans une liste prédéfinie de mots. Le joueur doit deviner le mot en proposant des lettres une par une.  
Le programme doit afficher l'état actuel du mot à deviner, en remplaçant les lettres non encore devinées par des underscores (_). Le joueur a un nombre limité de tentatives (par exemple, 6) pour deviner toutes les lettres du mot.  
Après chaque proposition de lettre, le programme doit indiquer si la lettre est présente dans le mot ou non, et mettre à jour l'état du mot en conséquence.  
Le jeu se termine lorsque le joueur devine le mot complet ou lorsqu'il n'a plus de tentatives restantes. Le programme doit afficher un message de victoire ou de défaite en conséquence.

### Choix 4 - Simulateur de Blackjack 21
Écrivez un programme qui simule une partie simplifiée de Blackjack 21. Le joueur commence avec un score de 0 et, à chaque tour de jeu, il peut choisir de "tirer" une carte (ajouter un nombre aléatoire entre 1 et 11 à son score) ou de "rester" (terminer la manche). Le but est d'atteindre un score total aussi proche que possible de 21 sans le dépasser. S'il est dépassé, le score retombe à 0 et la manche s'arrête. Le score est alors converti en jetons et donné aux joueurs qui peut choisir de rejouer en misant par exemple 15 jetons.

### Zone de codage (ou utilisez un éditeur externe)
```{codeplay}



```

