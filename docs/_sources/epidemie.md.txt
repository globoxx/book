# Simulation d'épidémie

Dans ce chapitre, nous allons simuler l'évolution d'une épidémie grâce à nos connaissances en python. Pour cela, nous allons écrire un **modèle** représentant les différentes caractéristiques de l'épidémie puis nous simulerons le temps qui passe afin de pouvoir mesurer les impacts de la maladie sur la population.

## 1. Caractéristiques de la population

Disons que nous allons jouer avec **une population d'un million de personnes**. Vous allez définir les variables `susceptibles`, `malades`, `gueris` et `morts` qui représentent respectivement le nombres de personnes susceptibles d’attraper la maladie, le nombre de malades, le nombre de guéris et le nombre de morts.
Définissez les valeurs de ces variables **au jour 0** de l'épidémie.

Dans un second temps, vous allez définir une variable `contacts_par_jour` qui représente le nombre de contacts que fait chaque individu par jour. Par exemple, si `contacts_par_jour` vaut 10, cela signifie que chaque personne rencontre en moyenne 10 autres personnes par jour.

```{codeplay}
# Nombre total d'individus: 1 000 000
susceptibles = ...
malades = ...
gueris = ...
morts = ...
```

## 2. Caractéristiques de la maladie

Nous allons maintenant définir les caractéristiques de la maladie. Pour cela, nous utiliserons les variables suivantes:

- `p_infection` qui représente la probabilité qu'un individu malade infecte un individu susceptible lors d'un contact.
- `p_guerison` qui représente la probabilité qu'un individu malade guérisse chaque jour.
- `p_deces` qui représente la probabilité qu'un individu malade meure chaque jour.

```{codeplay}
p_infection = ...
p_guerison = ...
p_deces = ...
```

Voici le diagramme représentant l'évolution d'un individu selon ce modèle:

```{image} prog1/media/epidemie.png
```

## 3. Simulation du jour 1

Nous allons maintenant simuler le jour 1 de l'épidémie. C'est à dire que nous allons calculer nombre de personnes susceptibles, malades, guéris et morts au jour 1. Pour cela, nous allons calculer les variables suivantes:

- `nb_concacts` qui représente le nombre de contacts que font les malades au cours du jour 1. Pour le calcul, vous devrez utilier les variables `malades` et `contacts_par_jour`.
- `nb_contacts_susceptibles` qui représente le nombre de contacts que font les malades **avec des personnes susceptibles** au cours du jour 1. Pour le calcul, multipliez `nb_contacts` avec la proportion de gens susceptibles dans la population (sans compter les morts car on ne rentre pas en contact avec eux).
- `nb_infections` qui représente le nombre de personnes infectées au cours du jour 1. Pour le calcul, vous devrez utilier les variables `nb_contacts_susceptibles` et `p_infection`.
- `nb_guerisons` qui représente le nombre de personnes guéries au cours du jour 1. Pour le calcul, vous devrez utilier les variables `p_guerison` et `malades`.
- `nb_deces` qui représente le nombre de personnes qui meurent au cours du jour 1. Pour le calcul, vous devrez utilier les variables `p_deces` et `malades`.

```{codeplay}
nb_contacts = ...
nb_contacts_susceptibles = ...
nb_infections = ...
nb_guerisons = ...
nb_deces = ...
```

Combien y a-t-il de malades après le premier jour selon ce modèle ? Est-ce que cela vous semble cohérent? Sinon, quelle modification pouvez-vous apporter à votre modèle ?

Nous allons maintenant pouvoir mettre à jour nos variables de population à la fin du jour 1. Calculez les nouvelles valeurs de `susceptibles`, `malades`, `gueris` et `morts` à la fin du jour 1.

```{codeplay}
susceptibles = ...
malades = ...
gueris = ...
morts = ...
```

Que peut-on dire du nombre total de personnes (susceptibles, malades, guéries ou décédées) dans votre modèle ? Cela vous semble-t-il logique ?

## 4. Simulation sur plusieurs jours

Nous allons maintenant simuler l'évolution de l'épidémie sur plusieurs jours. Placer une boucle `for jour in range(10):` au bon endroit de votre code pour que chaque répétition de la boucle corresponde au passage d’un jour.

Combien y a-t-il de malades après 10 jours? Et après 20 jours?

## 5. Visualisation de l'évolution de l'épidémie

On souhaite tracer la courbe des nouvelles infections. Pour cela, définissez (avant la boucle for) une liste vide (`[]`) appelée `courbe_infection`. Cette liste contiendra donc le nombre de nouvelles infections pour chaque jour (`nb_infections`). Pour remplir cette liste, placer l’instruction `courbe_infection.append(nb_infections)` à l’intérieur de la boucle for.

Commençons par afficher le nombre de nouvelles infections les 10 premiers jours avec `print(courbe_infection)`. Est-ce que cela vous semble cohérent ? Sinon quelle modification pouvez-vous apporter à votre modèle ?

Pour visualiser la courbe des nouvelles infections, nous allons utiliser la librairie `matplotlib`. Ajouter l'instruction permettant de l'importer au début de votre programme: `import matplotlib.pyplot as plt`. (Si vous rencontrez une erreur d'import ici, appelez votre enseignant).

Ajoutez ensuite les instructions suivantes à la fin de votre programme pour tracer la courbe des nouvelles infections:

```python
plt.plot(courbe_infection,'-')
plt.xlabel('jours')
plt.ylabel("nombre d'infections")
plt.show()
```

1. Modifier le programme pour tracer un graphique du nombre d’infections les 50 premiers jours.
2. Modifier le programme pour tracer également la courbe des décès sur les 50 premiers jours.

## 6. Expérimentations

Modifiez les paramètres de votre modèle pour voir comment cela impacte l'évolution de l'épidémie. Vous pouvez par exemple:

- Modifier le nombre de personnes dans la population.
- Modifier le nombre moyen de contacts par jour.
- Modifier le taux d'infection.
- Modifier le taux de guérison.
- Modifier le taux de mortalité.

## 7. Covid-19

On souhaite comparer le modèle à l’épidémie de Covid-19 dans le canton de Vaud. Le code suivant vous permet de lire le fichier `covid_vd.csv` et d’obtenir une liste contenant le nombre de nouveaux cas chaque jour.

```python
import csv

cas = []
date = []

with open ("covid_vd.csv") as covid_file:
    reader = csv.reader(covid_file)
    entete = next(reader)
    for row in reader:
        date.append(row[0])
        if row[1]== '':
            cas.append(0)
        else:
            cas.append(float(row[1]))
```

Essayer de trouver les paramètre de votre modèle qui correspondent le mieux à la première vague, puis à la seconde vague.
Quelle vague reflète selon vous le mieux la réelle propagation du virus ?
