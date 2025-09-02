(web.html2)=

# 2. Structurer son texte

```{admonition} Rappel
:class: hint
Le texte affiché sur votre page web est toujours compris entre les balises `<body> </body>`.
```

Dans ce chapitre, nous allons voir des balises supplémentaires afin de pouvoir afficher des titres, des listes, du texte plus important, etc.

## Les paragraphes et sauts de ligne

```{admonition} Rappel
:class: hint
Les balises `<p> </p>` permettent de délimiter des paragraphes.
```

N'est-il pas possible d'ajouter un saut de ligne sans forcément faire un nouveau paragraphe ?  
Si ! La balise orpheline `<br>` (pour _break_) permet d'insérer un saut de ligne.

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <p>Voici mon premier paragraphe (qui traite de manière très très détaillée l'histoire du chant folklorique russe à travers la 2ème moitié du XIVème siècle pour le plus grand plaisir de tous mes lecteurs avides de connaissances pour briller en société), <br>dont le contenu est particulièrement long.</p>
        <p>Et voilà mon second paragraphe...</p>
    </body>
</html>
```

```{question} Espace entre les textes
Vous voulez faire un grand espace entre 2 textes, est-ce une bonne idée selon vous d'empiler les `<br>` pour faire plein de sauts de ligne ?
* {f}`Oui, pourquoi pas ?`
* {f}`Non, ça ne fonctionne pas`
* {v}`Non, ça fonctionne mais ce n'est pas la bonne manière`
===
Même si cela fonctionne, c'est une mauvaise pratique qui rend le code compliqué à maintenir. Pour décaler du texte correctement, nous utiliserons un langage de mise en forme: le CSS.
```

## Les titres

Les balises de titre vont de `<h1> </h1>` (pour le titre principal) jusqu'à `<h6> </h6>` (pour le plus petit titre).  

```{admonition} Attention
:class: attention
Ne confondez pas la balise `<h1> </h1>` avec la balise `<title>` qui elle n'affiche rien sur la page mais qui affiche le titre de la page dans l'onglet du navigateur.
```

`````{admonition} Exercice 1
:class: note
Créez un nouveau fichier `.html` avec la structure de texte ci-dessous. Ajoutez les balises de titres (`<h1>`, `<h2>`, etc) et les balises de paragraphes (`<p>`) aux endroits appropriés:

- Histoire de la Suisse
- 1. Introduction
- Petit paragraphe introductif
- Second petit paragraphe introductif
- 2. Préhistoire
- 2.1 Age du bronze
- Petit blabla
- 2.2 Age du fer
- 2.2.1 L'occupation celte
- Encore du blabla
- ...
- 3. Conclusion
- Paragraphe de conclusion

````{dropdown} Solution
```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <h1>Histoire de la Suisse</h1>
        <h2>1. Introduction</h2>
        <p>Petit paragraphe introductif</p>
        <p>Second petit paragraphe introductif</p>
        <h2>2. Préhistoire</h2>
        <h3>2.1 Age du bronze</h3>
        <p>Petit blabla</p>
        <h3>2.2 Age du fer</h3>
        <h4>2.2.1 L'occupation celte</h4>
        <p>Encore du blabla</p>
        <p>...</p>
        <h2>3. Conclusion</h2>
        <p>Paragraphe de conclusion</p>
    </body>
</html>
```
````
`````

```{admonition} Note
:class: note
Vous noterez que les tailles de chaque titre sont prédéfinies par le navigateur. Nous pourrons les modifier à notre guise lors que nous verrons le langage CSS.
```

## Les listes

Voici un exemple de code permettant d'afficher 2 listes.

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <h1>Ma liste de courses</h1>
        <ul>
            <li>Pain</li>
            <li>Céréales</li>
            <li>Café</li>
            <li>Oranges</li>
        </ul>

        <h1>Ma recette de pates</h1>
        <ol>
            <li>Je fais chauffer de l'eau.</li>
            <li>Je mets les pates dans l'eau.</li>
            <li>J'attends.</li>
            <li>Je mets du sel parce que j'ai oublié avant.</li>
            <li>Je lance une pate contre le mur pour voir si elle est cuite.</li>
            <li>Je sors les pates.</li>
            <li>Je mets du beurre.</li>
            <li>Bon appétit !</li>
        </ol>
    </body>
</html>
```

````{admonition} Exercice 2
:class: note
Testez l'exemple précédent et devinez à quoi servent les balises suivantes:

- `<ul> </ul>`
- `<ol> </ol>`
- `<li> </li>`

```{dropdown} Solution
- La balise `<ul> </ul>` (pour "unordered list") sert à définir une liste non-ordonnée (ou liste à puces).
- La balise `<ol> </ol>` (pour "ordered list") sert à définir une liste ordonnée (ou liste numérotée).
- La balise `<li> </li>` (pour "list item") sert à définir un élément d'une liste.
```
````

## Mettre en valeur du texte

Dans le texte qui s'affiche sur une page web, vous aimeriez faire ressortir certains mots en particulier.

La balise la plus utilisée pour cela est `<strong>` mais HTML vous propose différents moyens de mettre en valeur le texte de votre page:

- `<strong> </strong>`: mets le texte en **gras**.
- `<em> </em>`: mets le texte en _italique_.
- `<u> </u>`: mets le texte en __souligné__.
- `<mark> </mark>`: mets le texte en surligné.

`````{admonition} Exercice 3
:class: note
Reprenez le fichier `.html` contenant les listes et mettez le café de la liste de course en valeur.

````{dropdown} Solution
```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <h1>Ma liste de courses</h1>
        <ul>
            <li>Pain</li>
            <li>Céréales</li>
            <li><strong>Café</strong></li>
            <li>Oranges</li>
        </ul>

        <h1>Ma recette de pates</h1>
        <ol>
            <li>Je fais chauffer de l'eau.</li>
            <li>Je mets les pates dans l'eau.</li>
            <li>J'attends.</li>
            <li>Je mets du sel parce que j'ai oublié avant.</li>
            <li>Je lance une pate contre le mur pour voir si elle est cuite.</li>
            <li>Je sors les pates.</li>
            <li>Je mets du beurre.</li>
            <li>Bon appétit !</li>
        </ol>
    </body>
</html>
```
````
`````

## Insérer une autre page dans sa page ?

Vous vous demandez comment insérer une vidéo YouTube ou une carte Google Maps sur votre site ? La balise `<iframe> </iframe>` peut vous permettre de le faire !

```{youtube} uHKfrz65KSU
```

Les iframe permettent d'insérer une page web dans une autre page. Elles étaient très utilisées au début de l'HTML mais ont aujourd'hui un rôle plus secondaire et ne servent très souvent qu'à insérer des éléments provenant de sites tiers comme des modules de partage sociaux ou des cartes google maps.

Le plus simple est encore d'obtenir le **code d'intégration** de la vidéo ou de la carte que vous voulez afficher. Il s'agit d'un code HTML contenant une iframe prête à l'emploi.

```{admonition} Comment faire
:class: note
Pour YouTube, il suffit de faire un clic droit sur la vidéo et de choisir "Copier le code d'intégration". Vous n'avez alors plus qu'à coller le code dans votre page web.

Pour Google Maps, ouvrez le menu en haut à gauche de la page et cliquez sur "Partager ou intégrer la carte". Choisissez ensuite "Intégrer une carte", choisissez la taille de l'iframe et copiez le code. Appelez votre enseignant en cas de problème pour le trouver.
```

`````{admonition} Exercice 4
:class: note
Reprenez votre page sur les meilleures destinations à visiter (`destination2025.html`) et ajoutez 2 iframe. Une comportant une vidéo sur une destination et une seconde affichant une carte (Google Maps).

````{dropdown} Solution
```{code-block} html
<iframe width="1257" height="707" src="lien vers votre vidéo" title="titre de la vidéo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe src="source google map" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
```
````
`````

## Résumé des balises de ce chapitre

- *Liste non ordonnée (unordered list)*: `<ul> ... </ul>`
- *Liste ordonnée (ordered list)*: `<ol> ... </ol>`
- *Élément de liste (list item)*: `<li> ... </li>`

Exemple de liste non ordonnée:

```{code-block} html
<ul>
    <li>Pain</li>
    <li>Céréales</li>
    <li>Oranges</li>
</ul>
```

- *Mise en forme du texte*: `<strong> ... </strong>` (gras), `<em> ... </em>` (italique), `<u> ... </u>` (souligné), `<mark> ... </mark>` (surligné)
- *Iframe*: `<iframe> ... </iframe>`

## Exercice récapitulatif 2

```{admonition} Exercice récapitulatif 2
:class: note
Vous êtes le nouveau propriétaire d'un restaurant et souhaitez créer une simple page listant les plats que vous proposez.

Écrivez la page web principale de votre site dans un fichier nommé `restaurant.html`.
Vous êtes libre sur le contenu, mais la page doit contenir les éléments suivants :

- Un titre principal annonçant le nom de votre restaurant.
- Un petit paragraphe expliquant quel type de cuisine est proposé dans votre restaurant.
- Un sous-titre “Plats proposés” (balise `<h2>`).
- Une liste non ordonnée de plats (au moins 3) avec images à l’appui (chaque élément de la liste contient le nom du plat ainsi qu’une image).
- Au moins un mot important (gras, italique, souligné ou surligné) sur votre page.
- Un iframe Google Maps pointant vers l'emplacement de votre restaurant.

Déposez votre fichier sur Moodle à l'endroit prévu.
```
