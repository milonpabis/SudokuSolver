from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from SudokuSolver import SudokuSolver


class AppWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sudoku Solver")
        self.list = []
        self.bt_solve.pressed.connect(self._create_list_and_start)
        self.bt_clear.pressed.connect(self._fill)


    def _create_list_and_start(self):       # function reading user input and solving the sudoku
        temp_list = []
        for i in range(1, 82):              # gets the input
            widget = getattr(self, f"l{i}")
            self.list.append(widget.text())

        for idx, item in enumerate(self.list):  # converting empty/not_numerical inputs to NULL
            if not item or not item.isnumeric():
                self.list[idx] = 0

        for i in range(81):                     # mapping to int
            self.list[i] = int(self.list[i])

        for i in range(0, 81, 9):               # converting into 2D array
            t = []
            for j in range(i, i+9):
                t.append(self.list[j])
            temp_list.append(t)

        self.list = temp_list
        solver = SudokuSolver(self.list)
        solver.solve()
        self._fill(solver.board)
        self.list = []

    def _fill(self, board: list[list] = None):      # filling function, if no 2D array given -> fills with empty strings
        idx = 1
        for i in range(9):
            for j in range(9):
                widget = getattr(self, f"l{i * 9 + j + 1}")
                if not board:
                    widget.setText('')
                else:
                    widget.setText(str(board[i][j]))
                idx += 1







