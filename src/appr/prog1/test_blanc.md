(prog1.test_blanc)=

# Test blanc d'algorithmique

````{admonition} Exercice 1 - Max (facile)
:class: note
Ecrivez la fonction `calcule_max(liste)` qui retourne la valeur maximum d'une liste.

```{codeplay}
:file: ex_1.py
def calcule_min(liste):
    minimum = liste[0]
    for valeur in liste[1:]:
        if valeur < minimum:
            minimum = valeur
    return minimum

def calcule_max(liste):
    ...

liste = [3, 4, 1, 2, 6, 5]
minimum = calcule_min(liste)  
print(f'Le minimum est {minimum}')
maximum = ...
print(f'Le maximum est {maximum}')
```
````
