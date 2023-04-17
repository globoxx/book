(portes_logiques)=

# Portes logiques

Dans cette activité, vous allez concevoir des circuits logiques à l'aide de portes logiques.

## 1. Sélecteur de chien

Dans cette première partie, vous allez concevoir un circuit logique qui permet de sélectionner un chien en fonction de ces différentes caractéristiques.

### Exercice 1.1

Concevez le circuit de manière à faire en sorte que la sortie «OK pour ce chien» soit allumée (c'est-à-dire, vaille 1) lorsque les 2 entrées sont réglées selon les caractéristiques d'un chien précis et que ce chien est à la fois **petit** et **gentil**.

Les caractéristiques **petit** et **gentil** sont sont les valeurs logiques d'entrée pouvant valoir 0 ou 1.

```{logic}
:height: 200
:mode: design
:showonly: and,or,xor

{
  "v": 2,
  "opts": {"showOnly": ["and", "or", "xor", "not"]},
  "in": [
    {"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}
],
  "out": [{"pos": [360, 80], "id": 18, "name": "OK pour ce chien!"}]
}
```

#### Solution

Il faut insérer une porte **ET**.

```{logic}
:height: 160
:mode: tryout

{
  "v": 2,
  "in": [{"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0}, {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}],
  "out": [{"pos": [360, 80], "id": 18, "name": "OK pour ce chien!"}],
  "gates": [{"type": "AND", "pos": [240, 80], "in": [0, 1], "out": 2}],
  "wires": [[2, 18], [14, 0], [16, 1]]
}
```

### Exercice 1.2 - critères plus compliqués

1. Les critères sont maintenant devenus plus complexes. Le chien doit remplir les conditions suivantes:

* Le chien doit être gentil;
* Le chien ne doit pas baver tout le temps;
* Il faut soit que ce soit un petit chien, soit que ce soit un labrador.
  
Pour tester, par exemple, si un gentil petit berger allemand qui ne bave pas tout le temps est un candidat à être récupéré, on règlera les entrées suivantes:

* Gentil: 1 (le chien est gentil)
* Bave tout le temps: 0 (le chien ne bave pas tout le temps)
* Petit: 1 (le chien est un petit chien)
* Labrador: 0 (le chien n'est pas un labrador)

On s'attend dans ce cas à ce que la sortie «OK pour ce chien» vaille 1.

```{logic}
:height: 320
:mode: design
:showonly: and,or,xor,not

{
  "v": 2,
  "in": [
    {"pos": [190, 70], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [190, 130], "id": 15, "name": "Bave tout le temps", "val": 0},
    {"pos": [190, 190], "id": 16, "name": "Petit", "val": 0},
    {"pos": [190, 250], "id": 17, "name": "Labrador", "val": 0}
  ],
  "out": [{"pos": [440, 160], "id": 18, "name": "OK pour ce chien!"}]
}
```

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

### Exercice 1.3 - encodage et décodage des races

L'entrée «labrador» de la partie précédente n'est pas très intéressante, car elle ne permet de modéliser qu'une seule race de chiens. Dans cette deuxième partie, on va se permettre d'utiliser **2 bits pour représenter plusieurs races**. Faire réfléchir les élèves à ceci: combien de races pourra-t-on au maximum représenter si on se permet d'utiliser deux entrées ? La réponse est 4 et non pas 2.

```{question}
Combien de races pourra-t-on au maximum représenter si on se permet d'utiliser 2 entrées ?

{v}`1`  
{f}`2`  
{v}`4`  
{f}`1 million`
===
Nous pourrons bien représenter 4 races car nous avons 4 possibilités: 00, 01, 10 et 11. De manière générale, avec `n` bits/entrées, on peut représenter `2^n` races.
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
:showonly: and,or,xor,not

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

<!-- ### Quatrième partie: conditions avec décodage

Dans cette partie, nous allons combiner les concepts de décodage des races de chiens avec les critères de sélection abordés dans la partie 3.  
Réalisez un circuit logique qui prend en compte à la fois les critères et les races de chiens encodées sur 2 bits.

### Exercice 4

1. Concevez un circuit logique qui prend en compte les critères de sélection définis dans la partie 2:

* Le chien doit être gentil;
* Le chien ne doit pas baver tout le temps;
* Il faut soit que ce soit un petit chien, soit que ce soit un labrador.

De plus, prenez en compte l'encodage des races de chiens (border collie, berger allemand, husky et labrador) que nous avons défini dans la partie 3.

Les entrées de votre circuit logique doivent inclure:

* Gentil (1 bit)
* Bave tout le temps (1 bit)
* Petit (1 bit)
* Race (2 bits)

Utilisez le décodeur que vous avez créé dans l'exercice 3 pour convertir les 2 bits d'entrée de la race en 4 sorties correspondant à chaque race de chien. Ensuite, utilisez ces sorties pour vérifier si le chien est un labrador ou non.

```{logic}
:height: 390
:mode: design
:showonly: and,or,xor,not

{
  "v": 5,
  "in": [
    {"pos": [470, 115], "id": 14, "name": "Gentil"},
    {"pos": [470, 175], "id": 15, "name": "Bave tout le temps"},
    {"pos": [470, 235], "id": 16, "name": "Petit"},
    {"bits": 2, "pos": [470, 300], "id": [4, 5], "name": "Race du chien"}
  ],
  "out": [
    {"pos": [860, 215], "id": 18, "name": "OK pour ce chien!"}
  ]
}
```

#### Solution

Pour résoudre cet exercice, vous devrez d'abord connecter les entrées de race au décodeur que vous avez conçu dans l'exercice 3. Ensuite, vous devrez combiner les résultats du décodeur avec les autres entrées (gentil, bave tout le temps et petit) à l'aide de portes logiques appropriées (comme les portes ET, OU, NON, etc.) pour respecter les critères de sélection.

Une fois que vous avez réussi à concevoir le circuit logique, testez-le avec différentes combinaisons d'entrées pour vous assurer qu'il fonctionne correctement et répond aux critères de sélection.
 -->

## 2. Circuit à partir d'une table de vérité

Dans cette partie, vous allez convevoir des circuits en vous basant sur la table de vérité associée.

### Exercice 2.1 - Système d'alarmes pour animaux de compagnie

Oublions un moment les chiens et concentrons-nous sur les systèmes d'alarme pour animaux de compagnie. Vous êtes mandaté par une entreprise pour développer un système capable de déclencher une alarme lorsque certaines conditions sont remplies.

1. Analysez la table de vérité ci-dessous. Comprenez quelles sont les conditions qui doivent être remplies pour que l'alarme se déclenche.
2. Concevez le circuit logique correspondant.

| Chien | Chat | Porte ouverte | Propriétaire présent | Alarme |
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

Les entrées de votre circuit logique doivent inclure:

* Chien (1 bit)
* Chat (1 bit)
* Porte ouverte (1 bit)
* Propriétaire présent (1 bit)

La sortie de votre circuit doit être l'alarme (1 bit).

```{logic}
:height: 390
:mode: design
:showonly: and,or,xor,not

{
  "v": 5,
  "in": [
    {"pos": [470, 115], "id": 14, "name": "Chien"},
    {"pos": [470, 175], "id": 15, "name": "Chat"},
    {"pos": [470, 235], "id": 16, "name": "Porte ouverte"},
    {"pos": [470, 290], "id": 21, "name": "Propriétaire présent"}
  ],
  "out": [
    {"pos": [830, 195], "id": 22, "name": "Alarme"}
  ]
}
```

## Exercice 2.2 - Table mystère

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

Les valeurs d'entrée sont A, B et C. Les valeurs de sortie sont S1 et S2.

```{logic}
:height: 390
:mode: design
:showonly: and,or,xor,not

{
  "v": 5,
  "in": [
    {"pos": [470, 115], "id": 14, "name": "A"},
    {"pos": [470, 175], "id": 15, "name": "B"},
    {"pos": [470, 235], "id": 16, "name": "C"}
  ],
  "out": [
    {"pos": [770, 150], "id": 22, "name": "S1"},
    {"pos": [770, 195], "id": 23, "name": "S2"}
  ]
}
```

Que fait ce circuit d'après vous ?

