import random
import os
os.system("cls")

def display_board(board):
    print("\n"*50)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("-"*9)
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("-"*9)
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    '''
    OUTPUT = PLAYER 1 AND PLAYER 2 MARKER!
    '''

    marker = ""
    while marker != "X" and marker != "O":
        marker = input("Player 1 Please pick a marker 'X' or 'O' :  ").upper()
    player1 = marker
    if player1 == "X":
        return ("X","O")
    else:
        return ("O","X")
       
def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[3] == board[5] == board[7] == mark) or (board[1] == board[5] == board[9] == mark)

def choose_first():
    return random.choice(["PLAYER1","PLAYER2"])

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position: (1-9): "))    
    return position

def replay():
    choice = input("PLAY AGAIN? (YES OR NO):  ")
    return choice == "yes"

print("Welcome to tic tac toe...")
while True:
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go FIRST!")

    play_game = input("Ready to play? y or n? ")
    if play_game.lower() == "y":
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == "PLAYER1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):               
                display_board(the_board)
                print("Player1 has won!!")
                game_on = False
            else:
                if full_board_check(the_board): 
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "PLAYER2"
        else:            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):                
                display_board(the_board)
                print("Player2 has won!!")
                game_on = False
            else:
                if full_board_check(the_board):                    
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = "PLAYER1"
    if not replay():
        break
