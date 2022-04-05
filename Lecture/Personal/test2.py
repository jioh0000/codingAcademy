from sympy import false

def check_result(player_position, current_player):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return "Draw"

    solution = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], 
                [3,5,7], [1,4,7], [2,5,8], [3,6,9]] #Cases in which determine a winner

    for i in solution:
        if all(y in player_position[current_player] for y in i):
            # If any winning combi satisfies, return win
            return "Win"

    return False


def single_game(current_player):
    inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #Stores the positions of X and O
    player_position = {'X':[], 'O':[]}
    while True:
        print("\n")
        print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
        print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
        print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
    
        print("Player", current_player, "Select a grid!:", end=" ")
        move = int(input())
        
        if move < 1 or move > 9:
            print()
            continue
        
        if inputs[move - 1] != ' ':
            print("grid alread taken. Try again")
            continue
        
        inputs[move - 1] = current_player
        player_position[current_player].append(move)

        #Function call for check_win
        if check_result(player_position, current_player) == "Win":
            print("\n")
            print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
            print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
            print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
            print("Player ", current_player, "won\n")
            return current_player

        if check_result(player_position, current_player) == "Draw":
            print("\n")
            print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
            print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
            print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
            print("Game Drawn\n")
            return "Drawn"

        #switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


#main
player1 = "X"
player2 = "O"

current_player = player1
player_choice = {'X': "", 'O': ""}

while True:
    player_choice['X'] == current_player
    if current_player == player1:
        player_choice['O'] = player2
    else:
        player_choice['O'] = player1

    single_game('X')

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1