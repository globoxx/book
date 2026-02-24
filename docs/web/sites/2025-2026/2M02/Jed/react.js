
let circles_alights = 5;
let has_started = false;
let all_is_turned_off = false;
let start_time = false;
let has_stopped = false;
let has_reacted = false;
//let has_failed = false;
let time = 0;

if (localStorage.getItem("bestTime") !== null){
    document.getElementById("bestTime").innerText = "Le meilleur score est " + Number(localStorage.getItem("bestTime")).toFixed(3)
}


function clicked(){
    if (has_started){
        if (has_reacted){
            restart()
        } else if(start_time){
            has_reacted = true;
        }
        else{
            alert("Le jeu n'a pas encore commencé, vous avez perdu !")
            restart()
        }
        
    } else{ 
        has_started = true;
    }
    
}

setInterval(turn_off,1500);

function turn_off(){
    if (circles_alights >= 1 && has_started){
        document.getElementById("circle"+circles_alights).style.backgroundColor = 'green';
        circles_alights -= 1;
        if (circles_alights == 0){
            all_is_turned_off = true;
        }
    }
}



setInterval(start, Math.random()*2000+4000);

function start(){
    if (all_is_turned_off == true && !start_time){
        //all_is_turned_off = false;
        start_time = true;
        const circles = document.getElementsByClassName("circles");
        for (let i = 0; i < circles.length ;i++){
            circles[i].style.backgroundColor = "grey";
        }
    }
}

setInterval(Time,1)

function Time(){
    if (start_time && !has_reacted){
        time = time + 0.004;
        document.getElementById("time").innerText = time.toFixed(3) + " secondes";
    } 
        else if (has_reacted && start_time) {
        let bestTime = localStorage.getItem("bestTime")
        if (bestTime !== null ){
            if (bestTime < time){
                return
            }
        }
        localStorage.setItem("bestTime",time)
        document.getElementById("bestTime").innerText = "Le meilleur score est " + time.toFixed(3)
        alert("Bravo, vous avez battu votre record !")
        start_time = false
    }
}

function restart(){
    location.reload()
}

document.addEventListener("keydown", event => {

    if (event.keyCode == 32){
        event.preventDefault()
        clicked()
    } else if (event.keyCode == 82){
        event.preventDefault()
        restart()
    }

})