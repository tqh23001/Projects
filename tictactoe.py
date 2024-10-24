import re

grid = [['1' , '2', '3' ],
        ['4', '5', '6' ],
    	['7', '8' , '9' ]]

def print_grid():
    grid2 = ""
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            grid2 += "\n "
        grid2 += " ".join(map(str, row)) + '\n'
    print(grid2)

def edit_grid(player_choice):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == player_choice:
                grid[i][j] = 'x'
                break

def check_horiz():
    count = 0
    for row in grid:
        for value in row:
            if value == 'x':
                count += 1
    if count == 3:
       return 3
    elif count == 0:
        return 0
    else:
        return 1

def chekc_vert():
    count = 0
    for i in len(grid):
            if grid[i][0] == 'x':
                count += 1
    if count == 3:
        return 3
    elif count == 0:
        return 0
    else:
        return 1

def check_diag():
    count = 0
    if grid[0][0] == 'x':
        count += 1
        if grid[1][1] == 'x':
            count += 1
            if grid[2][2] == 'x':
                count += 1
    if count == 3:
        return 3
    elif count == 0:
        return 0
    else:
        return 1
    

                

def main():
    done = False
    turn = 0
    count = 0
    print('Welcome to Tic Tac Toe!')
    while not done:
         print(print_grid())
         player = input("Player 1, please choose your grid(you are 'x'):")
         if len(player) == 0 or player.isnumeric() == False:
             print('Please enter something or a number!')
             count
         else:
             edit_grid(player)
             print(print_grid())
             num = check_horiz()       
             if num == 3:
                 print('X wins!')      

             
    
        
if __name__ == "__main__":
    main()
    #print(re.sub(r']','\n', str(grid)).re.sub(r'[,','',str(grid)))