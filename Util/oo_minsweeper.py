class UserInput():
    def __init__(self, value):
        self.operation = value.pop(0)
        remove = set(list(["(", ")" ,","]))
        temp = [x for x in value if x not in remove]
        self.x, self.y = int(temp.pop(0)), int(temp.pop(0))


class PlayBoard():
    def __init__(self, x, y, matrix):
        self.x = x
        self.y = y
        self.cells = [[Cell(matrix[j][k]) for k in range(y)] for j in range(x)]
        self.is_mine_opened = False
        self.count_non_mine_opened = 0
        self.total_non_mine = sum([sum(map(lambda x : 1 if x != 'm' else 0, row)) for row in matrix])

    def o(self, x, y):
        cell = self.cells[x][y]
        print(cell.value)
        if cell.value == "o":
            print("Already opened.")
            return
        if cell.value == "m":
            self.is_mine_opened = True
        else:
            self.count_non_mine_opened += 1

    def f(self, x, y, display_value):
        cell = self.cells[x][y]
        if display_value == "o": self.count_non_mine_opened -= 1
        cell.value == 'f'


class Cell():
    def __init__(self, value):
        self.is_flagged = False
        self.is_opened = False
        self.value = value


class Game():

    def __init__(self, matrix):
        self.x, self.y = len(matrix), len(matrix[0])
        self.play_board = PlayBoard(self.x, self.y, matrix)

    def is_won(self):
        return self.play_board.count_non_mine_opened == self.play_board.total_non_mine

    def validate_input(self, x, y):
        if min(x, y) < 0 or x >= self.play_board.x  or y >= self.play_board.y:
            # Throw invalid argument exception
            pass

    def play(self, operation, x, y):
        self.validate_input(x, y)
        if operation == 'o':
            self.play_board.o(x, y)

        else:
            self.play_board.f(x, y)

    def print_display_board(self):
        print("\n".join(["".join(x) for x in self.play_board]))

    def handle_display(self):
        # if self.play_board.is_mine_opened:
        #     self.print_updated_display_board()
        # else:
        self.print_display_board()


    def start_game(self):
        turn = 0
        while not self.play_board.is_mine_opened and not self.is_won():
            user_input = UserInput(list(input("Enter your input")))

            self.play(user_input.operation, user_input.x, user_input.y)
            turn += 1
            self.handle_display()
            turn += 1
        if self.play_board.is_mine_opened:
            print("Oops, you stepped on a mine! Game over !")
        else:
            print("Wow, you cleared the minefield! Game over !")

# str_in = "xxm, xmx, xxx"
str_in = input()
mat = [[l for l in k ] for k in str_in.strip().split(',')]
print(mat)
game = Game(mat)
game.start_game()


