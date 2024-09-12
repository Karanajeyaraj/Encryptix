import tkinter as tk
from tkinter import messagebox

# Function to check for a win or draw
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Check for a draw
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Draw'
    
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner == 'X':  # AI wins
        return 1
    elif winner == 'O':  # Human wins
        return -1
    elif winner == 'Draw':
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function to make the best move for AI
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to handle human move
def on_click(row, col):
    global current_board, buttons
    
    if current_board[row][col] == ' ' and not game_over():
        buttons[row][col].config(text='O')
        current_board[row][col] = 'O'
        
        # Check if human wins
        if check_winner(current_board) == 'O':
            messagebox.showinfo("Game Over", "You win!")
            reset_board()
            return
        
        # AI's turn
        ai_move = best_move(current_board)
        if ai_move:
            buttons[ai_move[0]][ai_move[1]].config(text='X')
            current_board[ai_move[0]][ai_move[1]] = 'X'
        
        # Check if AI wins or draw
        winner = check_winner(current_board)
        if winner == 'X':
            messagebox.showinfo("Game Over", "AI wins!")
            reset_board()
        elif winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()

# Check if game is over
def game_over():
    winner = check_winner(current_board)
    if winner == 'X' or winner == 'O' or winner == 'Draw':
        return True
    return False

# Reset the board
def reset_board():
    global current_board, buttons
    current_board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='')

# Main game setup with Tkinter GUI
def tic_tac_toe_gui():
    global buttons, current_board
    root = tk.Tk()
    root.title("Tic-Tac-Toe AI")
    
    buttons = [[None for _ in range(3)] for _ in range(3)]
    current_board = [[' ' for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                               command=lambda row=i, col=j: on_click(row, col))
            button.grid(row=i, column=j)
            buttons[i][j] = button

    root.mainloop()

# Start the game
tic_tac_toe_gui()
