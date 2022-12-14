class Board:
    EDGE = 3
    WIN_REACH = 3
    PIECE = (" ", "o", "x")
    MARU = 1
    BATSU = -1
    EMPTY = 0
    ALLOWED_NUMBERS = [str(i+1) for i in range(EDGE)]
    AXIS = [i for i in range(10)]


    def __init__(self):
        self.grid_data = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        self.piece = -1

            
    def show(self):
        print()
        self.grid = [[0 for _ in range(self.EDGE)] for _ in range(self.EDGE)]
        for i in range(self.EDGE+1):
            print(self.AXIS[i], end = " ")
        print()
        for i in range(self.EDGE):
            print(self.AXIS[i+1], end = " ")
            for j in range(self.EDGE):
                print(self.PIECE[self.grid_data[i][j]], end = " ")
            print()
            

    def set_(self, x, y):
        self.grid_data[y][x] = self.piece



    
    def grid_check(self, i, j):
        if self.grid_data[i][j] == self.piece:
            return True


    def around_check(self, i, j, n, m):
        if (n != 0 or m != 0) and (0 <= i+n <= self.EDGE-1 and 0 <= j+m <= self.EDGE-1):
            if self.grid_data[i+n][j+m] == self.piece:
                return True


    def result(self, i, j, n, m):
        count = 1
        for t in range(self.EDGE):
            if 0 <= i+n*(t+1) <= self.EDGE-1 and 0 <= j+m*(t+1) <= self.EDGE-1:
                if self.grid_data[i+n*(t+1)][j+m*(t+1)] == self.piece:
                    count += 1
                    if count == self.WIN_REACH:
                        self.show()
                        print("\n" + self.PIECE[self.piece], "WIN")
                        return True
        if turn == self.EDGE**2:
            self.show()
            print("\nDRAW")
            return True


    def trial(self):
        for i in range(self.EDGE):
            for j in range(self.EDGE):
                if self.grid_check(i, j):
                    for n in (-1, 0, 1):
                        for m in (-1, 0, 1):
                            if self.around_check(i, j, n, m):
                                if self.result(i, j, n, m):
                                    return True


class TUIBoard(Board):

    def input_(self):
        re = False
        emp = True

        while True:
            self.show()
            if re:
                print("1 ~", self.EDGE, "??????????????????????????????")
            elif not emp:
                print("???????????????????????????????????????")
            else:
                print()
            print("You :", self.PIECE[self.piece])

            re = False
            emp = True

            x = input("X = ")
            if x in self.ALLOWED_NUMBERS:
                x = int(x)-1
            else:
                re = True
                continue

            y = input("Y = ")
            if y in self.ALLOWED_NUMBERS:
                y = int(y)-1
            else:
                re = True
                continue
            
            if self.grid_data[y][x] != self.EMPTY:
                emp = False
                continue
            else:
                return x, y


        
board = TUIBoard()
turn = 0
while True:
    board.piece *= -1
    turn += 1

    x, y = board.input_()
    board.set_(x, y)
    if board.trial():
        break
