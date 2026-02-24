const form = document.getElementById("big_sudoku_form");

for (let i = 0; i < 144; i++) {
    const input = document.createElement("input");
    input.name = "cell" + i;
    input.className = "big_sudoku_cell";
    input.type = "text";
    input.maxLength = 2;
    form.appendChild(input);
}
