from SudokuSolver import SudokuSolver
from PySide6.QtWidgets import QApplication
from UIModel import AppWindow


if __name__ == "__main__":

    app = QApplication()
    window = AppWindow()
    window.show()
    app.exec()
