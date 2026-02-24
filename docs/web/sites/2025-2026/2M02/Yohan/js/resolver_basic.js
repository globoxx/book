// checker if it is in same box
function same_box(a, b) {
  return Math.floor(a.row / 3) === Math.floor(b.row / 3) &&
         Math.floor(a.col / 3) === Math.floor(b.col / 3);
}

//  checks if placing candidate in cell would cause conflict
function has_conflict(candidate, cell, cells) {
  return cells.some(other =>
    other.value == candidate &&
    (
      other.row === cell.row ||
      other.col === cell.col ||
      same_box(cell, other)
    )
  );
}

// Update tags for all cells based on current placements
function update_tags(cells) {
  for (const cell of cells) {
    if (cell.value) {
      if (!Array.isArray(cell.tags) || cell.tags.length > 0) {
        cell.tags = [];
        update_cell_display(cell);
      }
      continue;
    }

    // If tags missing, initialize to 1..9
    if (!Array.isArray(cell.tags)) cell.tags = [1,2,3,4,5,6,7,8,9];

    // Remove any tag that conflicts with an already-placed value
    for (let n = 1; n <= 9; n++) {
      if (!cell.tags.includes(n)) continue; // don't recreate tags (I had problems with the previous version where tags were recreated and cause trouble)
      const conflict = cells.some(other =>
        other.value == n &&
        (
          other.row === cell.row ||
          other.col === cell.col ||
          same_box(cell, other)
        )
      );
      if (conflict) {
        const before = cell.tags.length;
        cell.tags = cell.tags.filter(t => t !== n);
        if (cell.tags.length !== before) update_cell_display(cell);
      }
    }
  }
}

//function that places a number if it is the only candidate in a cell
function lone_tag(cells) {
  let changed = false;

  for (const cell of cells) {
    if (!cell.value && Array.isArray(cell.tags) && cell.tags.length === 1) {
      const candidate = cell.tags[0];
      // safety check: don't place if it conflicts
      if (!has_conflict(candidate, cell, cells)) {
        cell.value = candidate;
        cell.tags = [];
        update_cell_display(cell);
        changed = true;
        console.log(`lone_tag: placed ${candidate} at (${cell.row},${cell.col})`);
      } else {
        console.warn(`lone_tag: found candidate ${candidate} at (${cell.row},${cell.col}) but conflict exists; skipping`);
      }
    }
  }

  return changed;
}

// function that places a number if it is the only candidate in a row
function lone_row(cells) {
  let changed = false;

  for (let row = 0; row < 9; row++) {
    const row_cells = cells.filter(c => c.row === row && !c.value);
    const tag_count = {};

    for (const cell of row_cells) {
      for (const tag of (cell.tags || [])) {
        tag_count[tag] = (tag_count[tag] || 0) + 1;
      }
    }

    for (const [tagStr, count] of Object.entries(tag_count)) {
      if (count === 1) {
        const tag = Number(tagStr);
        const target_cell = row_cells.find(c => c.tags && c.tags.includes(tag));
        if (target_cell && !has_conflict(tag, target_cell, cells)) {
          target_cell.value = tag;
          target_cell.tags = [];
          update_cell_display(target_cell);
          changed = true;
          console.log(`lone_row: placed ${tag} at (${target_cell.row},${target_cell.col})`);
        }
      }
    }
  }

  return changed;
}

// same for columns
function lone_column(cells) {
  let changed = false;

  for (let col = 0; col < 9; col++) {
    const col_cells = cells.filter(c => c.col === col && !c.value);
    const tag_count = {};

    for (const cell of col_cells) {
      for (const tag of (cell.tags || [])) {
        tag_count[tag] = (tag_count[tag] || 0) + 1;
      }
    }

    for (const [tagStr, count] of Object.entries(tag_count)) {
      if (count === 1) {
        const tag = Number(tagStr);
        const target_cell = col_cells.find(c => c.tags && c.tags.includes(tag));
        if (target_cell && !has_conflict(tag, target_cell, cells)) {
          target_cell.value = tag;
          target_cell.tags = [];
          update_cell_display(target_cell);
          changed = true;
          console.log(`lone_column: placed ${tag} at (${target_cell.row},${target_cell.col})`);
        }
      }
    }
  }

  return changed;
}

// same for boxes
function lone_box(cells) {
  let changed = false;

  for (let box_row = 0; box_row < 3; box_row++) {
    for (let box_col = 0; box_col < 3; box_col++) {
      const box_cells = cells.filter(c =>
        Math.floor(c.row / 3) === box_row &&
        Math.floor(c.col / 3) === box_col &&
        !c.value
      );

      const tag_count = {};
      for (const cell of box_cells) {
        for (const tag of (cell.tags || [])) {
          tag_count[tag] = (tag_count[tag] || 0) + 1;
        }
      }

      for (const [tagStr, count] of Object.entries(tag_count)) {
        if (count === 1) {
          const tag = Number(tagStr);
          const target_cell = box_cells.find(c => c.tags && c.tags.includes(tag));
          if (target_cell && !has_conflict(tag, target_cell, cells)) {
            target_cell.value = tag;
            target_cell.tags = [];
            update_cell_display(target_cell);
            changed = true;
            console.log(`lone_box: placed ${tag} at (${target_cell.row},${target_cell.col})`);
          }
        }
      }
    }
  }

  return changed;
}

// function that removes tags from rows/columns based on the alignment of tags within the box (also called pointing pairs, you can check the internet if you didnt understand)
function pointing_pair(cells) {
  let changed = false;

  for (let box_row = 0; box_row < 3; box_row++) {
    for (let box_col = 0; box_col < 3; box_col++) {
      for (let tag = 1; tag <= 9; tag++) {
        const positions = [];

        // collect candidates for this tag inside the box
        for (let r = box_row * 3; r < box_row * 3 + 3; r++) {
          for (let c = box_col * 3; c < box_col * 3 + 3; c++) {
            const cell = cells.find(cc => cc.row === r && cc.col === c);
            if (cell && !cell.value && cell.tags && cell.tags.includes(tag)) {
              positions.push(cell);
            }
          }
        }

        if (positions.length >= 2) {
          const same_row = positions.every(p => p.row === positions[0].row);
          const same_col = positions.every(p => p.col === positions[0].col);

          // If all positions in the box are in one row: remove tag from that row outside box
          if (same_row) {
            const target_row = positions[0].row;
            for (let col = 0; col < 9; col++) {
              // skip columns inside this box
              if (Math.floor(col / 3) === box_col) continue;

              const cell = cells.find(cc => cc.row === target_row && cc.col === col);
              if (cell && !cell.value && cell.tags && cell.tags.includes(tag)) {
                const before = cell.tags.length;
                cell.tags = cell.tags.filter(t => t !== tag);
                if (cell.tags.length !== before) {
                  update_cell_display(cell);
                  changed = true;
                  console.log(`pointing_pair: removed ${tag} from row ${target_row+1}, col ${col+1}`);
                }
              }
            }
          }

          // If all positions in the box are in one column: remove tag from that column outside box
          if (same_col) {
            const target_col = positions[0].col;
            for (let row = 0; row < 9; row++) {
              // skip rows inside this box
              if (Math.floor(row / 3) === box_row) continue;

              const cell = cells.find(cc => cc.row === row && cc.col === target_col);
              if (cell && !cell.value && cell.tags && cell.tags.includes(tag)) {
                const before = cell.tags.length;
                cell.tags = cell.tags.filter(t => t !== tag);
                if (cell.tags.length !== before) {
                  update_cell_display(cell);
                  changed = true;
                  console.log(`pointing_pair: removed ${tag} from row ${row+1}, col ${target_col+1}`);
                }
              }
            }
          }
        }
      }
    }
  }

  return changed;
}

// helper to compare arrays as it was previously settled
function arraysEqualAsSets(a, b) {
  if (!Array.isArray(a) || !Array.isArray(b)) return false;
  if (a.length !== b.length) return false;
  const sa = a.slice().sort((x, y) => x - y);
  const sb = b.slice().sort((x, y) => x - y);
  for (let i = 0; i < sa.length; i++) {
    if (sa[i] !== sb[i]) return false;
  }
  return true;
}

//function that gets rid of tags in a row if a pair exists in it (for exemple : 1238, 1245, 37, 37, 457 -> the pair is 3,7 so we remove 3 and 7 from other cells in the same row)
function naked_pairs_row(cells) {
  let changed = false;
  for (let row = 0; row < 9; row++) {
    const row_cells = cells.filter(c => c.row === row && !c.value);
    const pair_candidates = row_cells.filter(c => Array.isArray(c.tags) && c.tags.length === 2);
    for (let i = 0; i < pair_candidates.length; i++) {
      for (let j = i + 1; j < pair_candidates.length; j++) {
        const cell_A = pair_candidates[i];
        const cell_B = pair_candidates[j];
        if (arraysEqualAsSets(cell_A.tags, cell_B.tags)) {
          const pair_tags = cell_A.tags.slice();
          for (const other of row_cells) {
            if (other === cell_A || other === cell_B) continue;
            const before = other.tags.length;
            other.tags = other.tags.filter(t => !pair_tags.includes(t));
            if (other.tags.length !== before) {
              update_cell_display(other);
              changed = true;
              console.log(`naked_pairs: removed ${pair_tags} from row ${row+1}, col ${other.col+1}`);
            }
          }
        }
      }
    }
  }
  return changed;
}

//same for columns
function naked_pairs_column(cells) {
  let changed = false;
  for (let col = 0; col < 9; col++) {
    const col_cells = cells.filter(c => c.col === col && !c.value);
    const pair_candidates = col_cells.filter(c => Array.isArray(c.tags) && c.tags.length === 2);
    for (let i = 0; i < pair_candidates.length; i++) {
      for (let j = i + 1; j < pair_candidates.length; j++) {
        const cell_A = pair_candidates[i];
        const cell_B = pair_candidates[j];
        if (arraysEqualAsSets(cell_A.tags, cell_B.tags)) {
          const pair_tags = cell_A.tags.slice();
          for (const other of col_cells) {
            if (other === cell_A || other === cell_B) continue;
            const before = other.tags.length;
            other.tags = other.tags.filter(t => !pair_tags.includes(t));
            if (other.tags.length !== before) {
              update_cell_display(other);
              changed = true;
              console.log(`naked_pairs: removed ${pair_tags} from column ${col+1}, row ${other.row+1}`);
            }
          }
        }
      }
    }
  }
  return changed;
}

//same for boxes
function naked_pairs_box(cells) {
  let changed = false;
  for (let box_row = 0; box_row < 3; box_row++) {
    for (let box_col = 0; box_col < 3; box_col++) {
      const box_cells = cells.filter(c => 
        Math.floor(c.row / 3) === box_row &&
        Math.floor(c.col / 3) === box_col &&
        !c.value
      );
      const pair_candidates = box_cells.filter(c => Array.isArray(c.tags) && c.tags.length === 2);
      for (let i = 0; i < pair_candidates.length; i++) {
        for (let j = i + 1; j < pair_candidates.length; j++) {
          const cell_A = pair_candidates[i];
          const cell_B = pair_candidates[j];
          if (arraysEqualAsSets(cell_A.tags, cell_B.tags)) {
            const pair_tags = cell_A.tags.slice();
            for (const other of box_cells) {
              if (other === cell_A || other === cell_B) continue;
              const before = other.tags.length;
              other.tags = other.tags.filter(t => !pair_tags.includes(t));
              if (other.tags.length !== before) {
                update_cell_display(other);
                changed = true;
                console.log(`naked_pairs: removed ${pair_tags} from box ${box_row+1}, ${box_col+1}, row ${other.row+1}, col ${other.col+1}`);
              }
            }
          }
        }
      }
    }
  }
  return changed;
}
// finds hidden pairs in tags (for exemple : in the same row we have a cell with 3,5,7 for tags and another one with 3,4,7,9 (but no other cells have 3 AND 7 in their tags) so we say the hidden pair is 3,7 and we remove all other tags in the cell except   those 2)
function hidden_pairs_row(cells) {
  let changed = false;
  for (let row = 0; row < 9; row++) {
    const digit_positions = {};
    for (let digit = 1; digit <= 9; digit++) {
      digit_positions[digit] = cells.filter(c => !c.value && c.row === row && c.tags.includes(digit));
      console.log("tag includes digit found")
    }
    for (let a = 1; a <= 9; a++) {
      const posA = digit_positions[a]
      for (let b = 1; b <= 9; b++){
        const posB = digit_positions[b]
        if (posA.length === 2 && posB.length === 2 && posA[0] === posB[0] && posA[1] === posB[1]) {
          const cell_pairs = posA;
          for (const cell of cell_pairs) {
            const before = cell.tags.length;
            cell.tags = cell.tags.filter(t => t === a || t === b)
            if (cell.tags.length !== before) {
              update_cell_display(cell);
              console.log("Hidden pair", a, b, "applied to cell", cell);
              changed = true
            }
          }
        }
        else{
          continue;
        }
      }
    }
  }
  return changed;
}
// same for columns
function hidden_pairs_col(cells) {
  let changed = false;
  for (let col = 0; col < 9; col++) {
    const digit_positions = {};
    for (let digit = 1; digit <= 9; digit++) {
      digit_positions[digit] = cells.filter(c => !c.value && c.col === col && c.tags.includes(digit));
      console.log("tag includes digit found")
    }
    for (let a = 1; a <= 9; a++) {
      const posA = digit_positions[a]
      for (let b = 1; b <= 9; b++){
        const posB = digit_positions[b]
        if (posA.length === 2 && posB.length === 2 && posA[0] === posB[0] && posA[1] === posB[1]) {
          const cell_pairs = posA;
          for (const cell of cell_pairs) {
            const before = cell.tags.length;
            cell.tags = cell.tags.filter(t => t === a || t === b)
            if (cell.tags.length !== before) {
              update_cell_display(cell);
              console.log("Hidden pair", a, b, "applied to cell", cell);
              changed = true
            }
          }
        }
        else {
          continue;
        }
      }
    }
  }
  return changed;
}

// same for boxes
function hidden_pairs_box(cells) {
  let changed = false;
  for (let box_row = 0; box_row < 3; box_row++) {
    for (let box_col = 0; box_col < 3; box_col++) {
      const digit_positions = {};
      for (let digit = 1; digit <= 9; digit++) {
        digit_positions[digit] = cells.filter(c => !c.value && Math.floor(c.row / 3) === box_row && Math.floor(c.col / 3) === box_col && c.tags.includes(digit));
        console.log("tag includes digit found")
      }
      for (let a = 1; a <= 9; a++) {
        const posA = digit_positions[a]
        for (let b = 1; b <= 9; b++){
          const posB = digit_positions[b]
          if (posA.length === 2 && posB.length === 2 && posA[0] === posB[0] && posA[1] === posB[1]) {
            const cell_pairs = posA;
            for (const cell of cell_pairs) {
              const before = cell.tags.length;
              cell.tags = cell.tags.filter(t => t === a || t === b)
              if (cell.tags.length !== before) {
                update_cell_display(cell);
                console.log("Hidden pair", a, b, "applied to cell", cell);
                changed = true
              }
            }
          }
          else{
            continue;
          }
        }
      }
    }
    return changed;
  }
}
// Main solver loop
function solve(cells) {
  // Ensure initial tags exist for empty cells
  for (const cell of cells) {
    if (!cell.value && !Array.isArray(cell.tags)) cell.tags = [1,2,3,4,5,6,7,8,9];
  }


  update_tags(cells);

  let progress = true;
  while (progress) {
    progress = false;

    if (lone_tag(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (lone_row(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (lone_column(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (lone_box(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    // I commented out hidden pairs for now because it seems to cause issues but I didn't want to delete it entirely, so you can still see my work
    /*if (hidden_pairs_row(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (hidden_pairs_col(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (hidden_pairs_box(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }*/
    if (naked_pairs_row(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (naked_pairs_column(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (naked_pairs_box(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
    if (pointing_pair(cells)) {
      progress = true;
      update_tags(cells);
      continue;
    }
  }
}

// function that updates the display (what you see) of a single cell based on its value and tags
function update_cell_display(cell) {
  const el = get_cell_by_index(cell.row * 9 + cell.col);
  if (!el) return;
  if (cell.value) {
    el.value = cell.value;
    el.classList.add("filled");
    el.placeholder = "";
  } else {
    el.value = "";
    el.placeholder = cell.tags ? cell.tags.join("") : "";
    el.classList.remove("filled");
  }
}

// function to check for duplicates (doppelgangers) in rows
function check_line(row_number, cells) {
  const seen = new Set();
  for (let col = 0; col < 9; col++) {
    const cell = cells.find(c => c.row === row_number && c.col === col);
    const value = cell?.value;
    if (value === "" || value == null) continue;
    if (seen.has(value)) {
      console.warn(`Doppelganger found in line ${row_number + 1} : ${value}`);
      alert("Doppelganger found in line " + (row_number + 1));
      return true;
    }
    seen.add(value);
  }
  return false; 
}

// same for columns
function check_column(col_number, cells) {
  const seen = new Set();
  for (let row = 0; row < 9; row++) {
    const cell = cells.find(c => c.col === col_number && c.row === row);
    const value = cell?.value;
    if (value === "" || value == null) continue;
    if (seen.has(value)) {
      console.warn(`Doppelganger found in column ${col_number + 1} : ${value}`);
      alert("Doppelganger found in column " + (col_number + 1));
      return true;
    }
    seen.add(value);
  }
  return false;
}

// same for boxes
function check_box(box_row, box_col, cells) {
  const seen = new Set();
  for (let row = box_row * 3; row < box_row * 3 + 3; row++) {
    for (let col = box_col * 3; col < box_col * 3 + 3; col++) {
      const cell = cells.find(c => c.row === row && c.col === col);
      const value = cell?.value;
      if (value === "" || value == null) continue;
      if (seen.has(value)) {
        console.warn(
          `Doppelganger found in box (${box_row + 1}, ${box_col + 1}) : ${value}`
        );
        alert(
          "Doppelganger found in box (" +
          (box_row + 1) + ", " + (box_col + 1) + ")"
        );
        return true;
      }
      seen.add(value);
    }
  }
  return false;
}

// function that checks if a value is valid (between 1 and 9 or empty)
function is_valid_value(value, maxDigit = 9) {
  if (value === "" || value == null) return true;

  const n = Number(value);
  return Number.isInteger(n) && n >= 1 && n <= maxDigit;
}

// function that calls all 3 checkers to check all of the cells in the grid
function check_all(cells) {
  for (const cell of cells) {
    if (!is_valid_value(cell.value, 9)) {
      console.warn(`Invalid value found at (${cell.row + 1}, ${cell.col + 1}): ${cell.value}`);
      alert("Invalid value found at (" + (cell.row + 1) + ", " + (cell.col + 1) + "): " + cell.value);
      return true;
    }
  }
  for (let y = 0; y < 9; y++) {
    if (check_column(y, cells)) return true;
    if (check_line(y, cells)) return true;
  }
  for (let box_row = 0; box_row < 3; box_row++) {
    for (let box_col = 0; box_col < 3; box_col++) {
      if (check_box(box_row, box_col, cells)) return true;
    }
    }
  return false;
}


function get_cell_by_index(index) {
  return document.getElementById(`cell${index}`) || document.querySelector(`[name="cell${index}"]`);
}

// when clicking "Resolve"
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
          value: value ? value : "",
          tags: value ? [] : [1,2,3,4,5,6,7,8,9]
        });
      }
    }

    // detect existing impossibilities first
    if (check_all(cells)) {
      alert("Impossibilties found in initial grid, process stopped");
      return;
    }

    // run solver only if no impossibilities
    solve(cells);

    // final check after solving
    check_all(cells);
  });
}

