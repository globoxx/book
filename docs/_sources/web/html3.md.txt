(web.html3)=

# 3. Faire des liens

Ne serait-ce pas chouette de pouvoir ajouter **plusieurs pages** à nos sites web ? Même si les sites "one-page" (qui ne contiennent qu'une seule longue page) sont de plus en plus courants ([exemple ici](https://mort-modern.losttype.com/)), la majorité des sites web contiennent une multitude de pages liées entre elles par des liens.

```{admonition} A retenir
:class: note
Un **lien hypertexte** (ou hyperlien) est une référence placée dans le contenu d'un document éléctronique permettant de passer automatiquement à un autre document.
```

````{admonition} Exercice 1
:class: note
Ouvrez Firefox, rendez-vous sur le site de votre choix et cherchez un lien hypertexte. Faites un clic droit sur le lien, puis cliquez sur "Inspecter". Votre navigateur devrait alors ouvrir le code HTML de la page et pointer directement sur le code du lien.
Lisez ce bout de code HTML pour découvrir quelle balise permet d'insérer un lien hypertexte.

```{dropdown} Solution
Un lien hypertexte s'insert avec la balise `<a> </a>` (pour "anchor", ancre en français).

L'attribut `href` suivi de `=` indique l'URL de redirection (par exemple l'url d'un autre site web). Il faut mettre des `" "` autour de l'URL.

Finalement, on écrit entre les 2 balises le texte du lien.  
Exemple: `<a href="https://mdlgb.ch/">Accédez à Moodle</a>`
```
````

`````{admonition} Exercice 2
:class: note
Modifiez le code HTML suivant pour ajouter des liens hypertextes vers les pages wikipédia des différentes destinations de la liste.  
Vous pouvez le faire directement sur <a href="https://www.w3schools.com/html/tryit.asp?filename=tryhtml_intro" target="_blank">w3schools</a>.

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <h1>Destinations</h1>
        <ul>
            <li>Hawaï</li>
            <li>Chypre</li>
            <li>Mongolie</li>
        </ul>
    </body>
</html>
```

````{dropdown} Solution
```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Ma page</title>
    </head>
    <body>
        <h1>Destinations</h1>
        <ul>
            <li><a href="https://fr.wikipedia.org/wiki/Hawa%C3%AF">Hawaï</a></li>
            <li><a href="https://fr.wikipedia.org/wiki/Chypre_(pays)">Chypre</a></li>
            <li><a href="https://fr.wikipedia.org/wiki/Mongolie">Mongolie</a></li>
        </ul>
    </body>
</html>
```
````
`````

## Les liens absolus (vers d'autres sites)

Si vous voulez faire un lien vers un autre site existant en ligne, rien de plus simple, il suffit de copier l'URL du site et le coller entre `""` à la suite de l'attribut `href`, comme ceci:

```{code-block} html
<a href="https://mdlgb.ch/">Accédez à Moodle</a>
```

```{admonition} A retenir
:class: note
On appelle ça un **lien absolu** car il indique une adresse complète.
```

## Les liens relatifs (entre vos pages)

En général, un site web contient un fichier `.html` par page.  
Si vous voulez faire un lien vers une autre page **de votre site**, il suffit d'entrer le nom du fichier `.html` entre `""` à la suite de l'attribut `href`, comme ceci:

```{code-block} html
<a href="page2.html">Page 2</a>
```

```{admonition} A retenir
:class: note
On appelle ça un **lien relatif** car il indique où trouver un fichier HTML par rapport à l'emplacement de la page courante.
```

Attention, si votre 2ème page se trouve dans un dossier (par exemple un dossier nommé `contenu`), il vous faudra préciser le chemin pour accéder à cette 2ème page:

```{code-block} html
<a href="contenu/page2.html">Page 2</a>
```

`````{admonition} Exercice 3
:class: note
Nous allons ajouter une 2ème page à votre site de restaurant créé dans le chapitre précédent. Le but est d'ajouter une page permettant aux visiteurs de contacter le restaurant.

Commencez par créer un nouveau fichier `.html` nommé `contact.html` et déposez le dans **le même dossier** que la page principale `restaurant.html`.

Copiez le code suivant dans le fichier `contact.html`:

```{code-block} html
<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Contact</title>
    </head>
    <body>
        <h1>Contact</h1>
        <p>Pour tout renseigment, vous pouvez prendre contact avec notre 
        agence par les moyens suivants:</p>
        <ul>
            <!-- Il est aussi possible de créer un lien vers une adresse mail avec "mailto" -->
            <li>Email: <a href="mailto:restaurant@gmail.com">restaurant@gmail.com</a></li>
            <li>Telephone: 0791234567</li>
        </ul>
    </body>
</html>
```

Ajoutez un lien relatif depuis la page principale `restaurant.html` vers la page `contact.html`. Ajoutez également un lien dans l'autre sens.

````{dropdown} Solution
```{code-block} html
<!-- Quelque part sur la page principale -->
<a href="contact.html">Contact</a>

<!-- Quelque part sur la page contact -->
<a href="restaurant.html">Accueil</a>
```
````
`````

```{question} Absolu ou relatif ?
Parmi les liens suivants, les quels sont relatifs ?
* {v}`<a href='chats.html'>Chats</a>`
* {f}`<a href='https://www.google.com'>Google</a>`
* {v}`<a href='mon_site/contenu/pages/page3.html'>Page 3</a>`
* {f}`<a href='https://www.codeur.com/page2/'>Page 2</a>`
```

```{admonition} Remonter dans les dossiers parents
:class: note
Dans un chemin **relatif**, utiliser `..` permet de pointer vers le dossier parent (c'est à dire que cela permet de **remonter** dans la hiérarchie des fichiers).
```

````{question} Chemin relatif
Vous avez des fichiers organisés de la manière suivante:

```{image} ../media/organisation_dossiers.png
```

Vous êtes dans la page `index.html`, quel code permet de faire un lien vers `page1.html` ?

* {f}`<a href='page1.html'>Page 1</a>`
* {v}`<a href='dossier1/page1.html'>Page 1</a>`
* {f}`<a href='../dossier1/page1.html'>Page 1</a>`
* {f}`<a href='dossier2/page1.html'>Page 1</a>`

Vous êtes dans la page `page1.html`, quel code permet de faire un lien vers `page2.html` ?

* {f}`<a href='page2.html'>Page 2</a>`
* {f}`<a href='dossier2/page2.html'>Page 2</a>`
* {v}`<a href='../dossier2/page2.html'>Page 2</a>`
* {f}`<a href='../page2.html'>Page 2</a>`
````

```{admonition} Info
:class: hint
La convention veut que la page d'accueil d'un site porte le nom `index.html`. Il s'agit de la première page que voit un visiteur qui entre sur votre site et celle qui est en général référencée par les moteurs de recherche.   
Ce n'est pas strictement obligatoire, mais recommandé.
```

## Ouvrir le lien dans un nouvel onglet

Il peut être utile de configurer un lien pour que le navigateur du visiteur ouvre un nouvel onglet quand il clique dessus.

L'attribut `target="_blank"` permet justement de le faire:

```{code-block} html
<a href="https://mdlgb.ch/" target="_blank">Accédez à Moodle</a>
```

## Une image cliquable

Il est tout à fait possible de transformer une image en lien. Pour ceci, il suffit de mettre une image entre les balises `<a> </a>` au lieu d'un texte.
Voici un exemple:

```{code-block} html
<a href="https://mdlgb.ch/"><img src="logo.png"></a>
```

## Résumé des balises de ce chapitre

- *Lien absolu*: `<a href="https://www.example.com"> ... </a>`
- *Lien relatif*: `<a href="page.html"> ... </a>`
- *Lien s'ouvrant dans un nouvel onglet*: `<a href="https://www.example.com" target="_blank"> ... </a>`
- *Image cliquable*: `<a href="https://www.example.com"><img src="image.jpg"></a>`

## Exercice récapitulatif 3

```{admonition} Exercice récapitulatif 3
:class: note
Vous êtes un·e artiste qui souhaite se faire connaître. Vous avez besoin d'un site où les amateurs d'art pourraient vous contacter pour acheter vos œuvres ou pour des commandes spéciales.
Vous décidez alors de lancer votre propre site.

Créez un nouveau **dossier** nommé `ArtGallerie`.
Écrivez la page d'accueil de votre site dans un fichier nommé `index.html`.
Vous êtes libre sur le contenu mais les différentes pages doivent contenir les éléments suivants :

La page principale `index.html` contient :
- Le titre "ArtGallerie" qui doit apparaître dans l'onglet du navigateur.
- Un titre principal avec votre nom.
- Un petit paragraphe auto-biographique (vous pouvez inventer votre biographie).
- Un lien vers une page `galerie.html`.
- Un lien vers une page `contact.html`.

La page `galerie.html` contient :
- Un titre principal "Galerie".
- Quelques-unes de vos meilleures œuvres (trouvées sur Internet) (au moins 3 œuvres).
- Un lien pour retourner à l'accueil (`index.html`).

La page `contact.html` contient :
- Un titre principal "Contact".
- Une liste à puce avec votre adresse mail (fausse), un numéro de téléphone (faux) et un bouton "Contactez-moi" (à vous de chercher comment ajouter un bouton en html).
- Un lien pour retourner à l'accueil (`index.html`).

Compressez votre dossier `ArtGallerie` en fichier `ArtGallerie.zip` (clic droit sur le dossier -> compresser).  
Déposez le fichier compressé sur Moodle à l'endroit prévu.
```
