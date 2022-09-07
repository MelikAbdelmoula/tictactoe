from TicTacToe import *

#initial state
tableau = {"a3": " ", "b3": " ", "c3": " ",
           "a2": " ", "b2": " ", "c2": " ",
           "a1": " ", "b1": " ", "c1": " "}

moves = ["a3", "b3", "c3", "a2", "b2", "c2", "a1", "b1", "c1"]


def game(state):

    while not terminal(state):

        if player(state) == "X":
            action = input("Play ")
            while action not in actions(state):
                action = input("Your move is not valid: please try again : ")
        else:
            action = ia_move(state)

        state = result(state, action)
        print(plateau(state))

        if terminal(state):
            if utility(state) == 1:
                print("You won!")
            elif utility(state) == 0:
                print("It's a tie!")
            else:
                print("Artificial intelligence won!")
                            
        
game(tableau)

