(prog1.algo)=

[Mémento Python](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf)  
[Raccourcis clavier](https://support.apple.com/fr-ch/HT201236)

# Les algorithmes

Dans ce chapitre, nous allons découvrir quelques algorithmes à appliquer sur des listes. Nous allons surtout nous pencher sur le tri qui est une fonctionnalité fondamentale dans l’informatique. Le succès énorme de Google est basé sur un tri efficace de l’information, car dans une liste triée on peut trouver un élément beaucoup plus vite. Nous allons voir que :

- la fonction `min(liste)` retourne le minimum,
- la fonction `max(liste)` retourne le maximum,
- la méthode `liste.sort()` trie une liste.

## Fonctions min et max

Les fonctions `min()` et `max()` retournent le minimum et le maximum d'une liste à l'aide d'un algorithme.  
Mais comment fonctionne cet algorithme ?

```{codeplay}
:file: sort1.py
liste = [3, 4, 1, 2, 6, 5]

print(min(liste))
print(max(liste))
```

Ces fonctions sont très utiles mais nous allons voir comment les créer nous-mêmes !
Pour trouver le minimum dans une liste il faut :

- prendre la première valeur comme minimum courant,
- parcourir le reste de la liste,
- garder la valeur comme nouveau minimum si elle est plus petite.

```{codeplay}
:file: sort2.py
def calcule_min(liste):
    minimum = liste[0]
    for valeur in liste[1:]:
        if valeur < minimum:
            minimum = valeur
    return minimum

liste = [3, 4, 1, 2, 6, 5]
minimum = calcule_min(liste)  
print(minimum)
```

```{admonition} Exercice
:class: note
Ecrivez la fonction `calcule_max(liste)` qui retourne la valeur maximum d'une liste.
```

## L'index du minimum

Souvent, on ne doit pas seulement trouver la valeur minimum, mais aussi sa position (son index) dans la liste.  
Contrairement au cas précédent, ici nous ne parcourons pas les valeurs, mais les index.

```{codeplay}
:file: sort6.py
liste = [3, 4, 1, 2, 6, 5]

minimum = liste[0]
index_minimum = 0
n = len(liste)

for i in range(1, n):
    if liste[i] < minimum:
        minimum = liste[i]
        index_minimum = i
        
print(f"Le minimum est {minimum} et se trouve à l'index {index_minimum}")
```

```{admonition} Exercice
:class: note
Modifier l'exemple précédent pour également afficher le maximum et son index.
```

## Échanger deux éléments

Pour échanger deux éléments d'une liste, nous pouvons utiliser une variable temporaire pour stocker une valeur.
Ici nous échangeons les deux premiers éléments, donc les éléments avec les index 0 et 1.

```{codeplay}
:file: sort7.py
liste = [3, 4, 1, 2, 6, 5]

print(liste)
tmp = liste[0]  # On stocke la valeur de liste[0] car elle sera écrasée par liste[1]
liste[0] = liste[1]
liste[1] = tmp
print(liste)
```

Le programme devient plus lisible si nous définissons une fonction `echange()`.

```{codeplay}
:file: sort8.py
liste = [3, 4, 1, 2, 6, 5]

def echange(liste, i, j):
    tmp = liste[i]
    liste[i] = liste[j]
    liste[j] = tmp

print(liste)
echange(liste, 0, 2)
print(liste)
```

````{caution}
**Pour aller plus loin**  
Il est également possible d'échanger la valeur de 2 variables en utilisant une **affectation multiple**.
```python
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
```
````

## Tri à bulles

L’algorithme du **tri à bulles** compare les éléments voisins, deux par deux, et les met dans le bon ordre. Le mot 'bulles' fait référence aux bulles dans une boisson qui montent à la surface exactement comme les grands éléments remontent progressivement vers la fin de la liste.

```{codeplay}
:file: sort8.py
def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]
===
def bubble_sort(liste):
    N = len(liste)
    for iteration in range(N - 1):
        for i in range(N - 1):
            x = liste[i]
            voisin = liste[i + 1]
            if liste[i] > liste[i+1]:
                echange(liste, i, i+1)
    return liste

liste = [3, 4, 1, 2, 6, 5]
print(liste)
liste = bubble_sort(liste)
print(liste)
```

```{codeplay}
---
hints: |
    Rappelle toi de l'opérateur `**`!
    ===
    Toujours pas?
---
def test(condition, erreur):
     if not condition:
        print(erreur)
===
def puissance(n, m):
    pass
===
test(puissance(2, 3) == 8, "Oups, ton implémentation est incorrecte.", "Yes tout à fait correct !")
```
