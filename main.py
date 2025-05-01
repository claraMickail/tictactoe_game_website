# Tic Tac Toe game in Python:
#
# The game should be a 3x3 grid where two players ('X' and 'O') take turns.
# After each move, check if a player has won by filling a row, column, or diagonal.
#
# Requirements:
# - Print the board after every move.
# - Ask the current player for their move (board position number).
# - Prevent players from choosing an occupied spot.
# - End the game when someone wins or the board is full.
#
# Example:
# Initial board:
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9
#
# Player X chooses position 5:
# 1 | 2 | 3
# 4 | X | 6
# 7 | 8 | 9
#
# Player O chooses position 1:
# O | 2 | 3
# 4 | X | 6
# 7 | 8 | 9
#
# ... and so on until either a player wins or the board is full.
#
# Bonus Challenges:
# DONE: - Add input validation (make sure players can't enter invalid positions). 
# DONE: - Allow players to play again without restarting the script.
# DONE: - Add a simple AI to play against
# DONE: Ask player if they want to be X or O first
# - If player wins, they start as X, otherwise they are O in the following round
# (if they choose to continue playing)

import random

class TicTacToe:
    board = [str(i) for i in range(1, 10)]  # ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x_moves = []
    o_moves = []
    comp_wins = 0
    player_wins = 0
    player = ''

    @staticmethod
    def position_selector():
        name = input("Enter your name: ")
        print(f"Hi {name}! Ready to play a great game of tictactoe?!")
        print("Well I hope you are!")
        print("I'll give you the first choice!")

        TicTacToe.player = ""
        while TicTacToe.player != "x" and TicTacToe.player != "o":
            choice = input("Would you rather start as X or O? Remeber, X always goes first (X/O): ")
            TicTacToe.player = choice.strip().lower()

        # if player == 'x':
        #     computer = 'o'    
        # else:
        #     computer = 'x'
        # return

    def run_game():
        TicTacToe.position_selector()

        # if TicTacToe.player == 'x':
        #     TicTacToe.myGameX()
        # else:
        #     TicTacToe.myGameO()

    @staticmethod
    def reset_game():
        TicTacToe.board = [str(i) for i in range(1, 10)]
        TicTacToe.x_moves = []
        TicTacToe.o_moves = []
    
    @staticmethod
    def exit_game():
        print ("\n Game ended! Thanks for playing")
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

            TicTacToe.print_board()
            move = input("Enter the position you want to play (as X): ")

            try:
                move = int(move)
            except ValueError:
                print ("invalid input type. input must be an integer between 1 and 9. try again")
                continue

            if move < 10 and move > 0 and move not in x_moves and move not in o_moves:
                b[move - 1] = 'X'
                print ("Your move: \n")
                TicTacToe.print_board()
                x_moves.append(move)
            else: 
                print("invalid input. your move has to be between 1 and 9 and must not be already filled")
                print("try again")
                continue

            winning_combinations = [
                [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
                [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
                [1, 5, 9], [3, 5, 7]              # diagonals
            ]

            x_wins = any(all(pos in x_moves for pos in combo)for combo in winning_combinations)

            if x_wins:
                print ("Congratulations! You won! \n")
                TicTacToe.player_wins += 1
                return 
            
            if (len(x_moves) + len(o_moves)) >= 9:
                break

            else:
                block = []
                for combo in winning_combinations:
                    pos_filled = [pos for pos in combo if pos in x_moves]
                    pos_not_filled = [pos for pos in combo if pos not in x_moves and pos not in o_moves]

                    if len(pos_filled) == 2 and len(pos_not_filled) == 1:
                        block.append(pos_not_filled[0])

                if block:
                    for num in block:
                        if num not in x_moves and num not in o_moves:
                            number = num
                            break
                else:
                    number = random.randint(1, 9)
                    while number in x_moves or number in o_moves:
                        number = random.randint(1, 9)

                b[number - 1] = 'O'
                o_moves.append(number)

            o_wins = any(all(pos in o_moves for pos in combo)for combo in winning_combinations)
            if o_wins:
                print("HAHA gotcha: \n")
                TicTacToe.print_board()
                print ("Hehe you loser")
                TicTacToe.comp_wins += 1
                return

        if not x_wins and not o_wins:
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
                print("board after my first move: ")
            else:
                print("Board after my move: ")
                TicTacToe.print_board()

            TicTacToe.print_board()

            move = input("Enter the position you want to play (as O): ")
            try:
                move = int(move)
            except ValueError:
                print ("invalid input type. input must be an integer between 1 and 9. try again")
                continue
            if move < 10 and move > 0 and move not in x_moves and move not in o_moves:
                b[move - 1] = 'O'
                print ("Your move: \n")
                TicTacToe.print_board()
                o_moves.append(move)
            else: 
                print("invalid input. your move has to be between 1 and 9 and must not be already filled")
                print("try again")
                continue

            winning_combinations = [
                [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
                [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
                [1, 5, 9], [3, 5, 7]              # diagonals
            ]

            o_wins = any(all(pos in o_moves for pos in combo)for combo in winning_combinations)

            if o_wins:
                print ("Congratulations! You won! \n")
                TicTacToe.player_wins += 1
                return 
            
            if (len(x_moves) + len(o_moves)) >= 9:
                break

            else:
                block = []
                for combo in winning_combinations:
                    pos_filled = [pos for pos in combo if pos in o_moves]
                    pos_not_filled = [pos for pos in combo if pos not in x_moves and pos not in o_moves]

                    if len(pos_filled) == 2 and len(pos_not_filled) == 1:
                        block.append(pos_not_filled[0])

                if block:
                    for num in block:
                        if num not in x_moves and num not in o_moves:
                            number = num
                            break
                else:
                    number = random.randint(1, 9)
                    while number in x_moves or number in o_moves:
                        number = random.randint(1, 9)

                b[number - 1] = 'X'
                x_moves.append(number)

            x_wins = any(all(pos in x_moves for pos in combo)for combo in winning_combinations)
            if x_wins:
                print("HAHA gotcha: \n")
                TicTacToe.print_board()
                print ("Hehe you loser")
                TicTacToe.comp_wins += 1
                return

        if not x_wins and not o_wins:
            print("No one won! Boo hoo")
            return



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

# STEP 3: Let the player choose their symbol (X or O)
# DONE: - At the start of the game, ask the player if they want to be 'X' or 'O'.
# - If the player chooses 'O', the computer should play first as 'X'.
# Otherwise, player starts

# STEP 4: Make the starting player dynamic based on win history
# - If the player wins, they start first (as X) in the next game.
# - If the computer wins, it starts first.

# STEP 5: Prepare for frontend integration (turn game into callable functions)
# - Refactor your class to separate logic into:
#     - `make_move(position, mark)` → updates the board
#     - `check_winner()` → returns winner or draw
#     - `get_board()` → returns current board state
#     - `reset_game()` → resets game state
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
