let board = Array(9).fill("");
let currentPlayer = "X";

// setup():
// Runs once at the start.
// Used to define initial environment properties (like canvas size) and load resources.
function setup() {
  createCanvas(300, 300);    // i.e each slot is going to be 100 x 100 px
  textAlign(CENTER, CENTER);
  textSize(48);
}

// draw():
// Runs continuously in a loop (by default ~60 times per second).
// Used for animations, updating visuals, etc.
function draw() {
  background(255); // Clears the screen and paints it white every frame (white = 255)
  drawGrid();
  drawMoves();
}

function drawGrid() {
  for (let i = 1; i < 3; i++) {
    line(i * 100, 0, i * 100, 300);  
    line(0, i * 100, 300, i * 100);
  }
}

function drawMoves() {
  for (let i = 0; i < board.length; i++) {
    const x = (i % 3) * 100 + 50;
    const y = floor(i / 3) * 100 + 50;
    text(board[i], x, y);
  }
}

//Any event functions like mousePressed() are triggered on user interaction
function mousePressed() {
  const i = floor(mouseX / 100) + floor(mouseY / 100) * 3;
  if (board[i] === "") {
    board[i] = currentPlayer;
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
}


