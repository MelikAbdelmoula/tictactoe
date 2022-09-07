import copy


def terminal(state): #checks if state s is a terminal state
    end = True
    
    #vertical check
    if state["a1"] == state["a2"] == state["a3"] != " ":
        return 1
    if state["b1"] == state["b2"] == state["b3"] != " ":
        return 1
    if state["c1"] == state["c2"] == state["c3"] != " ":
        return 1

    #horizontal check
    if state["a1"] == state["b1"] == state["c1"] != " ":
        return 1
    if state["a2"] == state["b2"] == state["c2"] != " ":
        return 1
    if state["a3"] == state["b3"] == state["c3"] != " ":
        return 1
    
    #diagonal check
    if state["a1"] == state["b2"] == state["c3"] != " ":
        return 1
    if state["a3"] == state["b2"] == state["c1"] != " ":
        return 1


    #if no victory:
    for e in state: 
        if state[e] == " ":
            end = False 

    return end

def actions(s): #returns legal moves in state s
    legal_moves = ["a3", "b3", "c3", "a2", "b2", "c2", "a1", "b1", "c1"]
    for e in s:
        if s[e] != " ":
            legal_moves.remove(e)
        
    if legal_moves == []:
        return None
    return legal_moves

def player(s): #Tells which player's turn it is
    current_player = ""
    count = 1

    for e in s:
        if s[e] != " ":
            count += 1
    
    if count == 1:
        current_player = "X"
        
    if count > 0:
        if count%2 == 0:
            current_player = "O"
        else:
            current_player = "X"
        
    return current_player


def result(s,a): #returns state after action a taken in state s
    current_player = player(s)

    if terminal(s):
        return s
    state = copy.deepcopy(s)
    state[a] = current_player

    return state



def utility(state):
    current_player = player(state)

    if current_player == "X":
        if not state["a1"] == state["a2"] == state["a3"] != " " \
        and not state["b1"] == state["b2"] == state["b3"] != " " \
        and not state["c1"] == state["c2"] == state["c3"] != " " \
        and not state["a1"] == state["b1"] == state["c1"] != " " \
        and not state["a2"] == state["b2"] == state["c2"] != " " \
        and not state["a3"] == state["b3"] == state["c3"] != " " \
        and not state["a1"] == state["b2"] == state["c3"] != " " \
        and not state["a3"] == state["b2"] == state["c1"] != " " :
            terminal_value = 0
            return terminal_value
        terminal_value = -1
        return terminal_value
        
    elif current_player == "O":
        if not state["a1"] == state["a2"] == state["a3"] != " " \
        and not state["b1"] == state["b2"] == state["b3"] != " " \
        and not state["c1"] == state["c2"] == state["c3"] != " " \
        and not state["a1"] == state["b1"] == state["c1"] != " " \
        and not state["a2"] == state["b2"] == state["c2"] != " " \
        and not state["a3"] == state["b3"] == state["c3"] != " " \
        and not state["a1"] == state["b2"] == state["c3"] != " " \
        and not state["a3"] == state["b2"] == state["c1"] != " " :
            terminal_value = 0
            return terminal_value
        terminal_value = 1
        return terminal_value

    if not terminal(state):
        terminal_value = 0

    return terminal_value



#Display the game
def plateau(tableau):
    
    row1 = ["(3) ",tableau["a3"], "|",tableau["b3"], "|", tableau["c3"]]
    for e in row1:
        print(e, end=" ")
    print()
    print("     ----------")
    row2 = ["(2) ", tableau["a2"], "|",tableau["b2"], "|", tableau["c2"]]
    for e in row2:
        print(e, end=" ")
    print()
    print("     ----------")
    row3 = ["(1) ", tableau["a1"], "|",tableau["b1"], "|", tableau["c1"]]
    for e in row3 :
        print(e, end=" ")

    print()
    print("   ","(a)", "(b)", "(c)")



#Minimax
def max_value(state):
    if terminal(state):
        return utility(state)
    v = -2
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    
    if terminal(state):
        return utility(state)
    v = 2
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
        
    return v

#Choose ia's move
def ia_move(state):
    meilleur_coup = ""
    state_to_use = copy.deepcopy(state)
    for action in actions(state):
        v_min = min_value(result(state_to_use, action))
        v_max = max_value(result(state_to_use, action))
        if utility(result(state, action)) == -1:
            meilleur_coup = action
            return meilleur_coup
        if v_max == -1 and v_min == -1:
            meilleur_coup = action
        elif v_min == -1 and v_max == 0:
            meilleur_coup = action
        elif v_min == 0 and v_max == 0:
            meilleur_coup = action  
        
    return meilleur_coup    




