def print_tic_tac_toe(game_values):
    print(" --- --- --- ")
    print(f"| {game_values[0]} | {game_values[1]} | {game_values[2]} |")
    print(" --- --- --- ")
    print(f"| {game_values[3]} | {game_values[4]} | {game_values[5]} |")
    print(" --- --- --- ")
    print(f"| {game_values[6]} | {game_values[7]} | {game_values[8]} |")
    print(" --- --- --- ")

def isMoveValid(move):
    if move < 1 or move > 9:
        print_tic_tac_toe(game_values)
        print("please enter a valid move!")
        return False
    elif (game_values[move - 1] != ' '):
        print_tic_tac_toe(game_values)
        print("Selected box is already occupied please select other box!")
        return False
    else:
        return True

def start_game(curplayer):
    move =  int(input(f"player {curplayer} turn. Which box?: "))
    if (isMoveValid(move)):
        update_box(move,curplayer)
    else:
        start_game(curplayer)

def update_box(move,curplayer):
    game_values[move-1] = curplayer
    position[curplayer].append(move)

def switch_player(curplayer):
    if curplayer == 'X':
        return '0'
    elif curplayer == '0':
        return 'X'

def check_for_completion(curplayer,position):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    if (position[curplayer])in solution:
        print(f"\n Congrats!! player {curplayer} won :)")
        return True
    elif len(position['X']) + len(position['0']) == 9:
        print("\n Game Drawn!")
        return True
    else:
        return False

print("\n Enter 1 for X \n Enter 2 for 0")
user_input = int(input("Turn to choose: "))

curplayer= ""
game_values = [' ' for x in range(9)]
position = {'X':[],'0':[]}
print_tic_tac_toe(game_values)

if user_input == 1:
    curplayer = 'X'
elif user_input == 2:
    curplayer = '0'

while True:
    start_game(curplayer)
    print_tic_tac_toe(game_values)
    if(check_for_completion(curplayer,position)):
        break
    curplayer = switch_player(curplayer)

