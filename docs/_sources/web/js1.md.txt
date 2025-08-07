(web.js1)=

# 9. Introduction à JavaScript

```{panels}

:img-top: ../media/eich.jpg

Brendan Eich 🇺🇸
^^^^^
***Né en 1961***

L'informaticien américain [**Brendan Eich**](https://fr.wikipedia.org/wiki/Brendan_Eich) est le créateur de JavaScript. Il a développé les bases du langage en seulement 10 jours en 1995 chez Netscape.

----
:img-top: ../media/js.png
JavaScript
^^^^^^^^^^
***Créé en 1995***

JavaScript est un langage de programmation qui permet d'ajouter de l'interactivité et de la logique à une page web. Il fait son apparition en 1995, développé par Brendan Eich chez Netscape. Il est aujourd'hui un des langages les plus utilisés au monde.
```

## Où écrire le code JavaScript ?

Il existe principalement deux manières d'intégrer du code JavaScript dans une page web:

- **Dans un fichier externe**: le code JavaScript est écrit dans un fichier séparé avec l'extension `.js`, et ce fichier est lié à la page web via une balise `<script src="..."></script>`. C'est similaire à ce que nous avons fait avec les fichiers CSS.
- **Dans la balise `<script>`**: le code JavaScript est écrit directement dans la balise `<script>` de la page HTML.

Pour simplifier dans ce cours, nous allons utiliser la deuxième méthode, mais sachez que la première est souvent préférée pour des projets plus importants.

## Quand on clique sur un bouton

### Un bouton qui affiche une alerte

```html
<button id="alertButton">Cliquez-moi</button>

<script>
    document.getElementById("alertButton").addEventListener("click", function() {
        alert("Hey tu m'as cliqué dessus !");
    });
</script>
```

Décortiquons un peu ce code:

- La balise `<button>` crée un bouton cliquable avec l'ID `alertButton`. C'est important de lui donner un ID pour pouvoir le retrouver dans le code JavaScript.
- La balise `<script>` contient le code JavaScript.
- `document.getElementById("alertButton")` permet de récupérer le bouton en utilisant son ID.
- `.addEventListener("click", function() { ... })` ajoute un écouteur d'événement qui déclenche une fonction quand le bouton est cliqué. Ici l'événement est un clic de souris (`click`) et la fonction affiche simplement une alerte avec `alert()`.

### Un bouton qui change le texte d'un paragraphe

```html
<p id="text">Texte original</p>
<button id="changeTextButton">Changer le texte</button>

<script>
    document.getElementById("changeTextButton").addEventListener("click", function() {
        document.getElementById("text").innerText = "Texte modifié";
    });
</script>
```

Ici, nous avons un paragraphe avec l'ID `text` et un bouton pour changer son contenu. Le code JavaScript récupère le bouton et ajoute un écouteur d'événement pour changer le texte du paragraphe quand le bouton est cliqué. La propriété `innerText` permet de modifier le texte affiché dans l'élément.

### Un bouton qui change la couleur de fond

```html
<button id="changeColorButton">Changer la couleur de fond</button>
<script>
    document.getElementById("changeColorButton").addEventListener("click", function() {
        document.body.style.backgroundColor = "lightblue";
    });
</script>
```

Ici, le bouton change la couleur de fond de la page en utilisant `document.body.style.backgroundColor`. On peut mettre n'importe quelle couleur CSS valide. Si vous voulez changer la couleur de fond d'un élément spécifique, il suffit de remplacer `document.body` par l'élément ciblé (par exemple, `document.getElementById("monElement")`). Vous pouvez bien sûr modifier n'importe quelle propriété CSS de cette manière, pas seulement la couleur de fond.

## D'autres évènements

Le clic est l'événement le plus courant, mais il en existe beaucoup d'autres. Voici quelques exemples:

- `mouseover`: quand la souris passe au-dessus d'un élément
- `mouseout`: quand la souris quitte un élément
- `keydown`: quand une touche du clavier est pressée
- `submit`: quand un formulaire est soumis
- `input`: quand la valeur d'un champ de formulaire change

Vous pouvez utiliser ces événements de la même manière que pour le clic, en remplaçant `"click"` par l'événement souhaité dans `addEventListener`. Une liste complète des événements disponibles est disponible <a href="https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Events#listing_des_%C3%A9v%C3%A9nements" target="_blank">ici</a>.

## Quand on traîte un formulaire

### Un formulaire qui affiche une alerte

```html
<form id="myForm">
    <input type="text" id="name" placeholder="Entrez votre nom">
    <button type="submit">Envoyer</button>
</form>

<script>
    document.getElementById("myForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Empêche l'envoi du formulaire
        let name = document.getElementById("name").value;
        alert("Bonjour " + name);
    });
</script>
```

Décortiquons ce code:

- La balise `<form>` crée un formulaire avec un champ de texte (`<input type="text">`) pour entrer un nom et un bouton pour soumettre le formulaire.
- L'événement `submit` est déclenché quand le formulaire est envoyé. On utilise `event.preventDefault()` pour empêcher le comportement par défaut du formulaire (qui est de recharger la page).
- On récupère la valeur du champ de texte avec `document.getElementById("name").value` et on la stocke dans une variable `name`. Le mot-clé `let` permet de déclarer une variable.
- Enfin, on affiche une alerte avec le nom entré.

### Un formulaire qui permet de choisir une couleur

```html
<form id="colorForm">
    <input type="color" id="color" value="#ff0000">
    <button type="submit">Choisir la couleur</button>
</form>

<script>
    document.getElementById("colorForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Empêche l'envoi du formulaire
        let color = document.getElementById("color").value;
        document.body.style.backgroundColor = color;
    });
</script>
```

Décortiquons ce code (très similaire au précédent):

- La balise `<form>` crée un formulaire avec un champ de sélection de couleur (`<input type="color">`) et un bouton pour soumettre le formulaire.
- L'événement `submit` est déclenché quand le formulaire est envoyé. On utilise `event.preventDefault()` pour empêcher le comportement par défaut du formulaire (qui est de recharger la page).
- On récupère la valeur du champ de couleur avec `document.getElementById("color").value` et on la stocke dans une variable `color`. Le mot-clé `let` permet de déclarer une variable.
- Enfin, on change la couleur de fond de la page avec `document.body.style.backgroundColor = color`.

### Un formulaire qui additionne deux nombres et affiche le résultat sur la page

```html
<form id="additionForm">
    <input type="number" id="number1" placeholder="Nombre 1">
    <input type="number" id="number2" placeholder="Nombre 2">
    <button type="submit">Additionner</button>
</form>

Resultat: <span id="result"></span>
<script>
    document.getElementById("additionForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Empêche l'envoi du formulaire
        let number1 = parseFloat(document.getElementById("number1").value); // parseFloat convertit le texte en nombre à virgule
        let number2 = parseFloat(document.getElementById("number2").value);
        document.getElementById("result").textContent = "La somme est: " + (number1 + number2);
    });
</script>
```

Ce code utilise 2 champs de saisie pour entrer deux nombres, et un bouton pour soumettre le formulaire. Quand le formulaire est soumis, il additionne les deux nombres et affiche le résultat dans un élément `<span>`.

## Quelques concepts clés de Javascript

### Variables

En Javascript, on déclare des variables en utilisant 2 mots-clés principaux: `let` et `const`.

- `let` permet de déclarer une variable dont la valeur peut changer. Par exemple: `let age = 25;`
- `const` permet de déclarer une variable dont la valeur ne changera pas. Par exemple: `const PI = 3.14;`

### Conditions

Les conditions permettent d'exécuter du code seulement si une certaine condition est vraie. En Javascript, on utilise `if`, `else if` et `else` pour créer des conditions.

```javascript
if (condition) {
    // code à exécuter si la condition est vraie
} else if (autreCondition) {
    // code à exécuter si l'autre condition est vraie
} else {
    // code à exécuter si aucune des conditions précédentes n'est vraie
}
```

### Boucles

Les boucles permettent de répéter du code plusieurs fois. En Javascript, on utilise principalement `for` et `while` pour créer des boucles.

```javascript
// Boucle for de 0 à 4 (5 itérations)
for (let i = 0; i < 5; i++) {
    alert("Itération " + i);
}

// Boucle while qui s'arrête quand i atteint 5 en partant de 0 (5 itérations)
let i = 0;
while (i < 5) {
    alert("Itération " + i);
    i++;
}
```

### Fonctions

Les fonctions permettent de regrouper du code réutilisable. En Javascript, on peut déclarer une fonction avec le mot-clé `function`.

```javascript
function direBonjour(nom) {
    alert("Bonjour " + nom + "!");
}

function addition(a, b) {
    return a + b; // Retourne la somme de a et b
}
```

## Pour aller plus loin

Si vous voulez approfondir vos connaissances en JavaScript, voici quelques ressources utiles:

- <a href="https://developer.mozilla.org/fr/docs/Web/JavaScript" target="_blank">MDN Web Docs - JavaScript</a>: la référence incontournable pour apprendre JavaScript.
- <a href="https://openclassrooms.com/fr/courses/7696886-apprenez-a-programmer-avec-javascript-1/8204629-declarez-une-variable-1" target="_blank">OpenClassrooms</a>: un cours complet pour débuter en JavaScript.
- <a href="https://www.w3schools.com/js/" target="_blank">W3Schools - JavaScript Tutorial</a>: un tutoriel complet avec des exemples et des exercices (en anglais).
