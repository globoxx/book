

let random_number = Math.floor((Math.random()*100))+1
// document.getElementById("random_number").innerText = random_number;

let tentatives = 5;
let timer = 20;
let has_won = false;
let has_start = false;

function check(number,random_number) {
    has_start = true;
    let n = parseInt(number,10);
    if (Number.isInteger(Number(number))){
        let text = "";
        if (n == random_number) {
            text = "Vous avez gagné !"
            has_won = true
        }
        else if (n < random_number) {
            text = "Trop bas !!"
        }
        else if (n>random_number){
        text = "Trop haut"
        }
        decrease_tentatives()
        document.getElementById("user_number").value = ""
        document.getElementById("result").innerText = text;
        document.getElementById("tentatives").innerText = "Il vous reste " + tentatives + " tentatives"
    } else {
        alert("ECRIVEZ UN NOMBER ENTIER !!!!!!!!!!!!!")
        document.getElementById("user_number").value = ""
    }
    
}

function restart(){
    location.reload()
}

function decrease_tentatives(){
    tentatives -= 1;
}

setInterval(timer_advendment,1000)
function timer_advendment(){
    if (!has_won && has_start){
        timer -= 1;
    }
    document.getElementById("timer").innerText = "Il vous reste " + timer + " secondes"
    if ((timer <= 0 || tentatives <= 0) && !has_won){
        alert("Vous avez perdu, le nombre était "+random_number);
        restart();
    }
}

document.getElementById("user_number").addEventListener("keydown", event => {
    
    if (event.keyCode === 13){
        event.preventDefault()
        check(document.getElementById('user_number').value, random_number);

    }
});