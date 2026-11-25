
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FLOWSTATE")
        self.resize(1200, 760)
        self.setMinimumSize(950, 600)

        self.build_interface()

    def build_interface(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        layout.setContentsMargins(40, 35, 40, 35)
        layout.setSpacing(18)

        title = QLabel("FLOWSTATE")
        title.setStyleSheet("""
            font-size: 34px;
            font-weight: 700;
            color: #F1F5F9;
        """)

        subtitle = QLabel(
            "Your workspace. Your focus. Your progress."
        )

        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #94A3B8;
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()

        self.setStyleSheet("""
            QMainWindow {
                background-color: #111318;
            }
        """)

        self.setCentralWidget(central_widget)
