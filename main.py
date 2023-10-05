from SudokuSolver import SudokuSolver


TEMP_BOARD = [
    [4, 6, 0, 0, 0, 0, 0, 8, 5],
    [3, 0, 0, 0, 6, 8, 0, 0, 0],
    [0, 1, 2, 4, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 1, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [7, 0, 9, 0, 0, 0, 0, 3, 0],
    [0, 7, 0, 0, 3, 0, 0, 0, 2],
    [6, 0, 0, 7, 9, 4, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 6, 7, 3]

]



if __name__ == "__main__":
    sudoku = SudokuSolver(TEMP_BOARD)
    sudoku.solve()
    sudoku.print_board()