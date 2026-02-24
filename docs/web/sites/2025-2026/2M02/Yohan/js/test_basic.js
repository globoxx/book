// ==========================================
// BASIC SUDOKU RESOLVER (using your structure)
// ==========================================

function get_cell_by_index(index) {
  return document.getElementById(`cell${index}`)
      || document.querySelector(`[name="cell${index}"]`);
}
// Helper to check if two cells are in the same 3×3 box
function same_box(a, b) {
  return Math.floor(a.row / 3) === Math.floor(b.row / 3) &&
         Math.floor(a.col / 3) === Math.floor(b.col / 3);
}

// Updates possible tags
function update_tags(cells) {
  for (const cell of cells) {
    if (cell.value) continue; // Skip filled cells

    const possible = new Set([1,2,3,4,5,6,7,8,9]);

    for (const other of cells) {
      if (other.value) {
        if (
          other.row === cell.row ||
          other.col === cell.col ||
          same_box(cell, other)
        ) {
          possible.delete(parseInt(other.value));
        }
      }
    }

    cell.tags = Array.from(possible);
    update_cell_display(cell);
  }
}

// Fill cells that have exactly one possible tag
function lone_tag(cells) {
  let changed = false;

  for (const cell of cells) {
    if (!cell.value && cell.tags && cell.tags.length === 1) {
      cell.value = cell.tags[0];
      cell.tags = [];
      update_cell_display(cell);
      changed = true;
    }
  }

  return changed;
}

// Keep updating until no progress is made
function solve(cells) {
  let progress = true;
  while (progress) {
    update_tags(cells);
    progress = lone_tag(cells);
  }
}

// Update the visible grid based on the cell data
function update_cell_display(cell) {
  const el = get_cell_by_index(cell.row * 9 + cell.col);
  if (!el) return;

  if (cell.value) {
    el.value = cell.value;
    el.classList.add("filled");
  } else {
    el.placeholder = cell.tags ? cell.tags.join("") : "";
    el.classList.remove("filled");
  }
}

// ================================
// MAIN: when clicking "Resolve"
// ================================
const submitBtn = document.getElementById("submit_btn");
if (submitBtn) {
  submitBtn.addEventListener("click", function (e) {
    e.preventDefault();

    const cells = [];
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        const index = row * 9 + col;
        const el = get_cell_by_index(index);
        const value = el ? el.value : "";
        cells.push({
          row,
          col,
          value: value ? parseInt(value) : null,
          tags: value ? [] : [1,2,3,4,5,6,7,8,9]
        });
      }
    }

    solve(cells);
  });
}
