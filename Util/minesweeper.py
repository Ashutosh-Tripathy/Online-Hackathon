layout = [[l for l in k ] for k in input().split(',')]

R, C = len(layout), len(layout[0]),
play_board = [['X' for j in range(C)] for i in range(R)]

total_not_mine, count_not_mine, is_game_over, is_won = 0, 0, False, False

for row in layout:
    for value in row:
        if row == 'M':
            total_not_mine += 1


count_not_mine = 0
def handle_display():
    print(layout)

def check_win():
    return count_not_mine == total_not_mine

def validate_input(i, j):
    if min(i, j) < 0 or i >= R or j >= C:
        # Throw Invalid argument
        pass

def O(i, j):
    validate_input(i, j)
    if play_board[i][j] == "o":
        print("Already opened")
    else:
        if layout[i][j] == "m":
            print("Game over")
            is_game_over = True
        else:
            play_board[i][j] = "o"
            count_not_mine += 1
            print("Continue playing.....")
            is_won = check_win()
            if is_won: is_game_over = True
        handle_display()

def F(i, j):
    validate_input(i, j)
    if play_board[i][j] == "o":
        count_not_mine -= 1
    play_board[i][j] = "f"
    handle_display()

turn = 0

while turn < R * C or not is_game_over:
    ops = input("Enter operation ('o' or 'f'): ")
    (i, j) = map(int, input("Enter the cordinate (space seperated): ").strip().split())
    O(i, j) if ops == "o" else F(i, j)






