(web.css4)=

# 8. Aligner ses blocs avec Flexbox

Nous avons vu comment créer des blocs, modifier leur taille, leurs marges et comment les centrer. Mais comment gérer l'alignement de ses blocs ? Par exemple horizontalement ? C'est ce que nous allons voir ici !

Pour pouvoir gérer l'alignement de nos blocs, on va devoir les ranger dans un **conteneur** (qui est en fait un autre bloc qui englobe vos blocs). Prenons un exemple simple:

```{code-block} html
<div class="conteneur">
    <p>Paragraphe 1</p>
    <p>Paragraphe 2</p>
    <p>Paragraphe 3</p>
</div>
```

Par défaut, les 3 paragraphes vont s'afficher les uns sous les autres. Il s'agit maintenant de spécifier au `conteneur` qu'il doit aligner ses blocs horizontalement. Cela se fait comme ceci:

```{code-block} css
.conteneur {
    display: flex;
}
```

Testez ce code dans ce <a href="https://codepen.io/Vincent-Guertler/pen/jOQKwYa" target="_blank">CodePen</a>.

Ce système s'appelle **Flexbox** et permet de définir simplement la manière dont un conteneur organise ses blocs.

## Choisir la direction avec `flex-direction`

La propriété `flex-direction` permet de définir la direction des blocs avec les valeurs principales suivantes:

- `row`: alignement horizontal (par défaut dès qu'on a appliqué `display: flex`)
- `column`: alignement vertical

## Aligner ses blocs sur l'axe principal avec `justify-content`

Les blocs sont organisés par défaut de manière horizontale. Mais ils peuvent être organisés de manière verticale. Selon le choix que vous faîtes, ça va définir ce qu'on appelle l'axe principal. Il y a aussi un axe secondaire:

- si vos éléments sont organisés horizontalement, l'axe secondaire est l'axe vertical
- si vos éléments sont organisés verticalement, l'axe secondaire est l'axe horizontal

Pour changer leur alignement sur l'axe principal, on va utiliser `justify-content`, qui peut prendre ces valeurs:

- `flex-start`: alignés au début de l'axe (par défaut)
- `flex-end`: alignés à la fin de l'axe
- `center`: alignés au centre de l'axe
- `space-between`: les éléments sont étirés sur tout l'axe (il y a de l'espace entre eux)
- `space-around`: idem, les éléments sont étirés sur tout l'axe, mais ils laissent aussi de l'espace sur les extrémités

`````{admonition} Exercice 1
:class: note
Testez les différentes valeurs de `justify-content` dans le <a href="https://codepen.io/Vincent-Guertler/pen/jOQKwYa" target="_blank">CodePen précédent</a>.

Tentez également de changer la direction avec `flex-direction`.
`````

## Aligner ses blocs sur l'axe secondaire avec `align-items`

La propriété `align-items` permet de changer leur alignement sur l'axe secondaire (par défaut vertical), grâce aux valeurs:

- `stretch`: les éléments sont étirés sur tout l'axe (valeur par défaut)
- `flex-start`: alignés au début de l'axe
- `flex-end`: alignés à la fin de l'axe
- `center`: alignés au centre de l'axe

`````{admonition} Exercice 2
:class: note
Testez les différentes valeurs de `align-items` dans le <a href="https://codepen.io/Vincent-Guertler/pen/jOQKwYa" target="_blank">CodePen précédent</a>.
`````

## Exemple: créer un menu horizontal

Flexbox peut être utilisé pour créer le menu suivant:

```{image} ../media/menu_css.gif
```

Rendez-vous sur ce <a href="https://codepen.io/Vincent-Guertler/pen/jOdbXBy" target="_blank">CodePen</a> pour comprendre comment arriver à ce résultat.

## Un outil puissant

Dans ce court chapitre, je ne vous ai montré que les bases du système **Flexbox** en vous cachant intentionnellement des propriétés plus complexes.

Voici un poster récapitulatif:

```{image} ../media/css-flexbox-poster.png
```

```{admonition} Visualiser tout ça
:class: note
Voici des ressources très utiles:
- <a href="https://cssflex-generator.netlify.app/" target="_blank">CSS flex-generator</a> est un site permettant de visualiser facilement l'utilisation de FlexBox.
- <a href="https://flexboxfroggy.com/#fr" target="_blank">Flexbox Froggy</a> est un petit jeu pour vous entraîner à faire des alignements parfaits !
```

## Exercice récapitulatif

```{admonition} Exercice récapitulatif
:class: note
Pas d'exercice à rendre pour ce chapitre !

Concentrez-vous sur le développement de votre site web.
```
