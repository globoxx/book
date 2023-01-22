(prog1.fonctions)=

# Les fonctions

[Mémento Python](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf)  
[Raccourcis clavier](https://support.apple.com/fr-ch/HT201236)

## C'est quoi une fonction ? 🤨

Python, comme tout autre langage de programmation, contient tout une séries de fonctions, c’est-à-dire **des instructions déjà définies qui font faire quelque chose de précis au programme**.
Nous en avons déjà utilisés deux au chapitre précédent, la fonction `print` qui affiche quelque chose à l’écran et la fonction `type` qui retourne le type d’un objet.

Elles permettent aux programmeurs de **gagner du temps en réutilisant du code déjà écrit (par quelqu'un d'autre)** 🙏

**L’appel d’une fonction s’effectue en indiquant la nom de la fonction, suivi d’une paires de parenthèses**.
Ces parenthèse contiennent les éventuels arguments de la fonction, c’est-à-dire les objets nécessaires pour que la fonction puisse être exécutée.
S’il y en a plusieurs, ces arguments sont séparés par des virgules.

```{codeplay}
print("Hello!")
type(56.8) # calcule le type de 56.8 (float) mais n'affiche rien
a = "rouge"
print(a)
type(a) # calcule le type de a (str) mais n'affiche rien
```

Dans l’exemple ci-dessus, chaque appel de fonction se fait en fournissant un argument.
Cet argument peut soit être une valeur donnée directement (comme dans les deux premières lignes), soit une variable (ligne 4-5).  
**Certaines fonctions prennent plus qu’un argument** comme la fonction `pow` qui calcule la puissance de deux nombres, et qui a donc besoin de deux arguments.

```{codeplay}
a = pow(2, 3) # calcule 2 puissance 3
print(a)
```

⚠️ Si vous ne donnez qu’un seul argument à la fonction `pow`, Python vous indiquera une erreur. ⚠️

**Souvent, les fonctions retournent une valeur qui contient le résultat de la fonction**.
Dans l’exemple ci-dessus, ce résultat (ici 8) est stocké dans la variable `a` puis affiché.
La fonction `print` a ceci de spécial qu’elle peut accueillir zéro, un, ou plusieurs arguments.
Chaque argument sera alors affiché et séparé par un espace.

```{codeplay}
a = 3
b = 5
print("a vaut", a, "et b vaut", b) # print a ici 4 arguments
print(f"a vaut {a} et b vaut {b}") # print a ici 1 seul argument (un string formaté)
```

Il est aussi possible d’utiliser ce qu’on appelle un **f-string** (pour string formaté) afin d’intégrer directement des variables à une chaîne de caractères.
Un string formaté a toujours la forme suivante : `f"...{var1}...{var2}..."` où `var1`, `var2`, etc sont des variables dont l’on veut afficher la valeur.  
Ainsi les 2 `print` de l'exemple précédent affichent la même chose.

> ### <span style="background-color:#c6d9f7"> Exercice 7 </span>
>
> Ecrivez un programme qui calcule 3.5 à la puissance 5 et qui affiche le résultat à l’aide d’une phrase commençant par "3.5 à la puissance 5 vaut ...".

> <details><summary markdown="span">Solution</summary>
> ```python
> resultat = pow(3.5, 5)
> # On pourrait aussi écrire: resultat = 3.5 ** 5
> print(f"3.5 à la puissance 5 vaut {resultat}")
> ```
> </details>

Python contient un grand nombre de fonctions, et la plupart d’entre elles sont organisées au sein de **modules**, qui ne sont rien d’autre que des **collections de fonctions**.  
Par exemple, le module `math` contient beaucoup de fonctions mathématiques 🤓, comme la fonction `sqrt` qui calcule la racine carrée (square root en anglais) d’un nombre.
Pour utiliser ces fonctions, il faut d’abord **importer le module** grâce à l'instruction `import`.

```{codeplay}
import math
a = math.sqrt(9) # calcule la racine carree
```

La première ligne de l’exemple ci-dessus indique que l’on va utiliser les fonctions du module `math`.
La seconde ligne utilise la fonction `sqrt` pour calculer la racine carrée de 9.
La description des fonctions du module `math` est disponible [ici](https://docs.python.org/fr/3/library/math.html){:target="_blank"}.

> ### <span style="background-color:#c6d9f7"> Exercice 8 </span>
>
> Trouvez dans le lien ci-dessus la fonction permettant de calculer le sinus d’un nombre.
> Ecrivez un programme calculant le sinus de 1 radian et affichant le résultat à l’écran.

> <details><summary markdown="span">Solution</summary>
> ```python
> import math
> a = math.sin(1) # la fonction sin attend des angles en radians
> print(a)
> ```
> Le [radian](https://fr.wikipedia.org/wiki/Radian){:target="_blank"} est l'unité d'angle du Système International.  
> PI radians équivaut à 180 degrés.
> </details>

## Les fonctions d'entrée (input)

Une des fonctions les plus utiles est la fonction `input(phrase)` qui affiche `phrase` dans le terminal et **retourne la chaîne de caractères que l’utilisateur ou l’utilisatrice écrit dans le terminal**.
Cela lui permet de donner des informations au programme, et le résultat du programme pourra ainsi dépendre des indications de la personne qui l’utilise 😉

```{codeplay}
nom = input("Entrez votre nom: ")
print(f"Bonjour {nom}")
```

Dans cet exemple, le programme va **demander** à la personne utilisatrice d’écrire son nom dans le terminal, puis assignera la chaîne de caractère entrée à la variable `nom`.
Il affiche ensuite "Bonjour" suivi du nom donné par la personne utilisatrice.

> ### <span style="background-color:#c6d9f7"> Exercice 9 </span>
> 
> Ecrivez un programme demandant d’abord le nom, puis le prénom de l’utilisateur ou l’utilisatrice et qui la salue ensuite avec son prénom et son nom.

> <details><summary markdown="span">Solution</summary>
> ```python
> nom = input("Entrez votre nom: ")
> prenom = input("Entrez votre prénom: ")
> print(f"Bonjour {prenom} {nom} !")
> ```
> </details>

Si l’on souhaite que l’utilisateur rentre un nombre, il faudra **convertir** la chaîne de caractère rentrée soit en un nombre entier avec la fonction `int`, soit en nombre à virgule avec la fonction `float`.

```{codeplay}
annee = int(input("Entrez votre annee de naissance: "))
age = 2022 - annee
print(f"Vous avez {age} ans cette annee !")
```

Si l’on n’appelle pas la fonction `int` dans la première ligne, `annee` sera une chaîne de caractère et la seconde ligne retournera une erreur car **Python ne sait pas comment soustraire une chaîne de caractère à un nombre** 😵 (faites le test !).

> ### <span style="background-color:#c6d9f7"> Exercice 10 </span>
> 
> Ecrivez un programme qui demande d’entrer un nombre et affiche le carré de ce nombre dans le terminal.

> <details><summary markdown="span">Solution</summary>
> ```python
> n = float(input("Entrez un nombre: "))
> resultat = n ** 2
> print(f"Le carré de {n} est {resultat}")
> ```
> Faire la conversion du texte en nombre avec la fonction `float` permet de gérer le cas où l'utilisateur entrerait un nombre à virgule.
> </details>

> ### <span style="background-color:#c6d9f7"> Exercice 11 </span>
> 
> Complétez et exécutez le programme suivant:
> ```
> r = float(input('Entrez le rayon du cercle: '))
> pi = 3.14
> diametre = ...
> circonference = ...
> surface = ...
> print() # Affiche une ligne vide
> print(f'rayon = {r}')
> print(f'diametre = {diametre}')
> print(f'circonference = {circonference}')
> print(f'surface = {surface}')
> ```
> (Rappel : La circonférence d’un cercle est égale à pi fois son diamètre.  
> La surface d’un cercle est égale à pi fois son rayon au carré.)

> <details><summary markdown="span">Solution</summary>
> ```python
> r = float(input('Entrez le rayon du cercle: '))
> pi = 3.14
> diametre = 2 * r
> circonference = pi * diametre
> surface = pi * r**2
> print()
> print(f'rayon = {r}')
> print(f'diametre = {diametre}')
> print(f'circonference = {circonference}')
> print(f'surface = {surface}')
> ```
> </details>

### Exercices Turtle 🐢 (facultatif)

> ### <span style="background-color:#A8D6C2"> Exercice Turtle 3 </span>

> Reprenez l’exercice Turtle du chapitre précédent mais permettez à l’utilisateur ou utilisatrice de choisir la taille de la maison grâce à la fonction prédéfinie `input`.

> <details><summary markdown="span">Solution</summary>
> ```python
> import turtle # Importe le module
> 
> d = int(input("Entrez la taille de la maison: ")) # On demande à l'utilisateur la taille de la maison
> 
> # On dessine le carré
> turtle.forward(d) # Avance de 100 pixels
> turtle.left(90) # Tourne a gauche de 90 degres
> turtle.forward(d)
> turtle.left(90)
> turtle.forward(d)
> turtle.left(90)
> turtle.forward(d)
> turtle.left(90)
> 
> # On se déplace au sommet du carré
> turtle.left(90)
> turtle.forward(d)
> turtle.right(90)
> 
> # On dessine le triangle
> turtle.forward(d) # Avance de 100 pixels
> turtle.left(120) # Tourne a gauche de 120 degres (180-60)
> turtle.forward(d)
> turtle.left(120)
> turtle.forward(d)
> turtle.left(120)
> 
> turtle.done() # Termine le dessin
> ```
> </details>

---

[Retour à l'accueil](../README.md)