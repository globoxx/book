(prog_jeu.projet)=

# Projet

Plongez vous dans la peau d'un développeur de jeu 2D et concevez votre propre jeu !

## Cahier des charges

```{admonition} Liberté et créativité
:class: note
Vous avez carte blanche concernant le contenu de votre jeu. Cela concerne les images, sons et musiques mais également le gameplay (tant que vous suivez les critères donnés).
```

```{admonition} Critères à respecter:
:class: note
- Le jeu est différent des tutoriels (même si une base commune peut exister).
- Le jeu est jouable, possède un objectif clair, ne contient pas de bug évident et ne plante pas.
- Le jeu comporte au moins 1 acteur déplaçable par l'utilisateur (à la souris ou au clavier).
- Le jeu comporte au moins 2 autres types d'acteurs différents qui se déplacent ou intéragissent avec le joueur.
- Il est possible de perdre et un game over doit alors s'afficher.
- Il est possible de gagner ou d'augmenter un score indéfiniment.
- Le jeu comporte au moins 1 musique de fond et 1 bruitage.
- Le jeu est développé de manière continue (pas de travail à la dernière minute).
- Le jeu est rendu à temps et défendu oralement.

Suivre les critères ci-dessus vous garantira la note minimale de 5.  
La note maximale est atteignable en ajoutant des éléments bonus.

**Bonus:**
- Des créations artistiques personnelles (images, animations, musiques).
- Des éléments de gamplay complexes (ex: améliorations difficiles vues en tutoriel).
- Une créativité particulière au niveau du gameplay (ex: un gameplay très différent de ce qui a été vu en tutoriel).
- Des notions de programmation non vues en cours.
```

```{admonition} Plagiat et tricherie
:class: attention
Vous n'êtes pas autorisé à simplement copier-coller du code trouvé sur Internet où dans d'autres groupes sans citer la source.

Il est cependant autorisé de s'inspirer de code d'autrui et de le modifier pour le faire sien. Dans ce cas, il vous est demandé d'ajouter un commentaire dans le code indiquant sa source.

L'utilisation d'IA génératives telles que ChatGPT est autorisée à des fins d'assistance (avec commentaire indiquant son utilisation). Il n'est pas autorisé d'utiliser directement le code produit par une IA et de le coller dans son code en faisant 2-3 modifications sans citer son utilisation (sachez que cela se voit tout de suite).

Enfin, **chaque ligne de code doit pouvoir être expliquée et défendue par le groupe**. Une présentation orale de votre travail aura lieu pour évaluer cette compréhension.
```

## Ressources de base

Téléchargez ici la structure de base pour démarrer votre projet.

{download}`Téléchargement des ressources du projet<../data/prog_2d/projet.zip>`.

Les dossiers `images`, `sounds` et `music` contiennent déjà toutes les ressources utilisées lors des tutoriels (et un peu plus).

## Travailler en dehors des TP

`````{admonition} Comment travailler en dehors du TP
:class: danger
````{dropdown} Depuis la maison
1. Récupérez votre projet depuis OneDrive. Vous devriez le voir dans "Mes fichiers" et vous pouvez le télécharger en cliquant sur les 3 petits points à côté du nom de votre projet et en sélectionnant "Télécharger".
2. Téléchargez et installez [Python](https://www.python.org/downloads/). **Attention, téléchargez une version entre 3.10 et 3.13, mais pas la version 3.14 ou supérieure.**
3. Téléchargez et installez [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/download/). Faites attention à sélectionner la version qui correspond à votre système d'exploitation (Windows, MacOS, Linux).
4. Ouvrez Pycharm et créez un nouveau projet. (Bouton "New Project" sur l'écran d'accueil ou via le menu "File" -> "New Project"). Il devrait par défaut prendre l'unique version de python installée sur votre ordinateur, mais si ce n'est pas le cas, sélectionnez la bonne version de Python (3.10 à 3.13). Validez.
5. Déplacez les fichiers et dossiers de votre jeu dans le dossier de votre projet (PythonProject par défaut).
6. Installez le package `pgzero`. Pour cela, assurez-vous d'avoir la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
````{dropdown} Depuis l'école
1. Ouvrez Pycharm et créez un nouveau projet (Bouton "New Project" sur l'écran d'accueil ou via le menu "File" -> "New Project"). **Attention, choisissez une version de Python entre 3.10 et 3.13, mais pas la version 3.14 ou supérieure.** Validez.
2. Récupérez votre projet. Il peut se trouver sur OneDrive, sur Moodle ou sur votre disque réseau (pxxxxx) selon votre situation. Dans les 2 premiers cas, il faut bien télécharger le dossier de votre projet. Sur OneDrive, vous devriez le voir dans "Mes fichiers" et vous pouvez le télécharger en cliquant sur les 3 petits points à côté du nom de votre projet et en sélectionnant "Télécharger".
3. Déplacez le dossier de votre jeu dans le dossier de votre projet (PythonProject par défaut). **Attention**, si vous prenez votre dossier depuis votre disque réseau (pxxxxx), il faudra le copier sur le bureau avant de le déplacer dans Pycharm.
4. Installez le package `pgzero`. Pour cela, assurez-vous d'avoir la ligne `import pgzero` tout en haut de votre code et Pycharm vous proposera de l'installer **en passant le curseur de la souris dessus** (sur `pgzero`).
```{image} ../media/pgzero.png
```
Programmez !
````
`````

## Rendre le projet

```{admonition} 
class: info

1. Rendez-vous sur la page Moodle du cours et descendez jusqu'à la section de rendu du projet.
2. Retrouvez le dossier de votre projet sur votre ordinateur avec le Finder (Mac) ou l'Explorateur de fichiers (Windows). Depuis Pycharm et si vous ne savez pas où est sauvegardé votre projet, vous pouvez faire un clic droit sur le dossier de votre projet et sélectionner "Open In" -> "Finder". Cela ouvrira le Finder avec le dossier de votre projet.
3. Si Moodle refuse le dépôt de votre dossier, zippez le dossier. Sur Mac, faites un clic droit sur le dossier de votre projet et sélectionnez "Compresser". Sur Windows, faites un clic droit sur le dossier de votre projet, sélectionnez "Envoyer vers" puis "Dossier compressé".
Cela créera un fichier `.zip` que vous pourrez ensuite déposer sur Moodle.
```