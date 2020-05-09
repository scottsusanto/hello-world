# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:31:48 2020

@author: gangh
"""

# Play Game
def play_game():
    global board
    global winner
    global current_player
    again = ""
    while again != 'n':
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        winner = None
        current_player = "X"
        print("\n")
        print("Welcome to scott's Tic Tac Toe")
        print("\n")
        mode = 0
        while mode != "1" and mode != "2":
            mode = input("Please input '1' for single player, '2' for multiplayer: ")
        if mode == "1":
            play_singleplayer_game()
        elif mode == "2":
            play_multiplayer_game()
        again = input("Would you like a rematch? 'y' to play again, any other key to quit ")
        if again == 'y':
            pass
        else:
            print("Told you, Scott's AI is unbeatable... see you next time!")
            break   
    return