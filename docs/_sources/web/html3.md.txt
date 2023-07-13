(web.html3)=

# 3. Faire des liens

Ne serait-ce pas chouette de pouvoir ajouter plusieurs pages à nos sites web ? Même si les sites "one-page" (qui ne contiennent qu'une seule longue page) sont de plus en plus courants ([exemple ici](https://mort-modern.losttype.com/)), la majorité des sites web contiennent une multitude de pages liées entre elles par des liens.

```{admonition} A retenir
:class: note
Un **lien hypertexte** (ou hyperlien) est une référence placée dans le contenu d'un document éléctronique permettant de passer automatiquement à un autre document.
```

````{admonition} Exercice 1
:class: note
Ouvrez Firefox, rendez-vous sur le site de votre choix et cherchez un lien hypertexte. Faites un clic droit sur le lien puis cliquez sur "Inspecter". Votre navigateur devrait alors ouvrir le code HTML du site et pointer directement sur le lien que vous aviez séléctionner.
Lisez ce bout de code HTML pour découvrir quelle balise permet d'insérer un lien hypertexte.

```{dropdown} Solution
Un lien hypertexte s'insert avec la balise `<a> </a>` (pour "anchor", ancre en français).

L'attribut `href` suivi de `=` indique l'URL de redirection (par exemple l'url d'un autre site web). Il faut mettre des `" "` autour de l'URL.

Finalement, on écrit entre les 2 balises le texte du lien.
```
````

`````{admonition} Exercice 2
:class: note
Modifiez le code HTML suivant pour ajouter des liens hypertextes vers les pages wikipédia des différentes destinations de la liste.

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

Si vous voulez faire un lien vers un autre site existant en ligne, rien de plus simple, il suffit de copier l'URL du site et le coller entre `" "` à la suite de l'attribut `href`, comme ceci:

```{code-block} html
<a href="https://mdlgb.ch/">Accédez à Moodle</a>
```

```{admonition} A retenir
:class: note
On appelle ça un **lien absolu** car il indique une adresse complète.
```

## Les liens relatifs (entre vos pages)

Si vous voulez faire un lien vers une autre page de votre site, il  suffit d'entrer le nom du fichier `.html` entre `" "` à la suite de l'attribut `href`, comme ceci:

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
Nous allons ajouter une 2ème page à votre site `mesvoyages.ch` créé dans le chapitre précédent. Le but est d'ajouter une page permettant aux visiteurs de contacter l'agence de voyage.

Commencez par créer un nouveau fichier `.html` nommé `contact.html` et déposez le dans le même dossier que la page principale `voyages.html`.

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
            <li>Email: <a href="mailto:mesvoyages@gmail.com">mesvoyages@gmail.com</a></li>
            <li>Telephone: 0791234567
        </ul>
    </body>
</html>
```

Ajoutez un lien relatif depuis la page principale `voyages.html` vers la page `contact.html`. Ajoutez également un lien dans l'autre sens.

````{dropdown} Solution
```{code-block} html
<!-- Quelque part sur la page principale -->
<a href="concact.html">Contact</a>

<!-- Quelque part sur la page concact -->
<a href="voyages.html">Accueil</a>
```
````
`````

```{question} Absolu ou relatif ?
Parmi les liens suivants, les quels sont relatifs ?
* {v}`<a href=`chats.html`>Chats</a>`
* {f}`<a href="https://www.google.com">Google</a>`
* {v}`<a href="mon_site/contenu/pages/page3.html">Page 3</a>`
* {f}`<a href="https://www.codeur.com/page2/">Page 2</a>`
```

````{question} Chemin relatif
Vous avez des fichiers organisés de la manière suivante:

```{image} ../media/organisation_dossiers.png
```

Vous êtes dans le fichier `index.html`, quel code permet de faire un lien vers la `page1.html` ?

* {v}`<a href="page1.html">Page 1</a>`
* {f}`<a href="dossier1/page1.html">Page 1</a>`
* {v}`<a href="../dossier1/page1.html">Page 1</a>`
* {f}`<a href="dossier2/page1.html">Page 1</a>`

Vous êtes dans le fichier `page1.html`, quel code permet de faire un lien vers la `page2.html` ?

* {v}`<a href="page2.html">Page 2</a>`
* {f}`<a href="dossier2/page2.html">Page 2</a>`
* {v}`<a href="../dossier2/page2.html">Page 2</a>`
* {f}`<a href="../page2.html">Page 2</a>`
````

```{admonition} Info
:class: hint
La convention veut que la page d'accueil d'un site porte le nom `index.html`. Il s'agit de la première page que voit un visiteur et celle qui est en général référencée par les moteurs de recherche.   
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
<a href="https://mdlgb.ch/"><img src="https://pbs.twimg.com/profile_images/1125713968637579265/L4HJ0qyd_400x400.png"></a>
```

## Exercice récapitulatif

```{admonition} Exercice 4 (récapitulatif)
:class: note
Vous vous lancez dans la photographie. Vous avez besoin d'un site où les potentiels clients pourraient vous contacter pour vos services.  

Créez un nouveau dossier de travail nommé `photographie`.  
Ecrivez la page d'accueil du site dans un fichier nommé `index.html`.  
Vous êtes libre sur le contenu mais la page doit contenir les éléments suivants:
- Un titre qui doit apparaître dans l'onglet du navigateur.
- Un titre principal avec votre nom.
- Un petit paragraphe auto-biographique.
- Un lien vers une page `book.html`.
- Un lien vers une page `contact.html`.

La page `book.html` contient quelques-unes de vos meilleures photographies (trouvées sur Internet) et un lien pour retourner à l'accueil.

La page `contact.html` contient votre adresse mail (fausse) et un lien pour retourner à l'accueil.

Déposez votre dossier sur Moodle à l'endroit prévu.
```
