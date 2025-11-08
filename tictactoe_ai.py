# Task 2 - Tic Tac Toe AI
# Created by Shabab Ahmad for CODSOFT Internship

import random

board = [' ' for _ in range(9)]  # 3x3 Tic Tac Toe board

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_winner(brd, player):
    win_cond = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    return any(all(brd[pos] == player for pos in combo) for combo in win_cond)

def is_full(brd):
    return ' ' not in brd

def player_move():
    while True:
        move = input("Choose your position (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        else:
            print("Please enter a number between 1-9.")

def ai_move():
    empty_positions = [i for i in range(9) if board[i] == ' ']
    # Simple AI logic: block or win
    for player in ['O', 'X']:
        for pos in empty_positions:
            board_copy = board.copy()
            board_copy[pos] = player
            if check_winner(board_copy, player):
                board[pos] = 'O'
                return
    # Otherwise random move
    move = random.choice(empty_positions)
    board[move] = 'O'

# Game loop
print("🎮 Welcome to Tic Tac Toe (AI Version)!")
print("You are 'X' and the AI is 'O'.")
print_board()

while True:
    player_move()
    print_board()
    if check_winner(board, 'X'):
        print("🎉 You win! Great job!")
        break
    if is_full(board):
        print("It's a draw!")
        break

    print("AI is thinking...")
    ai_move()
    print_board()

    if check_winner(board, 'O'):
        print("😈 AI wins! Better luck next time.")
        break
    if is_full(board):
        print("It's a draw!")
        break
