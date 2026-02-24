// Récupération des éléments HTML nécessaires au jeu //
const Box = document.getElementById("center-box")
const showhits = document.getElementById("hits")
const showtime = document.getElementById("time")
const showCPS = document.getElementById("cps")
const scd5Box = document.getElementById("5-click")
const scd10Box = document.getElementById("10-click")

// Variables principales du jeu //
let compteurClics = 0;          // Compte le nombre total de clics
let Ok = -1;                    // Sert à détecter le premier clic pour lancer le timer une seule fois
let time = 0;                   // Temps écoulé depuis le début du test (pas affiché)
let startTime = false;          // Indique si le timer est actif ou non
let CPS = 0;                    // Clicks par seconde
let timerDuration = 5000;       // Durée du test en millisecondes
let downtime = timerDuration/1000  // Durée du test en secondes (affiché)

// Met à jour l’affichage du nombre de clics //
function updateHitDisplay() {
    showhits.textContent = `= ${compteurClics}`;
}

// Met à jour l’affichage du temps restant //
function updateTimeDisplay() {
    result = downtime - time
    result = parseInt(result*100)/100 // Arrondi à 2 décimales
    showtime.textContent = `= ${result}s`;
}

// Met à jour l’affichage des CPS //
function updateCPSDisplay() {
    console.log(showCPS)
    showCPS.textContent = `= ${CPS}`;
}

function hit() { // Fonction appelée à chaque clic ou appui sur espace
    compteurClics += 1;          // Augmente le nombre de clics
    Ok += 1;                     // Permet de détecter le premier clic
    console.log("Nombre de clics :", compteurClics);
    updateHitDisplay(); 
    if (Ok== 0){ // Lance le timer uniquement au premier clic
        setTimeout(() => { // Ce bloc s’exécute à la fin du timer. Il analyze le cps et affiche une alert en fonction du résultat.
        if (CPS<5){
            alert("Le timer de " + timerDuration/1000 +" secondes est terminé ! Tu click " + CPS +" fois par secondes, c'est lent... Réessaye !" );}
        if (CPS<10  && CPS>5){
            alert("Le timer de " + timerDuration/1000 +" secondes est terminé ! Tu click " + CPS +" fois par secondes, c'est la vitesse moyenne.");}
        if (CPS>=10){
            alert("Le timer de " + timerDuration/1000 +" secondes est terminé ! Tu click " + CPS +" fois par secondes, c'est une vitesse impréssionante, Bravo !.");}
        
        // Réinitialisation complète du jeu
        compteurClics = 0;
        Ok = -1;
        time = 0
        CPS = 0
        downtime = timerDuration/1000
        startTime = false

        console.log("5000ms écoulées. Alerte affichée.");
        }, timerDuration ); // Pendant le temps en miliseconde définis par timerduration
        startTime = true}  // Active le comptage du temps
    }

setInterval(function() { // Fonction exécutée toutes les 5 millisecondes
    if (startTime) {
        time = time + 0.006 // Augmente le temps
        time = parseInt(time*1000)/1000 // Arrondi du temps
        CPS = compteurClics/time // Calcul du CPS
        CPS = parseInt(CPS*100)/100 // Arrondi du CPS
        updateTimeDisplay()
        updateCPSDisplay()
        if (time >= timerDuration/1000){ // Arrête le timer si le temps est écoulé
            startTime = false
            }
        }
    },
5)

Box.addEventListener('click', hit); // Vérifie les clics dans la boite (souris)

document.addEventListener('keydown', function(e) { // Vérifie les clics dans la boite (barre espace)
    // Détection du clavier
    if (e.code === "Space") {
        hit();
    }
});


scd5Box.addEventListener('click', function()  { timerDuration = 5000; downtime = timerDuration/1000;}); // Change la durée du test à 5 secondes
scd10Box.addEventListener('click', function() { timerDuration = 10000; downtime = timerDuration/1000;}); // Change la durée du test à 10 secondes
