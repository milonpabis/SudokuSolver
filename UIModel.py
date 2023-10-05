from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from SudokuSolver import SudokuSolver



class AppWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sudoku Solver")
        self.list = []
        self.pushButton.pressed.connect(self.create_list_and_start)

    def create_list_and_start(self):
        temp_list = []
        for i in range(1, 82):
            eval(f"self.list.append(self.l{i}.text())")
        for idx, item in enumerate(self.list):
            if not item or not item.isnumeric():
                self.list[idx] = 0
        for i in range(81):
            self.list[i] = int(self.list[i])
        for i in range(0, 81, 9):
            t = []
            for j in range(i, i+9):
                t.append(self.list[j])
            temp_list.append(t)
        self.list = temp_list
        solver = SudokuSolver(self.list)
        solver.solve()
        solver.print_board()
        idx = 1
        for i in range(9):
            for j in range(9):
                eval(f"self.l{idx}.setText(str(solver.board[{i}][{j}]))")
                idx += 1







