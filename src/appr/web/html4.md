(web.html4)=

# 4. Plus sur les images

```{admonition} Rappel
:class: note
Une image s'insert avec la balise orpheline `<img src="image.jpg" alt="Une image">`.  
Notez l'attribut `alt` (pour "alternative") qui permet de donner une description de l'image qui sera affichée dans le cas où l'image n'apparaît pas correctement dans le navigateur. Cet attribut est obligatoire pour que les robots des moteurs de recherche considère votre code comme conforme et fassent un bon référencement de votre site.
```

Voici un exemple qui spécifie l'attribut `alt`:

```{code-block} html
<p>
    Voici une très belle photo de mes dernières vacances.<br>
    <img src="images/plage.jpg" alt="Photo de plage vue du dessus" />
</p>
```

```{admonition} Et les non-voyants sur le web ?
:class: note
Quand ils surfent sur le web, les personnes non-voyantes utilisent des logiciels qui leur lisent le contenu des pages. Dans cette situation, vous réalisez l'importance de donner une courte description de vos images avec l'attribut `alt`, afin que le synthétiseur vocal puisse décrire l'image à la personne.
```

## Rassembler ses images

Il est fortement conseillé de rassembler les images de votre site dans un dossier `images` afin d'éviter de les mélanger avec les fichiers `.html`.

`````{admonition} Exercice 1
:class: note
Si ce n'est pas déjà fait, reprenez le dossier `photographie` de l'exercice récapitulatif du chapitre précédent et créez un dossier `images` pour y placer toutes vos images. Bien entendu, il vous faut ensuite modifier les sources des images dans le code.  
Ajoutez également l'attribut `alt` pour chaque image.

````{dropdown} Solution
Vos liens doivent maintenant ressembler à ça:
```{code-block} html
<img href="images/photo1.jpg" alt="Image montrant un gratte-ciel">
```
````
`````

```{admonition} Attention
:class: attention
Évitez à tout prix les accents, majuscules et espaces dans vos noms de fichiers et de dossiers. Par exemple, voici un chemin qui va poser problème: `Images du site/Image toute bête.jpg`.

Il est courant de remplacer les espaces par des tirets bas (_underscore_) `_`. Idéalement, le chemin devrait donc plutôt ressembler à `images_du_site/image_toute_bete.jpg`.
```

## Changer la taille des images

## Ajouter une infobulle

## Exercice récapitulatif

```{admonition} Exercice 4 (récapitulatif)
:class: note
Votre site de photographie attire de nombreux clients, mais certains se plaignent de ne pas pouvoir 

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
