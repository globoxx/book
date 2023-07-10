(prog_formel.definitions)=

# 4. Définition de fonctions

<a href="https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf" target="_blank">Mémento Python</a>  
<a href="https://support.apple.com/fr-ch/HT201236" target="_blank">Raccourcis clavier</a>

## Définir ses propres fonctions

Il est souvent utile d’écrire ses propres fonctions, **afin de ne pas avoir à écrire plusieurs fois le même bout de code**🙏  
En programmation, le concept de fonction n’est pas exactement le même qu’en mathématiques.
Il faut plutôt le voir comme un **sous-programme auquel on fournit des objets et qui peut en retourner d’autres**.

Pour définir une fonction, il faut indiquer les éléments suivants :

1. Le mot-clé `def` suivi du nom de la fonction puis de deux points (:).
2. Les **arguments**, ou paramètres, qui indiquent quels sont **les objets à fournir** à la fonction pour que le programme puisse l’exécuter. Certaines fonctions ne prennent aucun argument.
3. La liste des instructions de la fonction, autrement dit, le sous-programme effectué par la fonction. La liste des instructions est indentée par rapport au programme principal, c’est-à-dire qu’elle est **décalée à droite**. Une liste d’instruction est aussi appelée un **bloc d’instruction**.
4. Dans le cas où la fonction retourne un résultat, il est nécessaire d’utiliser le mot-clé `return` suivi de l’objet à retourner.

Ces quatre éléments constituent la définition de la fonction.
**Une fois une fonction ainsi définie, on peut l’utiliser (l’appeler) autant de fois que l’on désire dans un programme** 🤩

Voici la syntaxe générale pour définir une fonction et l'appeler :

```python
def nom_de_votre_fonction(argument1, argument2, ...):
	...
	# bloc d'instruction
	...
	# return resultat (optionnel)

nom_de_votre_fonction(arg1, arg2, ...)  # Appel de la fonction
...
nom_de_votre_fonction(argx, argy, ...)  # Un autre appel de la fonction (avec des arguments différents)
```

⚠️ Rappelez-vous de ceci ⚠️ :

1. On définit une fonction qu’une seule fois.
2. On appelle une fonction autant de fois que l’on veut.
3. Si on ne l’appelle pas, la fonction n’est pas exécutée.

```{codeplay}
def au_cube(n):
	cube = n**3
	return cube
	
a = au_cube(2)
b = au_cube(5)
print(f"Les cubes de 2 et 5 sont {a} et {b}")
```

L’exemple ci-dessus montre la définition d’une fonction nommée `au_cube` prenant 1 argument et retournant le cube de cet argument.

````{admonition} Exercice 12
:class: note
Ecrivez une fonction `au_carre(n)` qui calcule le carré d’un nombre et le retourne.  
Utilisez cette fonction pour calculer et afficher le carré des nombres 6, -5 et 573.28.

```{codeplay}
:file: ex_12.py
def au_carre(n):
    ...

a = au_carre(6)
b = au_carre(-5)
c = au_carre(573.28)
print(f"Les carrés de 6, -5 et 573.28 sont {a}, {b} et {c}")
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_12.py
def au_carre(n):
    carre = n**2
    return carre

a = au_carre(6)
b = au_carre(-5)
c = au_carre(573.28)
print(f"Les carrés de 6, -5 et 573.28 sont {a}, {b} et {c}")
```
Evidemment, cette fonction n'est pas très utile car elle reproduit simplement l'opération `n**2`😅
````
`````

L’exemple suivant montre la définition d’une fonction qui ne **retourne aucune valeur**: la fonction ne se termine pas par le mot-clé `return`.  
La fonction s’exécute (ici elle affiche des choses) mais ne retourne rien.

```{codeplay}
def saluer(prenom, nom):
	print(f"Bonjour {prenom} {nom}")
	print("Bienvenue !")

saluer("Pierre", "Schmutz")
```

Notez que les arguments doivent être donnés **dans le même ordre que dans la définition** de la fonction afin que le programme sache quelle entrée correspond à quel argument.

````{admonition} Exercice 13
:class: note
Modifiez l’exemple ci-dessus pour ajouter un troisième argument de votre choix à la fonction `saluer()`.  
Faites en sorte que la fonction utilise ce nouvel argument dans son message de bienvenue puis appelez la fonction.

```{codeplay}
:file: ex_13.py
def saluer(prenom, nom, ...):
    ...

saluer(...)
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_13.py
def saluer(prenom, nom, age):
    print(f"Bonjour {prenom} {nom} qui a {age} ans !")
    print("Bienvenue !")

saluer("Pierre", "Schmutz", 34)
```
````
`````

L’exemple ci-dessous montre une fonction prenant en arguments le rayon et la hauteur d’un cylindre afin d’en retourner le volume 🤓

```{codeplay}
def volume_cylindre(rayon, hauteur):
	vol = 3.14 * rayon**2 * hauteur
	return vol

v1 = volume_cylindre(2.3, 10)
v2 = volume_cylindre(1.2, 5)
print(f"Le volume des cylindres est de {v1} et {v2}")
```

````{admonition} Exercice 14
:class: note
L’indice de masse corporelle (IMC) d’une personne est donné par son poids (en kg) divisé par le carré de sa taille (en mètres).
Ecrivez une fonction qui prend le poids et la taille en argument et retourne l’IMC.  
Utilisez cette fonction dans un programme qui demande son poids et sa taille à l’utilisateur et affiche son IMC dans le terminal.  

**Exemple d’exécution :**
```
Entrez votre poids (kg) : 84
Entrez votre taille (m) : 1.84
Votre IMC est de 24.810964083175
```
L'IMC n'est q'un indicateur et ne permet absolument pas, à lui seul, de déterminer l'état de santé d'une personne.

```{codeplay}
:file: ex_14.py
def calcule_imc(...):
    ...

poids = ...
taille = ...
imc = ...

print(f"Votre IMC est de {imc}")
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: ex_14.py
def calcule_imc(poids, taille):
    imc = poids / taille**2
    return imc

poids = float(input("Entrez votre poids (kg): "))
taille = float(input("Entrez votre taille (m): "))
imc = calcule_imc(poids, taille)

print(f"Votre IMC est de {imc}")
```
Gardez à l'esprit qu'une fois que vous avez choisi un nom pour une fonction ou une variable, vous ne pouvez pas utiliser ce nom pour une autre fonction ou variable.
````
`````

## Exercices Turtle 🐢 (facultatif)

````{admonition} Exercice - Une maison fonctionnelle
:class: note
Il est temps d’améliorer notre code permettant de dessiner une maison grâce aux fonctions ! 🤩
1. Ecrivez une fonction `carre(taille)` qui dessine un carré de la taille passée en argument.
2. Ecrivez une fonction `triangle(taille)` qui dessine un triangle équilatéral avec la taille passée en argument.
3. Enfin, écrivez une fonction `maison(taille)` qui appelle les 2 fonctions précédentes pour dessiner une maison de la taille passée en argument.

```{codeplay}
:file: maison_fonctionnelle.py
import turtle # Importe le module

# Fonction qui dessine un carré de taille d
def dessine_carre(d):
    ...

# Fonction qui dessine un triangle de taille d
def dessine_triangle(d):
    ...

# Fonction qui dessine une maison de taille d
def dessine_maison(d):
    ...

# On demande à l'utilisateur la taille de la maison
d = int(input("Entrez la taille de la maison: "))

# Appelez la fonction dessine_maison() ici
...

turtle.done() # Termine le dessin
```
````

`````{admonition} Solution
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down
```{codeplay}
:file: maison_fonctionnelle.py
import turtle # Importe le module

# Fonction qui dessine un carré de taille d
def dessine_carre(d):
    turtle.forward(d) # Avance de 100 pixels
    turtle.left(90) # Tourne a gauche de 90 degres
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(90)

# Fonction qui dessine un triangle de taille d
def dessine_triangle(d):
    turtle.forward(d) # Avance de 100 pixels
    turtle.left(120) # Tourne a gauche de 120 degres (180-60)
    turtle.forward(d)
    turtle.left(120)
    turtle.forward(d)
    turtle.left(120)

# Fonction qui dessine une maison de taille d
def dessine_maison(d):
    # On dessine le carré
    dessine_carre(d)

    # On se déplace au sommet du carré
    turtle.left(90)
    turtle.forward(d)
    turtle.right(90)

    # On dessine le triangle
    dessine_triangle(d)

d = int(input("Entrez la taille de la maison: ")) # On demande à l'utilisateur la taille de la maison

# On dessine la maison de taille d
dessine_maison(d)

# Il est ensuite très facile de dessiner d'autres maisons de tailles variables
turtle.up() # Permet de lever le stylo
turtle.goto(125, 125) # Se déplace à ces coordonnées
turtle.down() # Permet de recommencer à dessiner
dessine_maison(d/2)

turtle.up()
turtle.goto(-250, -250)
turtle.down()
dessine_maison(d*2)

turtle.done() # Termine le dessin
```
````
`````
