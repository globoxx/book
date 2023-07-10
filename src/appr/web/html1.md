(web.html1)=

# 1. Introduction à l'HTML

Le HTML (HyperText Markup Language) a fait son apparition dès 1991 lors du lancement du Web. Son rôle est de gérer et d’organiser le contenu d'un site web.  
Il permet d'ajouter du texte, des liens, des images, des tableaux, etc.

```{image} ../media/html.png
```

```{admonition} À retenir
:class: attention
HTML est un langage de description, pas de programmation ! Il n'est pas possible de faire de logique en HTML.
```

## Le Web n'est qu'HTML (et quelques autres trucs)

Quand vous visitez un site web, le serveur du site vous transmet en réalité un fichier HTML qui sera lu et interprété par votre navigateur.  

```{admonition} Micro-activité
:class: note
Rendez-vous sur un site web de votre choix, faites un clic droit sur la page et cliquez sur "Enregistrez sous...".  
Vous observerez que votre navigateur télécharge un fichier `.html` que vous pouvez ouvrir à nouveau dans votre navigateur.  
La page est-elle identique à tout à l'heure ? A quoi ressemble l'url de la page ?
```

## Premier contact avec un code HTML

Tout comme n'importe quel autre langage informatique, HTML peut être lu et édité avec n'importe quel éditeur de texte.

```{admonition} Micro-activité
:class: note
Ouvrez le fichier .html de l'activité précédente avec un éditeur de texte.  
Il est probable que le fichier ne contienne pas que du code HTML mais également du code Javascript et CSS (nous verrons cela plus tard).  
Pour trouver le code HTML, cherchez les symboles `<` et `>`. HTML est un langage basé sur des balises représentées par des chevrons `<...>`.  

Voyez-vous des similitudes avec le langage python ?
```

L'HTML tout seul décrit simplement le contenu, mais pas la forme. Le CSS est un autre langage du Web qui vient compléter le HTML pour rendre les pages plus jolies.  
Une page HTML sans CSS ne contiendra par exemple aucune couleur (à l'exception des images).

```{admonition} Exercice 1
:class: note
Vous allez écrire votre tout premier (simplissime) fichier HTML.  
Créez un nouveau fichier texte (`.txt`) et changez l'extension du fichier en `.html` (ainsi vous pourrez l'ouvrir dans le navigateur).  
Ouvrez votre fichier avec un éditeur de texte, écrivez quelques mots, sauvegardez, puis ouvrez votre fichier avec un navigateur.  
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

## Un langage de balises

Comme évoqué précédemment, le langage HTML utilise ce qu'on appelle des balises. On les écrit entre chevrons `<`  et `>`:

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

- `<title> ... </title>`: Titre de la page (s'affiche dans l'onglet)
- `<img ...>`: Image
- `<p> ... </p>`: Paragraphe

```{admonition} Remarque
:class: hint
Vous l'aurez remarqué, certaines balises sont doublées et prennent un `/` dans leur syntaxe.  

On distingue 2 types de balises:
1. Les balises **en paires** (une balise ouvrante et une balise fermante)
2. Et les **balises orphelines** (une seule balise).
```

`````{admonition} Exercice 3
:class: note
Reprenez votre fichier `.html` de l'exercice précédent et utlisez les balises `<p> ... </p>` pour créer des paragraphes.  
Chaque portion de texte entouré de ces balises sera considéré comme un paragraphe séparé.

````{dropdown} Exemple de solution
```{code-block} html
<p>Ceci est mon premier paragraphe !</p>
<p>Et en voilà un autre...</p>
```
````
`````

## Paramètrer ses balises avec des attributs

Dans la section précédente, nous avons vu la balise `<img ...>` qui permet d'insérer une image dans la page. Il s'agit d'une balise orpheline.  
Mais alors... comment spécifier l'image que nous voulons ? Cela passe par un **attribut**.

Les attributs sont un peu les options des balises. Ils viennent les compléter pour donner des informations supplémentaires.

Un attribut est situé dans la balise ouvrante d'une balise en paire, ou directement dans une balise orpheline, comme c'est le cas ci dessous avec la balise `<img>`:

```{image} ../media/balise_img.jpg
```

L'attribut `src` correspond à la source de l'image. Dans l'exemple ci-dessus, l'image se trouve dans le même dossier que le fichier `.html` donc il suffit de donner le nom de l'image.  
Il est également possible de fournir une URL en ligne. Pour cela, faites un clic droit puis cliquez sur "Copier l'adresse de l'image".

`````{admonition} Exercice 4
:class: note
Reprenez votre fichier `.html` de l'exercice précédent et ajoutez une image de votre choix dans la page.  
Testez les 2 types de source différentes:
1. Image locale: téléchargez une image en ligne et placez là dans le même dossier que votre fichier `.html`.
2. Image en ligne: copiez l'adresse de l'image en ligne.

````{dropdown} Exemple de solution (en ligne)
```{code-block} html
<p>Ceci est mon premier paragraphe !</p>
<p>Et en voilà un autre...</p>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtwMFGdWzPi18CbXe1mmp2vPoxMZPbaObUX5LqrX6Ezcai5nAlNp6cnpv4HWtWUsueuw&usqp=CAU">
<p>Hop encore un paragraphe après l'image !</p>
```
````
`````

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
- La balise en paire `<html> ... </html>` englobe tout le contenu de la page web. A l'intérieur, il ya les balises en paire `<head> ... </head>` et `<body> ... </body>`.
- La balise en paire `<head> ... </head>` contient deux balises qui donnent des informations au navigateur : l’encodage et le titre de la page.
- La balise orpheline `<meta charset="utf-8">` indique l'encodage utilisé dans le fichier `.html` : cela détermine comment les caractères spéciaux s'affichent (accents, idéogrammes chinois et japonais, etc.).
- La balise en paire `<title> ... </title>` indique au navigateur le titre de la page web. Toute page doit avoir un titre qui décrit ce qu'elle contient, il s'affichera dans l'onglet du navigateur, et apparaîtra dans les résultats de recherche, comme sur Google. Autant vous dire que bien choisir son titre est important !
- La balise en paire `<body> ... </body>` contient tout ce qui sera affiché à l'écran sur la page web (c'est ici que vous passerez 99% de votre temps).

`````{admonition} Exercice 5
:class: note
Modifiez votre fichier `.html` des exercices précédents pour inclure cette structure de base.  
Pour rappel, tout le contenu de votre page doit se trouver entre les balises `<body> ... </body>`.

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
