// Task 2 - Tic Tac Toe AI (Web Version)
// Created by Shabab Ahmad for CODSOFT Internship

const board = Array(9).fill(null);
const cells = [];
let currentPlayer = 'X';
let gameOver = false;

const winningCombinations = [
  [0,1,2],[3,4,5],[6,7,8],
  [0,3,6],[1,4,7],[2,5,8],
  [0,4,8],[2,4,6]
];

const boardDiv = document.getElementById('board');
const status = document.getElementById('status');

// Create game cells
for (let i = 0; i < 9; i++) {
  const cell = document.createElement('div');
  cell.classList.add('cell');
  cell.dataset.index = i;
  cell.addEventListener('click', handleClick);
  boardDiv.appendChild(cell);
  cells.push(cell);
}

function handleClick(e) {
  const index = e.target.dataset.index;

  if (board[index] || gameOver) return;

  board[index] = currentPlayer;
  e.target.textContent = currentPlayer;

  if (checkWinner(currentPlayer)) {
    status.textContent = `🎉 You win!`;
    gameOver = true;
    return;
  }

  if (board.every(cell => cell)) {
    status.textContent = "It's a draw!";
    gameOver = true;
    return;
  }

  currentPlayer = 'O';
  status.textContent = "AI is thinking...";
  setTimeout(aiMove, 600);
}

function aiMove() {
  const emptyCells = board.map((v, i) => v ? null : i).filter(v => v !== null);

  // Simple AI: check for winning or blocking moves
  for (let player of ['O', 'X']) {
    for (let i of emptyCells) {
      const copy = [...board];
      copy[i] = player;
      if (checkWinner(player, copy)) {
        makeMove(i);
        return;
      }
    }
  }

  // Otherwise random move
  const move = emptyCells[Math.floor(Math.random() * emptyCells.length)];
  makeMove(move);
}

function makeMove(index) {
  board[index] = 'O';
  cells[index].textContent = 'O';

  if (checkWinner('O')) {
    status.textContent = "😈 AI wins! Better luck next time.";
    gameOver = true;
  } else if (board.every(cell => cell)) {
    status.textContent = "It's a draw!";
    gameOver = true;
  } else {
    currentPlayer = 'X';
    status.textContent = "Your turn!";
  }
}

function checkWinner(player, customBoard = board) {
  return winningCombinations.some(combo =>
    combo.every(i => customBoard[i] === player)
  );
}

function restartGame() {
  for (let i = 0; i < 9; i++) {
    board[i] = null;
    cells[i].textContent = '';
  }
  currentPlayer = 'X';
  gameOver = false;
  status.textContent = "Your turn! You are X.";
}
