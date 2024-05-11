(divers.portes_logiques)=

# Portes logiques

Dans cette activité, vous allez concevoir des circuits logiques à l'aide de portes logiques.

Voici par exemple un circuit logique qui permet de calculer la valeur de sortie d'une porte **OU-Exclusif** (XOR) en fonction de ses 2 entrées.

```{logic}
:height: 160
:mode: tryout
{
  "v": 4,
  "in": [
    {"pos": [40, 30], "id": 0, "val": 0},
    {"pos": [40, 110], "id": 47, "val": 0}
  ],
  "out": [
    {"pos": [430, 50], "id": 59}
  ],
  "gates": [
    {"type": "OR", "pos": [170, 40], "in": [48, 49], "out": 50},
    {"type": "AND", "pos": [170, 100], "in": [51, 52], "out": 53},
    {"type": "NOT", "pos": [250, 100], "in": 54, "out": 55},
    {"type": "AND", "pos": [360, 50], "in": [56, 57], "out": 58}
  ],
  "wires": [[0, 48], [47, 49], [0, 51], [47, 52], [53, 54], [50, 56], [55, 57], [58, 59]]
}
```

Pour rappel, le **OU-Exclusif** (XOR) sort un 1 en sortie si et seulement si il y a un nombre impair de 1 en entrée. Gardez le curseur de la souris sur cette porte XOR à 3 entrées pour voir sa table de vérité.

```{logic}
:height: 160
:mode: connect
{
  v: 6,
  components: {
    in0: {type: 'in', pos: [40, 30], id: 0},
    in1: {type: 'in', pos: [40, 70], id: 1},
    in2: {type: 'in', pos: [40, 110], id: 2},
    out0: {type: 'out', pos: [225, 70], id: 3},
    xor0: {type: 'xor', pos: [145, 70], in: '7-9', out: 10, bits: 3},
  },
  wires: [[10, 3], [0, 7], [1, 8], [2, 9]]
}
```

## 1. Sélecteur de chien 🐶

Dans cette première partie, vous allez concevoir un circuit logique qui permet de sélectionner un chien en fonction de ces différentes caractéristiques.

### Exercice 1.1 - Critères simples

Concevez le circuit de manière à faire en sorte que la sortie «OK» soit allumée (c'est-à-dire, vaille 1) lorsque les 2 entrées sont réglées selon les caractéristiques d'un chien à la fois **petit** et **gentil**.

Voici la table de vérité associée:
  | Petit                 | Gentil          | OK          |
  | :-------------------: | :---------------| :-----------|
  | 0                     | 0               | 0           |
  | 0                     | 1               | 0           |
  | 1                     | 0               | 0           |
  | 1                     | 1               | 1           |

```{logic}
:height: 300
:mode: design
:showonly: in,out,and,or,xor

{
  "v": 2,
  "opts": {"showOnly": ["and", "or", "xor", "not"]},
  "in": [
    {"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}
],
  "out": [{"pos": [360, 80], "id": 18, "name": "OK"}]
}
```

`````{admonition} Solution 1.1
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Il suffit d'insérer une porte **ET**.

```{logic}
:height: 300
:mode: tryout

{
  "v": 2,
  "in": [{"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0}, {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}],
  "out": [{"pos": [460, 80], "id": 18, "name": "OK"}],
  "gates": [{"type": "AND", "pos": [240, 80], "in": [0, 1], "out": 2}],
  "wires": [[2, 18], [14, 0], [16, 1]]
}
```
````
`````

### Exercice 1.2 - Critères plus compliqués

Les critères sont maintenant devenus plus complexes. Le chien doit remplir les conditions suivantes:

* Le chien doit être gentil;
* Le chien ne doit pas baver tout le temps;
* Il faut soit que ce soit un petit chien, soit que ce soit un labrador.
  
Pour tester, par exemple, si un gentil petit berger allemand qui ne bave pas tout le temps est un candidat à être récupéré, on règlera les entrées suivantes:

* Gentil: 1 (le chien est gentil)
* Bave tout le temps: 0 (le chien ne bave pas tout le temps)
* Petit: 1 (le chien est un petit chien)
* Labrador: 0 (le chien n'est pas un labrador)

On s'attend dans ce cas à ce que la sortie «OK» vaille 1.  

```{logic}
:height: 320
:mode: design
:showonly: in,out,and,or,xor,not

{
  "v": 2,
  "in": [
    {"pos": [190, 70], "id": 14, "name": "Gentil", "val": 1},
    {"pos": [190, 130], "id": 15, "name": "Bave tout le temps", "val": 0},
    {"pos": [190, 190], "id": 16, "name": "Petit", "val": 1},
    {"pos": [190, 250], "id": 17, "name": "Labrador", "val": 0}
  ],
  "out": [{"pos": [540, 160], "id": 18, "name": "OK"}]
}
```

`````{admonition} Solution 1.2
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Il existe de multiples solutions, en voici une.

```{logic}
:height: 320
:mode: tryout

{
  "v": 2,
  "in": [
    {"pos": [190, 70], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [190, 130], "id": 15, "name": "Bave tout le temps", "val": 0},
    {"pos": [190, 190], "id": 16, "name": "Petit", "val": 0},
    {"pos": [190, 250], "id": 17, "name": "Labrador", "val": 0}
  ],
  "out": [{"pos": [490, 210], "id": 18, "name": "OK pour ce chien!"}],
  "gates": [
    {"type": "AND", "pos": [420, 210], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [310, 220], "in": [3, 4], "out": 5},
    {"type": "AND", "pos": [340, 120], "in": [6, 7], "out": 8},
    {"type": "NOT", "pos": [260, 130], "in": 9, "out": 10}
  ],
  "wires": [[2, 18], [8, 0], [14, 6], [15, 9], [10, 7], [16, 3], [17, 4], [5, 1]]
}
```
````
`````

### Exercice 1.3 - Encodage et décodage des races

L'entrée «labrador» de la partie précédente n'est pas très intéressante, car elle ne permet de modéliser qu'une seule race de chiens. Dans cette deuxième partie, on va tenter **d'encoder différentes races de chien avec seulement 2 bits**.

```{question}
Combien de races pourra-t-on au maximum représenter si on se permet d'utiliser 2 entrées ?

{f}`1`  
{f}`2`  
{v}`4`  
{f}`8`  
{f}`1 million`
===
Nous pourrons représenter 4 races car nous avons 4 possibilités: 00, 01, 10 et 11. De manière générale, avec `n` bits/entrées, on pourra représenter `2^n` races.
```

On va donc s'intéresser à 4 races de chiens: border collie, berger allemand, husky et labrador. On décide de l'encodage suivant:

  | Représentation binaire | Race            |
  | :--------------------: | :---------------|
  | 00                     | border collie   |
  | 01                     | berger allemand |
  | 10                     | husky           |
  | 11                     | labrador        |

On a donc maintenant besoin d'un `décodeur`: en utilisant les 2 bits d'entrées, il s'agit d'avoir un circuit qui va activer **une seule des quatre sorties**, celle correspondant à la race du chien représentée selon la table ci-dessus. Par exemple, si les 2 entrées valent 0, alors la sortie «border collie» doit valoir 1 et les autres sorties doivent valoir 0.  

```{logic}
:height: 390
:mode: design
:showonly: in,out,and,or,xor,not

{
  "v": 2,
  "in": [
    {"pos": [120, 80], "orient": "s", "id": 0, "val": 0},
    {"pos": [160, 80], "orient": "s", "id": 1, "name": "Code de la race du chien sur 2 bits", "val": 0}
  ],
  "out": [
    {"pos": [460, 190], "id": 2, "name": "c’est un border collie"},
    {"pos": [460, 310], "id": 3, "name": "c’est un labrador"},
    {"pos": [460, 270], "id": 4, "name": "c’est un husky"},
    {"pos": [460, 230], "id": 5, "name": "c’est un berger allemand"}
  ]
}
```

`````{admonition} Solution 1.3
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{logic}
:height: 390
:mode: tryout

{
  "v": 2,
  "in": [
    {"pos": [120, 80], "orient": "s", "id": 0, "val": 0},
    {"pos": [160, 80], "orient": "s", "id": 1, "name": "Code de la race du chien sur 2 bits", "val": 0}
  ],
  "out": [
    {"pos": [460, 190], "id": 2, "name": "c’est un border collie"},
    {"pos": [460, 310], "id": 3, "name": "c’est un labrador"},
    {"pos": [460, 270], "id": 4, "name": "c’est un husky"},
    {"pos": [460, 230], "id": 5, "name": "c’est un berger allemand"}
  ],
  "gates": [
    {"type": "AND", "pos": [210, 310], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [360, 270], "in": [9, 10], "out": 11},
    {"type": "NOT", "pos": [230, 110], "in": 12, "out": 13},
    {"type": "NOT", "pos": [230, 160], "in": 14, "out": 15},
    {"type": "AND", "pos": [390, 120], "in": [16, 17], "out": 18},
    {"type": "AND", "pos": [360, 210], "in": [19, 20], "out": 21}
  ],
  "wires": [
    [8, 3],
    [1, 6],
    [0, 7],
    [11, 4],
    [1, 12],
    [0, 14],
    [18, 2],
    [13, 16],
    [15, 17],
    [21, 5],
    [13, 9],
    [0, 10, {"via": [[240, 280]]}],
    [15, 19],
    [1, 20, {"via": [[200, 220]]}]
  ]
}
```
La <a href="http://serge.mehl.free.fr/anx/lois_morgan.html" target="_blank">loi de De Morgan</a> permet de remplacer toutes les portes **ET** par des portes **OU** et inversement. Le même circuit peut donc être réalisé avec des portes **OU**.
````
`````

## 2. Binaire et décimal

Dans cette partie, vous allez concevoir des circuits traduisant des nombres décimaux en nombres binaires.

### Exercice 2.1 - Décodeur de clavier

Complétez le circuit pour un décodeur de touches de clavier qui a le comportement suivant :

* Touche 1 appuyée produit la sortie binaire 01
* Touche 2 appuyée produit la sortie binaire 10
* Touche 3 appuyée produit la sortie binaire 11

```{logic}
:height: 300
:showonly: in out or
{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 80], "id": 1, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 130], "id": 2, "name": "3", "val": 0, "isPushButton": true}
  ],
  "gates": [{"type": "OR", "pos": [220, 40], "in": [6, 7], "out": 8}],
  "out": [{"pos": [300, 150], "orient": "s", "id": 10}, {"pos": [350, 150], "orient": "s", "id": 11}],
  "wires": [[0, 6], [2, 7], [8, 11]]
}
```

`````{admonition} Solution 2.1
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{logic}
:height: 300
:mode: tryout

{
  v: 6,
  components: {
    in0: {type: 'in', pos: [50, 30], id: 0, name: '1', isPushButton: true},
    in1: {type: 'in', pos: [50, 80], id: 1, name: '2', isPushButton: true},
    in2: {type: 'in', pos: [50, 130], id: 2, name: '3', isPushButton: true},
    out0: {type: 'out', pos: [300, 150], orient: 's', id: 10},
    out1: {type: 'out', pos: [350, 150], orient: 's', id: 11},
    or0: {type: 'or', pos: [220, 40], in: [6, 7], out: 8},
    or1: {type: 'or', pos: [200, 110], in: [3, 4], out: 5},
  },
  wires: [[0, 6], [2, 7], [8, 11], [1, 3], [2, 4], [5, 10]]
}
```
Ajouter les touches 4 à 9 suit la même logique mais devient vite fastidieux (mais vous auriez besoin d'augmenter le nombre de bits de sortie).
````
`````

### Exercice 2.2 - Décodeur de dé

```{image} ../media/de_6_faces.png
:width: 300px
```

Un dé de jeu peut afficher les nombres 1 à 6 à l'aide de 7 petits points que l'on peut représenter par 7 lampes.  
Plusieurs lampes s'allument par paire. Voici la table de vérité.

| b2 | b1 | b0 |valeur| a,g | b,f | c,e | d |
|----|----|:--:|:----:|:---:|:---:|:---:|---|
| 0  | 0  | 0  |      |  0  |  0  |  0  | 0 |
| 0  | 0  | 1  | 1    |  0  |  0  |  0  | 1 |
| 0  | 1  | 0  | 2    |  1  |  0  |  0  | 0 |
| 0  | 1  | 1  | 3    |  1  |  0  |  0  | 1 |
| 1  | 0  | 0  | 4    |  1  |  0  |  1  | 0 |
| 1  | 0  | 1  | 5    |  1  |  0  |  1  | 1 |
| 1  | 1  | 0  | 6    |  1  |  1  |  1  | 0 |
| 1  | 1  | 1  |      |  1  |  1  |  1  | 1 |

Utilisez les portes logiques `OU` et `ET` pour créer le circuit de décodage affichant les lampes qui correspondent aux nombres 1 à 6.

Le nombre binaire $b_2 b_1 b_0$ doit allumer les lampes a-g pour afficher ce nombre dans la façon d'un dé à 6 faces.  
Pour résoudre l'exercice, il est nécessaire de trouver la fonction logique associée à chaque sortie. Par exemple, la sortie 'a,g' vaut 1 si et seulement si b1 ou b2 vaut 1.  

```{logic}
:height: 300
:showonly: in and or out.bar
{
  "v": 4,
  "opts": {"propagationDelay": 10},
  "in": [
    {"pos": [60, 40], "id": 7, "name": "b0", "val": 1},
    {"pos": [60, 80], "id": 8, "name": "b1", "val": 0},
    {"pos": [60, 120], "id": 26, "name": "b2", "val": 1}
  ],
  "out": [
    {"type": "bar", "pos": [380, 30], "id": 0, "display": "px", "name": "a"},
    {"type": "bar", "pos": [380, 70], "id": 1, "display": "px", "name": "b"},
    {"type": "bar", "pos": [430, 70], "orient": "s", "id": 2, "display": "px", "name": "d"},
    {"type": "bar", "pos": [380, 120], "id": 3, "display": "px", "name": "c"},
    {"type": "bar", "pos": [480, 70], "id": 4, "display": "px", "name": "f"},
    {"type": "bar", "pos": [480, 30], "id": 5, "display": "px", "name": "e"},
    {"type": "bar", "pos": [480, 120], "id": 6, "display": "px", "name": "g"}
  ]
}
```

`````{admonition} Solution 2.2
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{logic}
:height: 300
:mode: tryout

{
  v: 6,
  opts: {propagationDelay: 10},
  components: {
    in0: {type: 'in', pos: [60, 40], id: 7, name: 'b0', val: 1},
    in1: {type: 'in', pos: [60, 80], id: 8, name: 'b1'},
    in2: {type: 'in', pos: [60, 120], id: 26, name: 'b2', val: 1},
    bar0: {type: 'bar', pos: [535, 45], id: 0, name: 'a', display: 'px'},
    bar1: {type: 'bar', pos: [535, 85], id: 1, name: 'b', display: 'px'},
    bar2: {type: 'bar', pos: [585, 85], orient: 's', id: 2, name: 'd', display: 'px'},
    bar3: {type: 'bar', pos: [535, 135], id: 3, name: 'c', display: 'px'},
    bar4: {type: 'bar', pos: [635, 85], id: 4, name: 'f', display: 'px'},
    bar5: {type: 'bar', pos: [635, 45], id: 5, name: 'e', display: 'px'},
    bar6: {type: 'bar', pos: [635, 135], id: 6, name: 'g', display: 'px'},
    or0: {type: 'or', pos: [295, 130], in: [9, 10], out: 11},
    and0: {type: 'and', pos: [295, 210], in: [12, 13], out: 14},
  },
  wires: [[8, 9], [26, 10], [8, 12], [26, 13], [11, 0], [11, 6], [14, 1], [14, 4], [26, 3], [26, 5], [7, 2]]
}
```
Pour résoudre l'exercice, il est conseillé de trouver la fonction logique associée à chaque sortie. Par exemple, la sortie 'a,g' vaut 1 si et seulement si b1 ou b2 vaut 1. On peut donc utiliser une porte **OU** pour cette sortie. On procède ensuite de la même manière pour les autres sorties.
````
````
`````

## 3. Commutateurs

La porte XOR (OU Exclusif) peut permetre d'allumer et éteindre une lampe avec des commutateurs multiples.

Dans le schéma ci-dessous, on peut allumer ou éteindre la lumière dans une pièce à partir de la porte d'entrée ou de la cuisine.  
Ajoutez un circuit pour qu'on puisse également l'allumer ou l'éteindre depuis la chambre.

```{logic}
:ref: xor
:height: 300
:showonly: in out not and or xor label.rect
{
  "v": 3,
  "labels": [{"type": "rect", "pos": [290, 120], "w": 300, "h": 200, "color": "yellow", "strokeWidth": 2}],
  "in": [
    {"pos": [100, 150], "id": 9, "name": "entrée", "val": 0},
    {"pos": [290, 250], "orient": "n", "id": 14, "name": "chambre", "val": 0},
    {"pos": [470, 120], "orient": "w", "id": 15, "name": "cuisine", "val": 0}
  ],
  "out": [{"type": "bar", "pos": [300, 40], "id": 10, "display": "px", "color": "yellow"}],
  "gates": [{"type": "XOR", "pos": [220, 90], "orient": "n", "in": [11, 12], "out": 13}],
  "wires": [[13, 10], [9, 11], [15, 12]]
}
```

`````{admonition} Solution 3
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{logic}
:height: 300
:mode: tryout

{
  v: 6,
  components: {
    rect0: {type: 'rect', pos: [290, 120], w: 300, h: 200, color: 'yellow', strokeWidth: 2},
    in0: {type: 'in', pos: [100, 150], id: 9, name: 'entrée'},
    in1: {type: 'in', pos: [290, 250], orient: 'n', id: 14, name: 'chambre'},
    in2: {type: 'in', pos: [470, 120], orient: 'w', id: 15, name: 'cuisine'},
    bar0: {type: 'bar', pos: [300, 40], id: 10, color: 'yellow', display: 'px'},
    xor0: {type: 'xor', pos: [190, 140], orient: 'n', in: [11, 12], out: 13},
    xor1: {type: 'xor', pos: [245, 70], orient: 'n', in: [0, 1], out: 2},
  },
  wires: [[9, 11], [15, 12], [14, 1], [13, 0], [2, 10]]
}
```
La porte **XOR** est très utile pour créer des commutateurs. Elle permet de créer un circuit qui ne s'active que si un nombre impair d'entrées sont activées. Il aurait aussi été possible de résoudre cet exercice en utilisant une unique porte XOR à 3 entrées.
````
`````

```{question}
Comment se comporte une porte XOR prenant 3 entrées ? (A XOR B XOR C)  
Dans quel cas la valeur de sortie sera 1 ?

{f}`Seulement quand une seule entrée vaut 1`  
{f}`Seulement quand toutes les entrées valent 1`  
{v}`Seulement quand un nombre impair d'entrées valent 1`  
{f}`Seulement quand un nombre pair d'entrées valent 1`  
{f}`Jamais`
===
De manière générale, la porte XOR est un détecteur de parité (pair/impair). La sortie vaut 1 seuelement si un nombre impair d'entrées valent 1 (ce qui est une propriété extrêmement utile).
```

## 4. Table mystère (Challenge)

Créez le circuit logique correspondant à la table de vérité suivante:

| A | B | C | S1 | S2 |
|:-:|:-:|:---:|:----:|:---:|
| 0 | 0 |  0  |  0   |  0  |
| 0 | 0 |  1  |  0   |  1  |
| 0 | 1 |  0  |  0   |  1  |
| 0 | 1 |  1  |  1   |  0  |
| 1 | 0 |  0  |  0   |  1  |
| 1 | 0 |  1  |  1   |  0  |
| 1 | 1 |  0  |  1   |  0  |
| 1 | 1 |  1  |  1   |  1  |

```{logic}
:height: 390
:mode: design
:showonly: in,out,and,or,xor,not

{
  "v": 5,
  "in": [
    {"pos": [100, 115], "id": 14, "name": "A"},
    {"pos": [100, 175], "id": 15, "name": "B"},
    {"pos": [100, 235], "id": 16, "name": "C"}
  ],
  "out": [
    {"pos": [660, 150], "id": 22, "name": "S1"},
    {"pos": [660, 195], "id": 23, "name": "S2"}
  ]
}
```

Que fait ce circuit d'après vous ? Plus précisément, quelle opération fait-il ?

`````{admonition} Solution 4
:class: hint
````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{logic}
:height: 390
:mode: tryout

{
  v: 6,
  components: {
    in0: {type: 'in', pos: [100, 115], id: 14, name: 'A'},
    in1: {type: 'in', pos: [100, 175], id: 15, name: 'B'},
    in2: {type: 'in', pos: [100, 235], id: 16, name: 'C'},
    out0: {type: 'out', pos: [660, 150], id: 22, name: 'S1'},
    out1: {type: 'out', pos: [660, 195], id: 23, name: 'S2'},
    and0: {type: 'and', pos: [370, 50], in: [0, 1], out: 2},
    and1: {type: 'and', pos: [370, 110], in: [3, 4], out: 5},
    and2: {type: 'and', pos: [370, 170], in: [6, 7], out: 8},
    or0: {type: 'or', pos: [540, 110], in: [12, 13, 17], out: 18, bits: 3},
    xor0: {type: 'xor', pos: [385, 280], in: '24-26', out: 27, bits: 3},
  },
  wires: [[14, 0], [15, 1], [14, 3], [16, 4], [15, 6], [16, 7], [2, 12], [5, 13], [8, 17], [14, 24], [15, 25], [16, 26], [27, 23], [18, 22]]
}
```
Ce circuit représente un additionneur 3 bits (full adder). Il permet d'additionner 3 bits A, B et C et de récupérer le résultat sur 2 bits S1 et S2.
````
`````

Si vous avez tout terminé, vous pouvez faire un tour sur <a href="https://logic.modulo-info.ch/" target="_blank">logic modulo</a> qui permet de designer des circuits en toute liberté avec des composants plus complexes que ceux vus en cours. Vous pouvez aussi visiter <a href="https://dev-apprendre.modulo-info.ch/archi/tp2.html#addition-binaire" target="_blank">cette page modulo</a> qui contient des exercices plus avancés sur les additionneurs (à partir de l'exercice 10.6).
