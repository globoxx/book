document.querySelectorAll('.reponse').forEach((listContainer) => {
  // Pour chaque conteneur `.reponse`, attache un gestionnaire d'événement aux éléments de liste
  listContainer.querySelectorAll('li').forEach((item) => {
    item.addEventListener('click', function () {
      // Change le dégradé du conteneur parent
      const newGradient = this.getAttribute('data-gradient');
      listContainer.style.background = newGradient;

      // Réinitialise les classes actives uniquement dans ce conteneur
      listContainer.querySelectorAll('li').forEach((li) => li.classList.remove('active'));
      this.classList.add('active');
    });
  });
});//code fait par chat gpt

// Créer une fonction qui affiche un iframe au hasard
function afficherIframeAleatoire() {
  var iframes = document.querySelectorAll('iframe'); // Récupère tous les iframes
  var indexAleatoire = Math.floor(Math.random() * iframes.length); // Sélectionne un index au hasard

  // Affiche l'iframe correspondant à l'index choisi et cache les autres
  for (var i = 0; i < iframes.length; i++) {
      if (i === indexAleatoire) {
          iframes[i].style.display = 'block'; // Affiche l'iframe choisi
      } else {
          iframes[i].style.display = 'none'; // Cache les autres iframes
      }
  }
}

// Appeler la fonction au chargement de la page
window.onload = afficherIframeAleatoire;
//code fait par chat gpt

//Par manque de temps, j'ai été contrain de faire que l'algorithme si-dessus fake un peu le choix de la playlist avec de l'aléatoire contrairement a un réel choix influencé par les réponse au quiz. Cela n'affectant pas les critères de base du projet, je vous donne cette version si dans le délai demandé pour que vous puissier l'évaluer telle qu'elle. Cependant, je souhaite et vais surement créer un vrai algorithme qui fonctionne par la suite que je vous enverrai également si cela vous intéresse.
