(web.html3)=

# 3. Faire des liens

Ne serait-ce pas chouette de pouvoir ajouter plusieurs pages à nos sites web ? Même si les sites monopages (qui ne contiennent qu'une seule longue page) sont de plus en plus courants ([exemple ici](https://mort-modern.losttype.com/)), la majorité des sites web contiennent une multitude de pages liées entre elles par des liens.

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

````{admonition} Exercice 2
:class: note
Modifiez le code HTML suivant pour ajouter des liens hypertextes vers les pages wikipédia des différentes destinations de la liste.

```{code-block} html

```

```{dropdown} Solution

```
````

## Les liens absolus (vers d'autres sites)

Si vous voulez faire un lien vers un autre site existant en ligne, rien de plus simple, il suffit d'utiliser copier l'URL du site entre `" "` à la suite de l'attribut `href`, comme ceci :

```{code-block} html
<a href="https://mdlgb.ch/">Accédez à Moodle</a>
```

```{admonition} A retenir
:class: note
On appelle ça un **lien absolu** car il indique une adresse complète.
```

## Les liens relatifs (entre vos pages)

```{admonition} A retenir
:class: note
On appelle ça un **lien relatif** car il indique où trouver un fichier HTML par rapport à l'emplacement de la page courante.
```
