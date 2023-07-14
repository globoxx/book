(web.css1)=

# 5. Introduction au CSS

On ne va pas se mentir. Jusqu'ici, nos sites étaient plutôt moches.  
A partir de ce chapitre, nous allons pouvoir styliser nos pages grâce à un second langage fondateur du Web: CSS.

```{panels}

:img-top: ../media/andreessen.jpg

Mark Andreessen
^^^^^
***Né en 1971***

L'informaticien américain [**Mark Andreessen**](https://fr.wikipedia.org/wiki/Marc_Andreessen) est l'un des créateurs du premier navigateur web (Mosaic) en 1993 ainsi que le fondateur de Netscape, la 1ère entreprise entièrement tournée vers Internet. Il n'est pas à proprement parler le créateur du CSS mais ses nombreuses innovations vont pousser d'autres ingénieurs à travailler dessus, notamment [**Håkon Wium Lie**](https://fr.wikipedia.org/wiki/H%C3%A5kon_Wium_Lie) qui sera le premier à proposer l'idée même du CSS.
----
:img-top: ../media/css.png
CSS3
^^^^^
***Créé en 1996***

Le [CSS](https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade) (Cascading Style Sheets, aussi appelées feuilles de style) a pour rôle de gérer l'apparence de la page web (agencement, positionnement, décoration, couleurs, taille du texte…). Ce langage est venu compléter le HTML en 1996, et il est toujours au fondement même du style du Web de nos jours.
```

TODO CSS art

## Où écrire le CSS ?

Il est possible d'écrire du code CSS directement dans des fichiers `.html` grâce aux balises `<style> </style>`. Cependant, cela rend le code difficile à lire et ce n'est pas la méthode que nous allons utiliser ici.

Nous allons écrire tout notre code CSS dans un fichier `.css` puis le lier aux différentes pages `.html` de notre site.

````{admonition} Comment faire ?
Pour lier les fichiers `.css` et `.html`, vous allez rajouter une ligne dans le fichier `.html` pour indiquer au navigateur d'aller chercher la feuille de style associée.

Cette ligne s'ouvre avec la balise orpheline `<link>` et on la place à l'intérieur de la balise `<head> </head>`:

```{code-block} html
<head>
    <meta charset="utf-8">
    <title>Ma page</title>
    <link href="style.css" rel="stylesheet">
</head>
```
````

## Appliquer une propriété CSS à une balise HTML

Voici à quoi ressemble un bout de code CSS:

```{code-block} css
p {
    color: blue;
}
```

````{admonition} Exercice 1
:class: note
Créez un fichier `style.css` et copiez-y le code ci-dessus.

Créez un fichier `.html`, copiez-y le code ci-dessous et ajoutez le lien vers la feuille de style `style.css` comme expliqué dans la section précédente.

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Le titre de ma page</title>
    </head>
    <body>
        <h1> </h1>
        <p>Ceci est mon premier paragraphe !</p>
        <p>Hop encore un paragraphe après l'image !</p>
        <ul>
            <li> </li>
        </ul>
        <p> </p>
    </body>
</html>
```

Ouvrez le fichier `.html` dans votre navigateur.
Pouvez-vous dire ce que fait le code CSS du fichier `style.css` ?

```{dropdown} Solution
Le code CSS signifie en français: "Je veux que tous les paragraphes soient écrits en bleu".
```
````

Le CSS fonctionne avec 3 éléments différents:

1. **Le sélecteur**: ici on écrit les noms des balises HTML dont on veut modifier l'apparence. Par exemple, si je veux modifier l'apparence de tous les paragraphes  `<p>`, je dois écrire `p` (sans les chevrons).
2. **La ou les propriétés CSS**: les effets de style sont listés via des propriétés. Par exemple, `color` permet d'indiquer la couleur du texte, `font-size`  permet d'indiquer la taille du texte, etc. Il existe **BEAUCOUP** de propriétés CSS ! Mais rassurez-vous, vous n’avez pas besoin de les connaître toutes par cœur.
3. **…et leurs valeurs**: pour chaque propriété CSS, on doit indiquer une valeur. Par exemple, pour la propriété `color`, il faut indiquer le nom de la couleur. Pour font-size, il faut indiquer quelle taille on veut, etc.

```{image} ../media/structure_css.jpg
```

```{admonition} Accolades sur le clavier
Sur mac, vous utilisez:
- les touches `option ⌥` + `(` pour faire l'accolade ouvrante;
- et les touches `option ⌥` + `)` pour faire l'accolade fermante;
```

`````{admonition} Exercice 2
:class: note
Modifiez le fichier `.css` de l'exercice précédent pour changer tous les titres principaux (`h1`) en rouge.

````{dropdown} Solution
```{code-block} css
p {
    color: blue;
}

h1 {
    color: red;
}
```
````
`````

## Appliquer une propriété CSS à plusieurs balises HTML

## Les balises universelles `span` et `div`

## Exercice récapitulatif

```{admonition} Exercice 4 (récapitulatif)
:class: note
Votre site de photographie attire de nombreux clients, mais certains se plaignent de ne pas pouvoir 

Déposez votre dossier sur Moodle à l'endroit prévu.
```
