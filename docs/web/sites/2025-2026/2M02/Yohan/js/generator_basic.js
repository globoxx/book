const form = document.getElementById("sudoku_form");

for (let i = 0; i < 81; i++) {
    const input = document.createElement("input");
    input.name = "cell" + i;
    input.className = "basic_sudoku_cell";
    input.type = "text";
    input.maxLength = 1;
    form.appendChild(input);
}
