
import sys

from PySide6.QtWidgets import QApplication
from app.window import MainWindow
from database.db import initialize_database


def main():
    initialize_database()
    print("Starting FLOWSTATE...")

    app = QApplication(sys.argv)
    app.setApplicationName("FLOWSTATE")

    window = MainWindow()
    window.show()

    print("FLOWSTATE window launched!")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
