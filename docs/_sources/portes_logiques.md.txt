(portes_logiques)=

# Portes logiques

Dans cette activité, vous allez concevoir des circuits logiques à l'aide de portes logiques.

Voici par exemple un circuit logique qui permet de calculer la valeur de sortie d'une porte **OU-EXCLUSIF** (XOR) en fonction de ses deux entrées.

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

## 1. Sélecteur de chien 🐶

Dans cette première partie, vous allez concevoir un circuit logique qui permet de sélectionner un chien en fonction de ces différentes caractéristiques.

### Exercice 1.1 - Critères simples

Concevez le circuit de manière à faire en sorte que la sortie «OK» soit allumée (c'est-à-dire, vaille 1) lorsque les 2 entrées sont réglées selon les caractéristiques d'un chien à la fois **petit** et **gentil**.

Les caractéristiques **petit** et **gentil** sont les valeurs logiques d'entrée pouvant valoir 0 ou 1.

```{logic}
:height: 200
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

<!--
#### Solution

Il faut insérer une porte **ET**.

```{logic}
:height: 160
:mode: tryout

{
  "v": 2,
  "in": [{"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0}, {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}],
  "out": [{"pos": [460, 80], "id": 18, "name": "OK"}],
  "gates": [{"type": "AND", "pos": [240, 80], "in": [0, 1], "out": 2}],
  "wires": [[2, 18], [14, 0], [16, 1]]
}
```
-->

### Exercice 1.2 - Critères plus compliqués

1. Les critères sont maintenant devenus plus complexes. Le chien doit remplir les conditions suivantes:

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
  "out": [{"pos": [440, 160], "id": 18, "name": "OK"}]
}
```

<!--
#### Solution Ex 2

```{logic}
:height: 330
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

D'autres solutions sont possibles.
-->

### Exercice 1.3 - Encodage et décodage des races

L'entrée «labrador» de la partie précédente n'est pas très intéressante, car elle ne permet de modéliser qu'une seule race de chiens. Dans cette deuxième partie, on va se permettre d'utiliser **2 bits pour représenter plusieurs races**.

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

On a donc maintenant besoin d'un décodeur: en utilisant les 2 bits d'entrées, il s'agit d'avoir un circuit qui va activer une seule des quatre sorties, celle correspondant à la race du chien représentée selon la table ci-dessus. Par exemple, si les 2 entrées valent 0, alors la sortie «border collie» doit valoir 1 et les autres sorties doivent valoir 0.  

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

<!--
#### Solution Ex 3

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
-->

## 2. Binaire et décimal

Dans cette partie, vous allez concevoir des circuits traduisant des nombres décimaux en nombres binaires.

### Exercice 2.1 - Décodeur de clavier

Complétez le circuit pour un décodeur de touches de clavier qui a le comportement suivant :

* Touche 1 appuyée produit la sortie binaire 01
* Touche 2 appuyée produit la sortie binaire 10
* Touche 3 appuyée produit la sortie binaire 11

```{logic}
:height: 400
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

Ajouter les touches 5, 6, 7, etc suit la même logique mais devient vite fastidieux.

### Exercice 2.2 - Décodeur de dé

Un dé de jeu peut afficher les nombres 1 à 6 à l'aide de 7 lampes.  
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

Utilisez les portes logiques OU et ET pour créer le circuit de décodage affichant les lampes qui correspondent aux nombres 1 à 6.

Le nombre binaire $b_2 b_1 b_0$ doit allumer les lampes a-g pour afficher ce nombre dans la façon d'un dé à jeu standard.

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

<!--
### Exercice 2.1 - Système d'alarmes pour animaux de compagnie

Oublions un moment les chiens et concentrons-nous sur les systèmes d'alarme pour animaux de compagnie. Vous êtes mandaté par une entreprise pour développer un système capable de déclencher une alarme lorsque certaines conditions sont remplies.

1. Analysez la table de vérité ci-dessous. Comprenez quelles sont les conditions qui doivent être remplies pour que l'alarme se déclenche.
2. Concevez le circuit logique correspondant.

| Chien | Chat | Porte ouverte | Propriétaire présent | **Alarme** |
| :---: | :--: | :-----------: | :------------------: | :----: |
|   0   |  0   |       0       |           0           |   0   |
|   0   |  0   |       0       |           1           |   0   |
|   0   |  0   |       1       |           0           |   0   |
|   0   |  0   |       1       |           1           |   0   |
|   0   |  1   |       0       |           0           |   0   |
|   0   |  1   |       0       |           1           |   0   |
|   0   |  1   |       1       |           0           |   1   |
|   0   |  1   |       1       |           1           |   0   |
|   1   |  0   |       0       |           0           |   0   |
|   1   |  0   |       0       |           1           |   0   |
|   1   |  0   |       1       |           0           |   1   |
|   1   |  0   |       1       |           1           |   0   |
|   1   |  1   |       0       |           0           |   0   |
|   1   |  1   |       0       |           1           |   0   |
|   1   |  1   |       1       |           0           |   1   |
|   1   |  1   |       1       |           1           |   0   |

Déterminez d'abord en français les conditions qui doivent être remplies pour que l'alarme se déclenche. Ensuite, concevez le circuit logique correspondant.

```{logic}
:height: 390
:mode: design
:showonly: and,or,xor,not

{
  "v": 5,
  "in": [
    {"pos": [180, 115], "id": 14, "name": "Chien"},
    {"pos": [180, 175], "id": 15, "name": "Chat"},
    {"pos": [180, 235], "id": 16, "name": "Porte ouverte"},
    {"pos": [180, 290], "id": 21, "name": "Propriétaire présent"}
  ],
  "out": [
    {"pos": [660, 195], "id": 22, "name": "Alarme"}
  ]
}
```
-->

## (Challenge) Exercice 3 - Table mystère

Ecrivez le circuit logique correspondant à la table de vérité suivante:

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

Que fait ce circuit d'après vous ?

Si vous avez tout terminé, allez faire un tour sur <a href="https://logic.modulo-info.ch/" target="_blank">logic modulo</a> qui permet de designer des circuits en toute liberté avec des composants plus complexes que ceux vus en cours.
