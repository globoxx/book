
document.getElementById("submit").onclick = function() {
    let nbrnote = Number(document.getElementById("nbrnote").value);
    if (nbrnote % 1 != 0) {
        alert("Veuillez entrer un nombre entier de notes");
        return;
    }
    let moyvoul = Number(document.getElementById("moyvoul").value);
    let somme = 0; //s pour somme

    for (let i = 0; i < nbrnote; i++) {
        let x; //définit x sans lui donner de valeur pour pouvoir l'utiliser
        do { //pour pouvoir éxécuter la boucle au moins une fois sans avertissement
            x = Number(prompt("Veuillez entrer une note entre 1 et 6 :"));
            if (x < 1 || x > 6 || isNaN(x)) {
                alert("Veuillez entrer une note valide entre 1 et 6.");
            }
        } while (x < 1 || x > 6 || isNaN(x)); //continue à demander tant que la note n'est pas dans la plage correcte

        somme += x; //ajoute la note à la somme
    }
    notenec = (moyvoul - 0.25) * (nbrnote + 1) - somme;




    if (notenec > 6) {
        alert("Il vous faudrait une note supérieure à 6 pour avoir une moyenne de " + moyvoul + ". Désolé!");
    } else if (notenec < 1) {
        alert("Il vous faudrait une note inférieure à 1 pour baisser votre moyenne à " + moyvoul + ". Détendez-vous!");
    } else {
        alert("Vous devez obtenir une note de " + notenec.toFixed(1) + " pour avoir une moyenne de " + moyvoul + ". Bonne chance!");
    }
}





document.getElementById("submitmoy").onclick = function() {
    let nbrnote = Number(document.getElementById("nbrnote").value);
    let somme = 0; //s pour somme

    for (let i = 0; i < nbrnote; i++) {
        let x; //définit x sans lui donner de valeur pour pouvoir l'utiliser
        do { //pour pouvoir éxécuter la boucle au moins une fois sans avertissement
            x = Number(prompt("Veuillez entrer une note entre 1 et 6 :"));
            if (x < 1 || x > 6 || isNaN(x)) {
                alert("Veuillez entrer une note valide entre 1 et 6.");
            }
        } while (x < 1 || x > 6 || isNaN(x)); //continue à demander tant que la note n'est pas dans la plage correcte

        somme += x; //ajoute la note à la somme
    }
    let moyenne = somme / nbrnote;
    alert(moyenne)
}




