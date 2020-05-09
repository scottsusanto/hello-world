# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:51:19 2020

@author: gangh

Tic Tac Toe with Modes and AI
"""


# ----------- Global Variables ------------

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None

current_player = "X"


# For prediction of opponent's moves
def other_player():
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X"
    

# Keep track of the player's score
playerScore = 0


# Keep track of Chibi's score
chibiScore = 0


# Display the current state of the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("\n")
    return


# ----------------- Main -------------------
    

# Play Game
def play_game():
    global board
    global winner
    global current_player
    print("\n")
    print("Greetings traveller, and welcome to Scott's Tic Tac Toe")
    print("\n")
    mode = 0
    while mode != "1" and mode != "2":
        mode = input("Please input '1' for single player, '2' for multiplayer: ")
    if mode == "1":
        again = 'y'
        while again == 'y':
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
            winner = None
            current_player = "X"
            play_singleplayer_game()
            again = input("Would you like a rematch? 'y' to play again, any other key to quit ")
            if again == 'y':
                pass
            else:
                print("\n")
                print("Told you, Scott's AI is unbeatable... try again in your next life.")
                break
    elif mode == "2":
        again = 'y'
        while again == 'y':
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
            winner = None
            current_player = "X"
            play_multiplayer_game()
            again = input("Would you like to play again? 'y' to play again, any other key to quit ")
            if again == 'y':
                pass
            else:
                print("May we cross paths again traveller.")
                break
    return


# ----------------- Modes -------------------


# Play vs AI
def play_singleplayer_game():
    print("\n")
    print("You have selected single player!")
    print("\n")
    print("Scott's Tic Tac Toe AI, Chibi, is UNBEATABLE!")
    display_score()
    print("If you manage to score just 1 point, collect a $10 prize on Venmo from Scott!")
    print("\n")
    start = ""
    while start != 'y' and start != 'n':
        start = input("Would you like to start first? Press 'y' to start, 'n' for Chibi to start: ")
    print("\n")
    display_board()
    if start == 'y':
        startY()
    elif start == 'n':
        startN()
    return


# Player goes first
def startY():
    global playerScore
    global chibiScore
    while is_board_full() == False and winner == None:
        player_move()
        if check_for_win(board):
            print("Unbelievable... You actually beat Chibi! Collect your $10 from Master Scott.")
            playerScore += 1
            display_score()
            break
        elif check_for_tie():
            display_score()
            break
        comp_moves_second()
        if check_for_win(board):
            print("Sorry, but Chibi has won this round, and you have failed in life.")
            chibiScore += 1
            display_score()
            break
        elif check_for_tie():
            display_score()
            break


# Player goes second
def startN():
    global playerScore
    global chibiScore
    while is_board_full() == False and winner == None:
        comp_moves_first()
        if check_for_win(board):
            print("Sorry, but Chibi has won this round, and you have failed in life.")
            chibiScore += 1
            display_score()
            break
        elif check_for_tie():
            display_score()
            break
        player_move()
        if check_for_win(board):
            print("Unbelievable... You actually beat Chibi! Collect your $10 from Master Scott.")
            playerScore += 1
            display_score()
            break
        elif check_for_tie():
            display_score()
            break


# Computer moves first -- winning strategy
def comp_moves_first():
    print("Chibi's turn!")
    # Check for possible victories
    position = check_for_winloss(current_player)
    print(str(position) + " 1")
    if position == -1:
        # If no immediate victories, check for possible defeats
        position = check_for_winloss(other_player())
        print(str(position) + " 2")
        if position == -1:
            # If no immediate victories/defeats, dominate corners
            corners = [0, 2, 6, 8]
            position = corners[select_random()]
            while board[position] != "-":
                position = corners[select_random()]
            board[position] = current_player
    print("Chibi chose position " + str(position + 1) + ".")
    print("\n")
    display_board()
    flip_player()
    return


# Computer moves second -- defensive strategy
def comp_moves_second():
    print("Chibi's turn!")
    # Is center piece taken? If not, take the center
    if board[4] == "-":
        position = 4
        board[position] = current_player
    else:
        # Check for possible victories
        position = check_for_winloss(current_player)
        if position == -1:
            # If no immediate victories, check for possible defeats
            position = check_for_winloss(other_player())
            if position == -1:
                # If not immediate victories/defeats, dominate corners
                corners = [0, 2, 6, 8]
                position = corners[select_random()]
                while board[position] != "-":
                    position = corners[select_random()]
                board[position] = current_player
    print("Chibi chose position " + str(position + 1) + ".")
    print("\n")
    display_board()
    flip_player()
    return


# Check for possible victories/defeats
def check_for_winloss(player):
    global winner
    # ALl the possible moves in Tic Tac Toe
    allMoves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Iterating over every possibility
    for move in allMoves:
        # Make a copy of the board
        predictiveBoard = board[:]
        # If the position is empty, take that position
        if predictiveBoard[move] == "-":
            predictiveBoard[move] = player
            if check_for_win(predictiveBoard):
                board[move] = current_player
                winner = None
                return move
    return -1


# Play with friends
def play_multiplayer_game():
    print("\n")
    print("Multiplayer mode. May the best entity win.")
    print("\n")
    display_board()
    while is_board_full() == False and winner == None:
        player_move()
        if check_for_win(board):
            print("What a noob. " + winner + " has this round in the bag.")
            break
    if check_for_tie():
        pass
    return


# ----------------- Functions ------------------


# Check if board is full
def is_board_full():
    if "-" not in board:
        return True
    else:
        return False

        
# Player move
def player_move():
    print(current_player + "'s turn!")
    valid = False
    # An input will only be valid when...
    while not valid:
        try:
            # It is an integer...
            position = int(input("Please enter a position between 1 - 9: ")) - 1
        except (ValueError, TypeError):
            print("Invalid input.")
        else:
            # Between 1 - 9...
            if position >= 0 or position <= 8:
                # And has not yet been occupied on the board
                if board[position] == "-":
                    board[position] = current_player
                    valid = True
                else:
                    print("Sorry, this position is occupied.")
            else:
                print("This number is not between 1 - 9.")
    print("\n")
    display_board()
    flip_player()
    return    
    
    
# Flip player
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# Check for tie
def check_for_tie():
    # If board is full and there is still no winner, then the game ends in a tie
    if is_board_full() and winner == None:
        print("Tie Game!")
        return True
    else:
        return False


# Check for win
def check_for_win(board):
    if check_rows(board) or check_cols(board) or check_diags(board):
        return True
    else:
        return False


# Check to see if Rows are filled with same element
def check_rows(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True


# Check to see if Columns are filled with same element
def check_cols(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True


# Check to see if Rows are filled with same element
def check_diags(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True


# Display score
def display_score():
    print("The current score is " + str(playerScore) + " : " + str(chibiScore) + ".")
    return


# To pick a random position
def select_random():
    import random
    r = random.randint(0, 3)
    return r


# ------------ Execution --------------
# Play Game
        
play_game()









