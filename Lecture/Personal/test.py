from sympy import false

def check_result(player_position, current_player):

    winningGridPosition = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], 
                [3,5,7], [1,4,7], [2,5,8], [3,6,9]] #Cases in which determine a winner

    for i in winningGridPosition:
        if all(y in player_position[current_player] for y in i):
            # If any winning combi satisfies, return win
            return 'Win'

    if len(player_position['X']) + len(player_position['O']) == 9:
        return 'Draw'

    return False


player1 = 'X'
player2 = 'O'

current_player = player1
player_choice = {'X': '', 'O': ''}

while True:
    player_choice['X'] == current_player
    if current_player == player1:
        player_choice['O'] = player2
    else:
        player_choice['O'] = player1

    inputs = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #Stores the positions of X and O
    player_position = {'X':[], 'O':[]}
    while True:
        print("\n")
        print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
        print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
        print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
    
        print(current_player, "--> Select a grid!:", end=" ")
        userSelectGrid = int(input())
        
        if inputs[userSelectGrid - 1] != ' ':
            print("Alread taken. Try again")
            continue
        
        inputs[userSelectGrid - 1] = current_player
        player_position[current_player].append(userSelectGrid)

        #Function call for check_win
        if check_result(player_position, current_player) == 'Win':
            print("\n")
            print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
            print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
            print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
            print('winner is ',current_player,'\n')
            break

        if check_result(player_position, current_player) == "Draw":
            print("\n")
            print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}]\n")
            print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}]\n")
            print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}]\n")
            print('Draw\n')
            break

        #switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

  