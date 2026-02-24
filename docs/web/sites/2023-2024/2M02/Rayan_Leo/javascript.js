var nouveauparagraphe = document.createElement("p");
nouveauparagraphe.id = "texte de fin du jeu";
nouveauparagraphe.className = "texte-fin-de-jeu"

function clicked1() {
  if (x % 2 == 0 && a == 0) {
    document.getElementById("case 1").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    a += 1;
    result();

  }
  else if (x % 2 == 1 && a == 0) {
    document.getElementById("case 1").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    a += 2;
    result();

  }
}
function clicked2() {
  if (x % 2 == 0 && b == 0) {

    document.getElementById("case 2").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    b = 1;
    result();

  }
  else if (x % 2 == 1 && b == 0) {

    document.getElementById("case 2").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    b = 2;
    result();

  }
}
function clicked3() {
  if (x % 2 == 0 && c == 0) {
    document.getElementById("case 3").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    c = 1;
    result();

  }
  else if (x % 2 == 1 && c == 0) {

    document.getElementById("case 3").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    c = 2;
    result();

  }
}
function clicked4() {
  if (x % 2 == 0 && d == 0) {
    document.getElementById("case 4").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    d = 1;
    result();

  }
  else if (x % 2 == 1 && d == 0) {

    document.getElementById("case 4").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    d = 2;
    result();

  }
}
function clicked5() {
  if (x % 2 == 0 && e == 0) {
    document.getElementById("case 5").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    e = 1;
    result();

  }
  else if (x % 2 == 1 && e == 0) {

    document.getElementById("case 5").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    e = 2;
    result();

  }

}
function clicked6() {
  if (x % 2 == 0 && f == 0) {
    document.getElementById("case 6").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    f = 1;
    result();

  }
  else if (x % 2 == 1 && f == 0) {

    document.getElementById("case 6").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    f = 2;
    result();

  }
}
function clicked7() {
  if (x % 2 == 0 && g == 0) {

    document.getElementById("case 7").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    g = 1;
    result();

  }
  else if (x % 2 == 1 && g == 0) {

    document.getElementById("case 7").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    g = 2;
    result();

  }

}
function clicked8() {
  if (x % 2 == 0 && h == 0) {

    document.getElementById("case 8").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    h = 1;
    result();

  }
  else if (x % 2 == 1 && h == 0) {

    document.getElementById("case 8").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    h = 2;
    result();

  }
}
function clicked9() {
  if (x % 2 == 0 && i == 0) {

    document.getElementById("case 9").innerHTML = ' <img src="photos/Capture decran 2023-09-21 a 11.40.38.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    i = 1;
    result();

  }
  else if (x % 2 == 1 && i == 0) {

    document.getElementById("case 9").innerHTML = '<img src="photos/Capture decran 2023-09-21 a 11.40.16.png"style="border: 1px solid" alt="case rond"width="350" height="350">';
    x += 1;
    i = 2;
    result();

  }
}
function result() {
  if (e == 1 && y == 0) {
    if (a == 1 && i == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (b == 1 && h == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (c == 1 && g == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;
    }

    else if (d == 1 && f == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;
    }


  }
  if (a == 1 && y == 0) {
    if (b == 1 && c == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;
    }
    else if (d == 1 && g == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
  }
  if (i == 1 && y == 0) {
    if (f == 1 && c == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (h == 1 && g == 1) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
  }

  if (e == 2 && y == 0) {
    if (a == 2 && (i == 2)) {
      var texte = document.createTextNode("Le joueur 2 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;
    }
    else if (b == 2 && h == 2) {
      var texte = document.createTextNode("Le joueur 2 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (c == 2 && g == 2) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;
    }
    else if (d == 2 && f == 2) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
  }
  if (a == 2 && y == 0) {
    if (b == 2 && c == 2) {
      var texte = document.createTextNode("Le joueur 2 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (d == 2 && g == 2) {
      var texte = document.createTextNode("Le joueur 2 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
  }
  if (i == 2 && y == 0) {
    if (f == 2 && c == 2) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
    else if (h == 2 && g == 2) {
      var texte = document.createTextNode("Le joueur 1 a gagné");
      nouveauparagraphe.appendChild(texte);
      document.body.appendChild(nouveauparagraphe);
      y = 1;

    }
  }
  if (a > 0 && b > 0 && c > 0 && d > 0 && e > 0 && f > 0 && g > 0 && h > 0 && i > 0 && y == 0) {
    var texte = document.createTextNode("Le match est nul");
    nouveauparagraphe.appendChild(texte);
    document.body.appendChild(nouveauparagraphe);
  }
}