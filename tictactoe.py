grid = [['1' , '2', '3'], # The player grid
        ['4', '5', '6'],
        ['7', '8' , '9']]

def reset_grid():
    grid = [['1' , '2', '3'], # The player grid
        ['4', '5', '6'],
        ['7', '8' , '9']]

def print_grid(): # Prints out the player grid
    count = 0 # When to print new line
    for row in grid:
        for element in row:
            print(f'{element} ', end=' ')
        print()

def mod_grid(choice, turn): #Changes the grid based on player input
    for i, row in enumerate(grid):
        if choice in row:
            y = row.index(choice) #Index of player choice inside the sublist where the player choice is found
            if turn == 0:
                grid[i][y] = 'X'
            else:
                grid[i][y] = 'O'

def check_horiz(player): #Check horizontal player is the current player ('X' or 'Y')
    for row in grid:
        if row.count(player) == 3:
            return True
    return False

def check_vert(player):
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col]:
            return True
    return False

def check_cross(player): #Checks across the board:
    if grid[0][0] == grid[1][1] == grid [2][2]:
        return True
    elif grid[2][2] == grid[1][1] == grid [0][0]:
        return True
    else:
        return False
        
def game():
    end = False
    players = {0: 'X', 1:'Y'} #Which player's turn, 0 for X and 1 for O
    curr = 0 #Current player
    last_play = 1 #Last player
    play_count = 0

    while not end:
        choice = input(f'\nEnter a number on the grid to choose your turn! Player {players[curr]}\'s turn ')
        while len(choice) != 1 or not choice.isdigit():
            print('Please enter only one number')
            choice = input()
        if curr == 0:
            mod_grid(choice, curr)
            print_grid()
            last_play = curr
            curr = 1
            play_count += 1
        else:
            mod_grid(choice, curr)
            print_grid()
            last_play = 1
            curr = 0
            play_count += 1
        if play_count >= 3:
            if check_vert(players[last_play]):
                print(f'Player {players[last_play]} has won!')
                end = True
            elif check_horiz(players[last_play]):
                print(f'Player {players[last_play]} has won!')
                end = True
            elif check_cross(players[last_play]):
                print(f'Player {players[last_play]} has won!')
                end = True
        if play_count == 9:
            print('Tie!')
            continuee = input('Would you like to play again?').lower()
            if continuee == 'n':
                end = True
            elif continuee == 'y':
                reset_grid()        
    
def main():
    print('Welcome to Tic Tac Toe!')
    print_grid()
    print()
    game()

   
if __name__ == "__main__":
    main()