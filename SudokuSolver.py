#   1. divide board to squares
#   2. create square checking function
#   3. create vertical and horizontal checking function
#   4. create
#


HEIGHT = 9
WIDTH = 9


class SudokuSolver:

    def __init__(self, board):
        self.board = board




    def check_row(self, number, row):
        values_in_row = self.board[row]
        return number in values_in_row

    def check_col(self, number, col):
        values_in_col = [self.board[i][col] for i in range(HEIGHT)]
        return number in values_in_col

    def check_square(self, number, row, col):
        s_h = row//3*3
        s_w = col//3*3
        values_in_square = [self.board[row][col] for row in range(s_h, s_h+3) for col in range(s_w, s_w+3)]
        return number in values_in_square

    def can_be_placed(self, number, row, col):
        if not self.check_square(number, row, col):
            if not self.check_col(number, col):
                if not self.check_row(number, row):
                    return True
        return False

    def solve(self, row=0, col=0):
        if row == 9:
            return True
        if col == 9:
            return self.solve(row+1, 0)
        if self.board[row][col] != 0:
            return self.solve(row, col+1)
        for i in range(1, 10):
            if self.can_be_placed(i, row, col):
                self.board[row][col] = i
                if self.solve(row, col+1):
                    return True
                self.board[row][col] = 0
        return False

    def print_board(self):
        print("SOLUTION:\n")
        for i in range(HEIGHT):
            print(self.board[i])




