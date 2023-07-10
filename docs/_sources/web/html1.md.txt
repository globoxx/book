(web.html1)=

# Introduction à l'HTML

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

Comme évoqué plus haut, le langage HTML utilise ce qu'on appelle des balises. On les écrit entre chevrons `<`  et `>`:

```{image} ../media/balises_html.jpg
```

```{admonition} Touches pour les chevrons
:class: hint
Sur mac, vous utilisez :
- la touche `<` pour faire le chevron ouvrant
- et `⇧`  + `<` pour le chevron fermant.
```

Les balises indiquent la nature du texte qu'elles encadrent. Elles permettent au navigateur de comprendre ce qu'il faut afficher à l'écran.
