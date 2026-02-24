// Liste des villages avec leurs coordonnées sur la carte
const villages = [ 
    { name: "Boulens", x: 1, y: 2 },
    { name: "Thierrens", x: 3, y: 4 },
    { name: "Ogens", x: 5, y: 6 },
    { name: "Correvon", x: 6, y: 4 },
    { name: "Neyruz", x: 5, y: 7 },
    { name: "Villars-Tiercelin", x: 3, y: 5 },
    { name: "Sottens", x: 7, y: 6 },
    { name: "Peney-Le-Jorat", x: 8, y: 5 },
    { name: "Chapelle-Sur-Moudon", x: 4, y: 7 },
    { name: "Moudon", x: 5, y: 8 },
    { name: "Peyres-Possens", x: 5, y: 3 },
    { name: "Bioley-Magnoux", x: 6, y: 7 },
    { name: "Donneloye", x: 7, y: 7 },
    { name: "Vuarrens", x: 8, y: 4 },
    { name: "Saint-Cierges", x: 4, y: 3 }
];

// Fonction pour générer un prix aléatoire entre une valeur min et max
function prix_aleatoire(min, max) { 
    return Number((Math.random() * (max - min) + min).toFixed(2));  
}

// Liste des stations essence avec leurs coordonnées et prix
const stations = [
    
    { name: "BP de Thierrens", x: 5, y: 9, price: prix_aleatoire(1.60, 1.90) },
    { name: "Shell de Boulens", x: 4, y: 3 , price: prix_aleatoire(1.60, 1.90)},
    { name: "AVIA d'Ogens", x: 6, y: 7 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Tamoil de Correvon", x: 7, y: 4 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Migrol de Chavannes-sur-Moudon", x: 4, y: 7 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Shell de Neyruz-sur-Moudon", x: 5, y: 8 , price: prix_aleatoire(1.60, 1.90)},
    { name: "BP de Villars-le-Comte", x: 3, y: 6 , price: prix_aleatoire(1.60, 1.90)},
    { name: "AVIA de Montaubion-Chardonney", x: 7, y: 5 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Tamoil de Sottens", x: 8, y: 6 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Migrol de Peney-le-Jorat", x: 8, y: 5 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Shell de Chapelle-sur-Moudon", x: 4, y: 8 , price: prix_aleatoire(1.60, 1.90)},
    { name: "AVIA de Moudon-Haut", x: 5, y: 9 , price: prix_aleatoire(1.60, 1.90)},
    { name: "BP d'Hermonville", x: 6, y: 3 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Tamoil de Peyres", x: 5, y: 3 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Migrol de Montpreveyres", x: 8, y: 7 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Shell de Bioley-Magnoux", x: 6, y: 8 , price: prix_aleatoire(1.60, 1.90)},
    { name: "AVIA de Donneloye", x: 7, y: 7 , price: prix_aleatoire(1.60, 1.90)},
    { name: "BP de Vuarrens", x: 8, y: 4 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Tamoil de Montanaire-Centre", x: 3, y: 4 , price: prix_aleatoire(1.60, 1.90)},
    { name: "Migrol de Saint-Cerque", x: 4, y: 3 , price: prix_aleatoire(1.60, 1.90)}
]; 
// Récupération de l'élément slider pour la consommation
const slider = document.getElementById("conso");
// Récupération de l'élément qui affiche la valeur du slider
const output = document.getElementById("consoValue");
// Initialisation de l'affichage avec la valeur par défaut du slider
output.textContent = slider.value;

// Écouteur d'événement pour mettre à jour l'affichage quand l'utilisateur bouge le slider
slider.oninput = function() {
    // Met à jour le texte affiché avec la nouvelle valeur
    output.textContent = this.value; 
};

// Récupération de l'élément slider pour les litres à acheter
const slider2 = document.getElementById("litres");
// Récupération de l'élément qui affiche la valeur du slider
const output2 = document.getElementById("litresValue");
// Initialisation de l'affichage avec la valeur par défaut du slider
output2.textContent = slider2.value;

// Écouteur d'événement pour mettre à jour l'affichage quand l'utilisateur bouge le slider
slider2.oninput = function() {
    // Met à jour le texte affiché avec la nouvelle valeur
    output2.textContent = this.value; 
};

// Récupération du menu déroulant pour sélectionner le village
const select = document.getElementById("villageSelect");
// Boucle sur tous les villages pour créer les options du menu
villages.forEach(v => {
    // Création d'un nouvel élément option
    const option = document.createElement("option");
    // Définition de la valeur de l'option
    option.value = v.name;
    // Définition du texte affiché dans l'option
    option.textContent = v.name;
    // Ajout de l'option au menu déroulant
    select.appendChild(option);
});

// Fonction qui calcule la distance euclidienne entre deux points
// Utilise le théorème de Pythagore: distance = racine((x2-x1)² + (y2-y1)²)
function distance(a, b) {
    return Math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2);
}

// Fonction qui calcule le coût total pour aller à une station et y faire le plein
// Prend en compte: le trajet aller-retour ET le prix de l'essence achetée
function coutTotal(village, station, conso, litresAchetes) {
    // Calcul de la distance entre le village et la station
    const dist = distance(village, station);
    // Calcul des litres nécessaires pour le trajet (distance * consommation / 100)
    const litresTrajet = dist * (conso / 100);
    // Calcul du coût en essence pour le trajet
    const coutTrajet = litresTrajet * station.price;
    // Calcul du coût de l'essence achetée à la station
    const coutAchat = litresAchetes * station.price;
    // Retourne le coût total (trajet + achat)
    return coutTrajet + coutAchat;
}

// Fonction quand l'utilisateur clique sur Trouver la station
// Elle analyse toutes les stations et trouve la plus rentable
function montrerStation() {
    const villageSelectionne = villages.find(v => v.name === select.value);
    const consoRecup = parseFloat(slider.value);
    const litresAchetes = parseFloat(slider2.value);
    
    // Calcule les coûts pour chaque station disponible
    const resultats = stations.map(s => {
        // Calcul de la distance du village à cette station
        const dist = distance(villageSelectionne, s);
        // Calcul des litres nécessaires pour le trajet
        const litresTrajet = dist * (consoRecup / 100);
        // Calcul du coût total pour cette station
        const cout = coutTotal(villageSelectionne, s, consoRecup, litresAchetes);
        // Retourne un objet avec toutes les infos de cette station
        return {
            station: s,
            cout: cout,
            distance: dist,
            litresTrajet: litresTrajet
        };
    });
    // reduce compare chaque station et garde celle qui coûte le moins cher
    const stationMoinsChere = resultats.reduce((min, current) => 
        current.cout < min.cout ? current : min
    );
    
    // Affichage du résultat et de tout  les détails dans la page HTML
    document.getElementById("resultat").innerHTML = `
        <strong>${stationMoinsChere.station.name}</strong><br>
        Prix: ${stationMoinsChere.station.price.toFixed(2)} CHF/L<br>
        Distance: ${stationMoinsChere.distance.toFixed(2)} km<br>
        Essence pour le trajet: ${stationMoinsChere.litresTrajet.toFixed(2)} L<br>
        Essence à acheter: ${litresAchetes.toFixed(2)} L<br>
        Coût total: ${stationMoinsChere.cout.toFixed(2)} CHF
    `;
}