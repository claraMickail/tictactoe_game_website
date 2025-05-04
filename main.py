"""
Tic Tac Toe game in Python.

This script implements a two-player Tic Tac Toe game where a human player competes against a simple AI.
Key features include:
- A 3x3 board rendered in the terminal.
- User choice of playing as 'X' or 'O' (with 'X' going first).
- Input validation to prevent illegal or duplicate moves.
- Win condition checking after each move (rows, columns, diagonals).
- Simple AI that plays randomly or blocks winning moves.
- Option to replay the game after it ends.
- Tracks and displays the win count for both player and computer.
- Modular structure designed for integration with a frontend or API.
"""

import random

class TicTacToe:
    board = [str(i) for i in range(1, 10)]  # ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x_moves = []
    o_moves = []
    comp_wins = 0
    player_wins = 0
    player = ''
    
    winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]              # diagonals
        ]
    
    @staticmethod
    def get_board():
        return TicTacToe.board

    @staticmethod
    def position_selector():
        name = input("Enter your name: ")
        print(f"Hi {name}! Ready to play a great game of tictactoe?!")
        print("Well I hope you are!")
        print("I'll give you the first choice!")

        TicTacToe.player = ""
        while TicTacToe.player != "x" and TicTacToe.player != "o":
            choice = input("Would you rather start as X or O? Remember, X always goes first (X/O): ")
            TicTacToe.player = choice.strip().lower()

    def run_game():
        TicTacToe.position_selector()

    @staticmethod
    def reset_game():
        TicTacToe.board = [str(i) for i in range(1, 10)]
        TicTacToe.x_moves = []
        TicTacToe.o_moves = []
    
    @staticmethod
    def exit_game():
        print ("\nGame ended! Thanks for playing")
        print(f"I have won {TicTacToe.comp_wins} games while you have won {TicTacToe.player_wins} games")
    
    def play_again_check():        
        while True:
            answer = input("Do you want to play again: (Y/N) ")
            answer = answer.lower()
            if answer == "y" or answer == "yes":
                    TicTacToe.reset_game()
                    print("\nRestarting game...\n")
                    return True
            elif answer == "n" or answer == "no":
                TicTacToe.exit_game()
                return False
            else: 
                print("Sorry did not understand your response. try again \n")
        
    @staticmethod
    def print_board():
        b = TicTacToe.board
        print(f"{b[0]} | {b[1]} | {b[2]}")
        print(f"{b[3]} | {b[4]} | {b[5]}")
        print(f"{b[6]} | {b[7]} | {b[8]}")
        print()

    @staticmethod   
    def myGameX():
        x_moves = TicTacToe.x_moves
        o_moves = TicTacToe.o_moves
        
        while ((len(x_moves) + len(o_moves)) < 9):
            b = TicTacToe.board

            if len(x_moves) == 0 and len(o_moves) == 0:
                print("Starting board: \n")
            else:
                print("Board after my last move: ")

            TicTacToe.player_move("X")

            update = TicTacToe.playing_update('O', x_moves, o_moves)

            if update == 0:
                break
            elif update == 1:
                return

        TicTacToe.print_board()
        print("No one won! Boo hoo")
        return

    @staticmethod   
    def myGameO():
        x_moves = TicTacToe.x_moves
        o_moves = TicTacToe.o_moves
        
        while ((len(x_moves) + len(o_moves)) < 9):
            b = TicTacToe.board

            if len(x_moves) == 0 and len(o_moves) == 0:
                print("Starting board: \n")
                TicTacToe.print_board()
                move = random.randint(1,9)
                x_moves.append(move)
                b[move-1] = "X"
                print("Board after my first move: ")
            else:
                print("Board after my move: ")

            TicTacToe.player_move("O")
            update = TicTacToe.playing_update('X', o_moves, x_moves)

            if update == 0:
                break
            elif update == 1:
                return
            
        TicTacToe.print_board()
        print("No one won! Boo hoo")
        return

    @staticmethod
    def player_move(mark):
        while True:
            TicTacToe.print_board()
            move = input(f"Enter the position you want to play (as {mark}): ")

            try:
                move = int(move)
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            if 1 <= move <= 9:
                if TicTacToe.make_move(move, mark):
                    print("Your move:\n")
                    TicTacToe.print_board()
                    return move
                else:
                    print("Invalid move. That position is already taken.")
            else:
                print("Invalid move. Please choose a number from 1 to 9.")


    @staticmethod
    def playing_update(playing, playing_moves, opp_moves):
        b = TicTacToe.board
        player_wins = any(all(pos in playing_moves for pos in combo)for combo in TicTacToe.winning_combinations)

        if player_wins:
            print ("Congratulations! You won! \n")
            TicTacToe.player = 'x' #if won, restart next game as x
            TicTacToe.player_wins += 1
            return 1 # if return 1, its like we return. i.e return 1 if anyone wins
            
        if (len(opp_moves) + len(playing_moves)) >= 9:
            return 0    # if return 0, its like we break

        else:
            block = []
            for combo in TicTacToe.winning_combinations:
                pos_filled = [pos for pos in combo if pos in playing_moves]
                pos_not_filled = [pos for pos in combo if pos not in opp_moves and pos not in playing_moves]

                if len(pos_filled) == 2 and len(pos_not_filled) == 1:
                    block.append(pos_not_filled[0])

            if block:
                for num in block:
                    if num not in opp_moves and num not in playing_moves:
                        number = num
                        break
            else:
                number = random.randint(1, 9)
                while number in opp_moves or number in playing_moves:
                    number = random.randint(1, 9)

            b[number - 1] = playing.upper()
            opp_moves.append(number)

        opp_wins = any(all(pos in opp_moves for pos in combo)for combo in TicTacToe.winning_combinations)
        if opp_wins:
            print("HAHA gotcha: \n")
            TicTacToe.print_board()
            print ("Hehe you loser")
            TicTacToe.player = 'o' # if player lost, start next game as o
            TicTacToe.comp_wins += 1
            return 1
        
    def check_winner():
        x_wins = any(all(pos in TicTacToe.x_moves for pos in combo)for combo in TicTacToe.winning_combinations) 
        o_wins = any(all(pos in TicTacToe.o_moves for pos in combo)for combo in TicTacToe.winning_combinations)

        if x_wins:
            return 'X'
        if o_wins:
            return 'O'
        else:
            return None
        
    
    """Returns True if move was successful, False otherwise"""
    @staticmethod
    def make_move(position, mark):
        if TicTacToe.board[position - 1] in ['X', 'O']:
            return False

        TicTacToe.board[position - 1] = mark.upper()
        if mark.lower() == 'x':
            TicTacToe.x_moves.append(position)
        else:
            TicTacToe.o_moves.append(position)
        return True


# === Main Game Loop ===
TicTacToe.run_game()
while True:
    method_name = f"myGame{TicTacToe.player.upper()}"
    getattr(TicTacToe, method_name)()  # This calls TicTacToe.myGameX() or TicTacToe.myGameO()
    if not TicTacToe.play_again_check():
        break

# ==== FUTURE STEPS FOR THIS PROJECT ====

# DONE
# STEP 1: Create github project and push to it

# DONE
# STEP 2: Improve the AI logic
# - Currently, the AI (O) blocks the first combo with two X's and one empty spot.
# - Update this logic so that if this blockage spot is already filled, continue checking other combos.
#  (do this for all combos until a good blockage is found)
# - If good block is found, play it.
# - If none found (or all are already filled), fallback to a random valid move.

# DONE
# STEP 3: Let the player choose their symbol (X or O)
# DONE: - At the start of the game, ask the player if they want to be 'X' or 'O'.
# - If the player chooses 'O', the computer should play first as 'X'.
# Otherwise, player starts

# DONE
# STEP 4: Make the starting player dynamic based on win history
# - If the player wins, they start first (as X) in the next game.
# - If the computer wins, it starts first.

# DONE
# STEP 4.5: modularize better myGameX and myGameO

# DONE
# STEP 5: Prepare for frontend integration (turn game into callable functions)
# - Refactor your class to separate logic into:
#       Examples
#     - DONE: `make_move(position, mark)` → updates the board
#     - DONE: `check_winner()` → returns winner or draw
#     - DONE: `get_board()` → returns current board state
#     - DONE: `reset_game()` → resets game state
# - These functions will be useful for turning the game into an API backend later.

# STEP 6: Build a simple frontend with HTML + CSS + p5.js
# - Create an HTML canvas (with p5.js) that visually displays the board.
# - When a user clicks a cell, send their move to the backend using `fetch()`.
# - The backend returns the updated board and game status.
# - Redraw the board and update the game state in the browser.

# STEP 7: Connect Python backend (Flask) to the frontend
# - Build a Flask API with endpoints like:
#     - POST `/move` → accepts a move and returns updated board/status
#     - POST `/reset` → resets the game
#     - GET `/state` → returns the current board and whose turn it is
# - Serve `index.html` from Flask or run the frontend separately.

# STEP 8: Bonus polish
# - Add visuals: highlight winning lines
# - Add basic animations or delays between moves
# - Add sound or hover effects
# - Add a “Restart Game” button on the frontend

# ==== END OF FUTURE STEPS ====
