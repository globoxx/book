(prog_jeu.rappels)=

# 1. Rappels de programmation

## Exercice 1 - Afficher du texte

Écrivez un programme qui affiche "Salut" suivi de votre prénom.
Rappel: la fonction `print(texte)` permet d'afficher un `texte` donné.

```{codeplay}



```

````{dropdown} Solution possible
```{codeplay}
print("Salut Alice")  # Remplacez "Alice" par votre prénom
```
````

## Exercice 2 - Afficher le résultat d'un calcul

Ecrivez un programme qui affiche le résultat de la multiplication de 15 et 27.

```{codeplay}



```

````{dropdown} Solution possible
```{codeplay}
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
```{codeplay}
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
```{codeplay}
largeur = 5
hauteur = 10
aire = largeur * hauteur
print("L'aire du rectangle est", aire)
```
````

## Exercice 5 - Ajouter une condition

Écrivez un programme qui demande à l'utilisateur son âge et qui affiche "Vous êtes majeur" si l'âge est au moins 18 ans, ou "Vous êtes mineur" sinon.

La partie du code qui demande l'âge et stocke la réponsedans une variable `age` vous est fournie.

```{dropdown} Aide sur les conditions
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
```

```{codeplay}
age = int(input("Quel âge avez-vous ? "))


```

````{dropdown} Solution possible
```{codeplay}
age = int(input("Quel âge avez-vous ? "))
if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
```
````

## Exercice 6 - Utiliser une boucle pour parcourir des nombres

Ecrivez un programme qui affiche les nombres de `0` à `49` en utilisant une boucle `for`.

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
```{codeplay}
for i in range(50):
    print(i)
```
````

## Exercice 7 - Utiliser une boucle pour parcourir une liste

Ecrivez un programme qui affiche chaque prénom d'une liste de prénoms. La liste est fournie dans la variable `prenoms`.

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
```{codeplay}
prenoms = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for prenom in prenoms:
    print(prenom)
```
````

## Exercice 8 - Utiliser une fonction

Ecrivez un programme qui définit une fonction `carre(x)` qui prend un nombre `x` en paramètre et qui affiche le carré de ce nombre (c'est-à-dire `x` multiplié par lui-même).

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
```{codeplay}
def carre(x):
    print(x * x)

carre(3)  # Affiche 9
carre(5)  # Affiche 25
carre(10) # Affiche 100
```
````

## Exercice 9 - Ecrire la fonction max

Écrivez un programme qui définit une fonction `max(a, b)` qui prend 2 nombres `a` et `b` en paramètres et qui affiche le plus grand des deux.

Testez la fonction `max(a, b)` en l'appelant avec différentes valeurs pour `a` et `b`.

```{codeplay}



```

````{dropdown} Solution possible
```{codeplay}
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


## Exercice 10 - Ecrire la fonction somme

Ecrivez un programme qui définit une fonction `somme(n)` qui prend un nombre entier `n` en paramètre et qui retourne la somme des entiers de 1 à `n`. Par exemple, `somme(5)` doit retourner `1 + 2 + 3 + 4 + 5 = 15`.

Vous pouvez utiliser une boucle `for` pour parcourir les entiers de 1 à `n`.

Testez la fonction `somme(n)` en l'appelant avec différentes valeurs pour `n`.

```{codeplay}



```

````{dropdown} Solution possible
```{codeplay}
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
