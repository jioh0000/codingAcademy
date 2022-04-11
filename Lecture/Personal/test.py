def check_result(player_choice, current_player):

    winningGridPosition = [[7,8,9],[4,5,6],[1,2,3],[1,5,9], 
                [3,5,7],[1,4,7],[2,5,8],[3,6,9]] #Cases in which determine a winner

    for i in winningGridPosition:
        if all(j in player_choice[current_player] for j in i):
            # If any winning combi satisfies, return win
            return 'Win'

    if len(player_choice['X']) + len(player_choice['O']) == 9:
        return 'Draw'

    return False


player1 = 'X'
player2 = 'O'
current_player = player1

while True:

    inputlist = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #Stores the positions of X and O

    player_choice = {'X':[], 'O':[]}
    
    while True:
        #Output (Grid)
        print("\n")
        print(f"\t [{inputlist[0]}] | [{inputlist[1]}] | [{inputlist[2]}]\n") 
        print(f"\t [{inputlist[3]}] | [{inputlist[4]}] | [{inputlist[5]}]\n")
        print(f"\t [{inputlist[6]}] | [{inputlist[7]}] | [{inputlist[8]}]\n")
    
        print(current_player, "--> Select a grid!:", end=" ")
        #Input (GridNum)
        userSelectGrid = int(input())
        
        if inputlist[userSelectGrid - 1] != ' ':
            print("Alread taken. Try again")
            continue
        
        inputlist[userSelectGrid - 1] = current_player


        player_choice[current_player].append(userSelectGrid)


        #Function call for check win
        if check_result(player_choice, current_player) == 'Win':
            #Output (Grid)
            print("\n")
            print(f"\t [{inputlist[0]}] | [{inputlist[1]}] | [{inputlist[2]}]\n")
            print(f"\t [{inputlist[3]}] | [{inputlist[4]}] | [{inputlist[5]}]\n")
            print(f"\t [{inputlist[6]}] | [{inputlist[7]}] | [{inputlist[8]}]\n")
            print('winner is ',current_player,'\n')
            break
        #Function call for check draw
        if check_result(player_choice, current_player) == "Draw":
            #Output (Grid)
            print("\n")
            print(f"\t [{inputlist[0]}] | [{inputlist[1]}] | [{inputlist[2]}]\n")
            print(f"\t [{inputlist[3]}] | [{inputlist[4]}] | [{inputlist[5]}]\n")
            print(f"\t [{inputlist[6]}] | [{inputlist[7]}] | [{inputlist[8]}]\n")
            print('Draw\n')
            break

        #switch player
        if current_player == 'O':
            current_player = 'X'
        else:
            current_player = 'O'