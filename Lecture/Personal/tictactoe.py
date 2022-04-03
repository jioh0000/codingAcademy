from sympy import false


def grid_tic_tac_toe(inputs):
    print("\n")
    print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
    print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
    print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")



#print(grid_tic_tac_toe(['X','O','X','X','O','X','X','O','X']))

#Function to check if anyone has won
def check_result(player_position, current_player):

    if len(player_position['X']) + len(player_position['O']) == 9:
        return "Draw"

#이길 수 있는 모든 경우의 수
    solution = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], 
                [3,5,7], [1,4,7], [2,5,8], [3,6,9]]
    
    for i in solution:
        if all(y in player_position[current_player] for y in i):
            # if any_winning combi satisfies, return true
            return "Win"

    return False


def single_game(current_player):
    inputs = []
    for i in range(9):
        inputs.append(' ')
    #stores the positions of X and O
    player_position = {'X':[], 'O':[]}
    while True:
        grid_tic_tac_toe(inputs)
    
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
            grid_tic_tac_toe(inputs)
            print("Player ", current_player, "won\n")
            return current_player

        if check_result(player_position, current_player) == "Draw":
            grid_tic_tac_toe(inputs)
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