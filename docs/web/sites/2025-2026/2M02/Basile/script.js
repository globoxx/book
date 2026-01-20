const board = document.getElementById("board");

let currentPalyer = "X";

function switchPlayer() {
    if(currentPalyer ==="X"){
        currentPalyer = "O";
    }
    else if(currentPalyer ==="O") {
        currentPalyer = "X";
    }
}

function handleClick(event) {
    const cell = event.target;

    if(!cell.classList.contains("cell")) return;
    cell.textContent = currentPalyer;
    switchPlayer();
}
board.addEventListener("click",handleClick);


