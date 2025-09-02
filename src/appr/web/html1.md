(web.html1)=

# 1. Introduction à l'HTML

Le HTML (HyperText Markup Language) a fait son apparition dès 1991 au lancement du Web par Tim Berners-Lee. Son rôle est de **structurer** le contenu d'une page web.  
Il permet d'ajouter du texte, des liens, des images, des tableaux, etc.

```{panels}

:img-top: ../media/berners.jpg

Tim Berners-Lee 🇬🇧
^^^^^
***Né en 1955***

L'informaticien britannique [**Tim Berners-Lee**](https://fr.wikipedia.org/wiki/Tim_Berners-Lee) est le principal inventeur du Web alors qu'il travaillait au CERN à Genève dans les années 90. Il a inventé les adresses URL, le protocole HTTP et le langage HTML.

----
:img-top: ../media/html.png
HTML5
^^^^^
***Créé en 1991***

HTML5 (HyperText Markup Language 5) est la dernière révision majeure du [**HTML**](https://fr.wikipedia.org/wiki/HTML5) (format de données conçu pour représenter les pages web). Cette version a été finalisée le 28 octobre 2014.
```

```{admonition} À retenir
:class: attention
HTML est un langage de description, pas de programmation ! Il n'est pas possible de faire de logique en HTML.
```

## Le Web n'est qu'HTML (et quelques autres trucs)

Quand vous visitez un site web, le serveur du site vous transmet en réalité un fichier HTML qui sera lu et interprété par votre navigateur.

```{image} ../media/web_html.png
```

Ce fichier se trouve alors chez vous, sur votre ordinateur, et il est possible de le lire et le modifier depuis le navigateur en faisant un clic droit sur la page et en choisissant "Inspecter l'élément" ou "Afficher le code source de la page".

<!--
````{admonition} Micro-activité
:class: note
Ouvrez Firefox et rendez-vous sur un site web de votre choix, faites un clic droit sur la page et cliquez sur "Enregistrez sous..." pour sauver le fichier html sur votre ordinateur.  
Vous observez que votre navigateur télécharge un fichier `.html` que vous pouvez ouvrir à nouveau dans votre navigateur (double clic).

La page est-elle identique à tout à l'heure ? A quoi ressemble l'url de la page ?

```{dropdown} Réponse
En général, elle sera toute moche ! Car vous ne téléchargez que le fichier `.html` qui contient le contenu et non le fichier `.css` qui contient son style.

Pour le contenu, cela dépend de la page que vous avez téléchargée. S'il s'agit d'une page web **statique** (ex: wikipedia), le contenu sera quasi identique après l'avoir téléchargé localement. En revanche, si le site est **dynamique** (ex: youtube), le contenu risque d'être très différent car le serveur n'est plus là pour personnaliser le contenu de la page en temps réel pour vous.

Concernant l'url, vous pouvez voir qu'il ne pointe plus vers le serveur du site, mais bien vers le fichier `.html` local de votre ordinateur.
```
````
-->

## Premier contact avec un code HTML

Voici à quoi ressemble un fichier HTML très simple :

```{image} ../media/tout_premier_exemple_html.png
```

<!--
````{admonition} Micro-activité
:class: note
Ouvrez le fichier .html de l'activité précédente avec un éditeur de texte (Visual Studio Code).  
Il est probable que le fichier ne contienne pas que du code HTML mais également du code Javascript et CSS (nous verrons cela plus tard).  
Pour trouver le code HTML, cherchez les symboles `<` et `>`. HTML est un langage basé sur des balises représentées par des chevrons `<>`.  

Voyez-vous des similitudes avec le langage python ?

```{dropdown} Réponse
Vous ne devriez retrouver que très peu de similitudes avec python car HTML n'est pas un langage de programmation. La seule similitude pourrait être les indentations (décalage à droite) qui sont présentes dans presque tous les langages informatiques.
```
````
-->

L'HTML tout seul décrit seulement le contenu de la page, mais pas la forme. Le CSS est un autre langage du Web qui vient compléter le HTML pour rendre les pages plus jolies.  
Une page HTML sans CSS ne contiendra par exemple aucune couleur (à l'exception des images).

```{image} ../media/html_sans_css.png
```

<!--
```{admonition} Exercice 1
:class: note
Vous allez écrire votre tout premier (simplissime) fichier HTML.  
Créez un nouveau fichier et changez l'extension du fichier en `.html` (vous devriez pouvoir le faire directement depuis Visual Studio Code).  
Ouvrez votre fichier, écrivez quelques mots, sauvegardez, puis ouvrez votre fichier avec un navigateur en double-cliquant dessus.  
Vous devriez voir votre texte s'afficher !
```

````{admonition} Exercice 2
:class: note
Modifiez le texte de votre fichier `.html`pour ajouter des sauts de lignes (touche `enter`) afin de faire des paragraphes séparés.  
Est-ce que cela fonctionne ? Les paragraphes sont-ils bien visibles dans le navigateur ?

```{dropdown} Réponse
Non, les paragraphes ne seront pas visibles dans le navigateur car il faut utiliser des balises bien spécifiques pour dire que l'on veut faire un paragraphe.  
C'est ce que nous allons voir dans la prochaine section.
```
````
-->

## Un langage de balises

Comme évoqué précédemment, le langage HTML utilise ce qu'on appelle des balises. On les écrit entre chevrons `<` et `>`:

```{image} ../media/balises_html.jpg
```

```{admonition} Touches pour les chevrons
:class: hint
Sur mac, vous utilisez :
- la touche `<` pour faire le chevron ouvrant
- et `⇧`  + `<` pour le chevron fermant.
```

Les balises indiquent la nature du texte qu'elles encadrent. Elles permettent au navigateur de comprendre ce qu'il faut afficher à l'écran.  
Voici quelques exemples:

- `<title> ... </title>`: Titre de la page (s'affiche dans l'onglet du navigateur, pas sur la page)
- `<h1> ... </h1>`: Titre de niveau 1 (titre principal)
- `<img src="...">`: Image
- `<p> ... </p>`: Paragraphe

<!--
```{admonition} Remarque
:class: hint
Vous l'aurez remarqué, certaines balises sont doublées et prennent un `/` dans leur syntaxe.  

On distingue 2 types de balises:
1. Les balises **en paires** (une balise ouvrante et une balise fermante)
2. Et les **balises orphelines** (une seule balise).
```

`````{admonition} Exercice 3
:class: note
Reprenez votre fichier `.html` de l'exercice précédent et utlisez les balises `<p> </p>` pour créer des paragraphes.  
Chaque portion de texte entouré de ces balises sera considéré comme un paragraphe séparé.

````{dropdown} Solution
```{code-block} html
<p>Ceci est mon premier paragraphe !</p>
<p>Et en voilà un autre...</p>
```
````
`````
-->

```{admonition} Tester facilement son code
:class: hint
Pour faire des tests rapides, vous pouvez vous rendre sur <a href="https://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro"> w3schools</a> qui permet de rapidement voir ce que donne votre code HTML.
```

## Paramètrer ses balises avec des attributs

Dans la section précédente, nous avons brièvement vu la balise `<img>` qui permet d'insérer une image dans la page. Il s'agit d'une balise orpheline.  
Mais alors... comment spécifier l'image que nous voulons ? Cela passe par un **attribut** (`src` dans ce cas).

Les attributs sont un peu les options des balises. Ils viennent les compléter pour donner des informations supplémentaires.

Un attribut est situé dans la balise ouvrante d'une balise en paire, ou directement dans une balise orpheline, comme c'est le cas ci dessous avec la balise `<img>`:

```{image} ../media/balise_img.jpg
```

L'attribut `src` correspond à la source de l'image. Dans l'exemple ci-dessus, l'image se trouve dans le même dossier que le fichier `.html` donc il suffit de donner le nom de l'image.  
Il est également possible de fournir l'URL d'une image en ligne. Pour cela, faites un clic droit sur l'image que vous souhaitez utiliser puis cliquez sur "Copier l'adresse de l'image".

<!--
`````{admonition} Exercice 4
:class: note
Reprenez votre fichier `.html` de l'exercice précédent et ajoutez une image de votre choix dans la page.  
Testez les 2 types de source différentes:
1. Image locale: téléchargez une image en ligne et placez-la dans le même dossier que votre fichier `.html`.
2. Image en ligne: copiez l'adresse de l'image en ligne.

````{dropdown} Solution
Voici un exemple de solution possible avec une source en ligne.
```{code-block} html
<p>Ceci est mon premier paragraphe !</p>
<p>Et en voilà un autre...</p>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtwMFGdWzPi18CbXe1mmp2vPoxMZPbaObUX5LqrX6Ezcai5nAlNp6cnpv4HWtWUsueuw&usqp=CAU">
<p>Hop encore un paragraphe après l'image !</p>
```
````
`````
-->

```{admonition} Pour aller plus loin
:class: hint
Evidemment, il existe une multitude d'autres attributs associés à la balise `<img>`, telle que la taille de l'image par exemple.  
Vous trouverez la liste des attributs disponibles <a href="https://www.w3schools.com/tags/tag_img.asp" target="_blank">ici</a>.
```

## Structure d'une page HTML

Je peux vous l'avouer, jusqu'ici nous avons un peu triché... En réalité, tout fichier `.html` doit contenir la structure de base suivante:

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Le titre de ma page</title>
    </head>
    <body>
    </body>
</html>
```

Voyons à quoi servent toutes ces balises.

- La première ligne `<!DOCTYPE html>` est une balise orpheline indispensable : elle indique qu'il s'agit d'une page HTML.
- La balise en paire `<html> </html>` englobe tout le contenu de la page web. A l'intérieur, il y a les balises en paire `<head> </head>` et `<body> </body>`.
- La balise en paire `<head> </head>` contient deux balises qui donnent des informations au navigateur : l’encodage et le titre de la page.
- La balise orpheline `<meta charset="utf-8">` indique l'encodage utilisé dans le fichier `.html` : cela détermine comment les caractères spéciaux s'affichent (accents, idéogrammes chinois et japonais, etc.).
- La balise en paire `<title> </title>` indique au navigateur le titre de la page web. Toute page doit avoir un titre qui décrit ce qu'elle contient, il s'affichera dans l'onglet du navigateur, et apparaîtra dans les résultats de recherche, comme sur Google. Autant vous dire que bien choisir son titre est important !
- La balise en paire `<body> </body>` contient tout ce qui sera affiché à l'écran sur la page web (c'est ici que vous passerez 99% de votre temps).

<!--
`````{admonition} Exercice 5
:class: note
Modifiez votre fichier `.html` des exercices précédents pour inclure cette structure de base.  
Pour rappel, tout le contenu de votre page doit se trouver entre les balises `<body> </body>`.

````{dropdown} Solution
```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Le titre de ma page</title>
    </head>
    <body>
        <p>Ceci est mon premier paragraphe !</p>
        <p>Et en voilà un autre...</p>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtwMFGdWzPi18CbXe1mmp2vPoxMZPbaObUX5LqrX6Ezcai5nAlNp6cnpv4HWtWUsueuw&usqp=CAU">
        <p>Hop encore un paragraphe après l'image !</p>
    </body>
</html>
```
````
`````
-->

```{admonition} Attention
:class: attention
L'ordre des balises est super **important** ! Elles doivent s'emboiter les unes dans les autres, un peu comme des poupées russes.  
```

```{image} ../media/structure_html.jpg
```

```{question} Ordre des balises
:multi: 
Parmi les emboîtements suivants, lesquels sont corrects ?
* {f}`<html><body></html></body>`
* {v}`<html><body></body></html>`
* {v}`<p><img></p>`
* {f}`<body><p></p><p></body></p>`
* {v}`<body><p></p><p></p></body>`
```

## Les commentaires

```{admonition} À retenir
:class: hint
Tout code informatique se doit d'être suffisamment commenté pour faciliter sa compréhension par un autre humain.  
Même vous, vous pouvez oublier ce que fait votre code avec le temps... Les commentaires sont là pour vous aider !
```

Un commentaire en HTML est donc un texte qui sert simplement de mémo. Il n'est pas affiché, il n'est pas lu par l'ordinateur, cela ne change rien à l'affichage de la page.  
Souvenez-vous, en python, nous ajoutons un commentaire grâce au symbole `#`.  
En HTML, la syntaxe est la suivante:

```{code-block} html
<!-- Ceci est un commentaire -->
```

```{question} Confidentialité
Si vous mettez en ligne un site web avec des commentaires dans le code, pensez-vous que les visiteurs de votre site pourront les retrouver avec un peu d'ingéniosité ?
* {v}`Oui`
* {f}`Non`
===
Oui ! Rappelez-vous, le fichier `.html` est envoyé au visiteur et il a donc tout le loisir de lire son code, y compris vos commentaires.  
Faites donc attention à ne jamais mettre d'informations sensibles tel qu'un mot de passe dans les commentaires de votre page !
```

## Résumé des balises de ce chapitre

Structure de base d'une page HTML:

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Le titre de ma page</title>
    </head>
    <body>
        <h1>Bienvenue sur mon super site !</h1>
        <p>Blablabla</p>
        etc...
    </body>
</html>
```

- *Titre de la page*: `<title> ... </title>`
- *Titre de niveau 1* (titre très important): `<h1> ... </h1>`
- *Titre de niveau 2* (titre important): `<h2> ... </h2>`
- ...
- *Titre de niveau 6* (titre vraiment pas important): `<h6> ... </h6>`
- *Paragraphe*: `<p> ... </p>`
- *Image*: `<img src="...">`
- *Commentaire*: `<!-- Ceci est un commentaire -->`

## Exercice récapitulatif 1

```{admonition} Exercice récapitulatif 1
:class: note
Ecrivez la page web principale d'un site d'agence de voyage dans un fichier nommé `destination2025.html`.  
Vous êtes libre sur le contenu mais la page doit contenir les éléments suivants:
- Le titre "Pays à visiter en 2025" qui doit apparaître dans l'onglet du navigateur.
- Présentation de 3 pays de votre choix, avec à chaque fois un titre, un paragraphe et une image.
- Un mot écrit en gras (à vous de chercher sur internet la balise qui permet de le faire).
- Un commentaire indiquant le site où vous avez trouvé la balise permettant de mettre un mot en gras.

Déposez votre fichier sur Moodle à l'endroit prévu.
```
