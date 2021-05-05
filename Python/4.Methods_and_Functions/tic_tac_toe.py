def display_grid(grid):
    print('\n{} | {} | {}\n----------\n{} | {} | {}\n----------\n{} | {} | {}'.format(grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8],))

def change_grid(player,position):
    if player == 1:
        grid[position] = 'x'
    else:
        grid[position] = 'o'

def player_input(player):
    while(True):
        print("\nplease select one of the following 0,1,2,3,4,5,6,7,8")
        choice = int(input('Player{}: '.format(player)))
        if choice in [0,1,2,3,4,5,6,7,8]:
            return choice

def check_result(grid):
    if grid[0] == grid[1] == grid[2] == 'x' or grid[3] == grid[4] == grid[5] == 'x' or grid[6] == grid[7] == grid[8] == 'x':
        print("\nPlayer1 wins")
        return 1
    elif grid[0] == grid[1] == grid[2] == 'o' or grid[3] == grid[4] == grid[5] == 'o' or grid[6] == grid[7] == grid[8] == 'o':
        print("\nPlayer 2 wins")
        return 1
    elif grid[0] == grid[3] == grid[6] == 'x' or grid[1] == grid[4] == grid[7] == 'x' or grid[2] == grid[5] == grid[8] == 'x':
        print("\nPlayer1 wins")
        return 1
    elif grid[0] == grid[3] == grid[6] == 'o' or grid[1] == grid[4] == grid[7] == 'o' or grid[2] == grid[5] == grid[8] == 'o':
        print("\nPlayer 2 wins")
        return 1
    elif grid[0] == grid[4] == grid[8] == 'x' or grid[2] == grid[4] == grid[6] == 'x':
        print("\nPlayer1 wins")
        return 1
    elif grid[0] == grid[4] == grid[8] == 'o' or grid[2] == grid[4] == grid[6] == 'o':
        print("\nPlayer 2 wins")
        return 1
    elif ' ' not in grid:
        print("\nIts a draw")
        return 1
    else:
        return 2

grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1
result = 2

display_grid(grid)

while(result == 2):

    position = player_input(player)

    change_grid(player, position)

    display_grid(grid)

    result = check_result(grid)

    if player == 1:
        player = 2
    else:
        player = 1

    if result == 1:
        break



