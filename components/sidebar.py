
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PySide6.QtCore import Qt


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(230)
        self.setObjectName("Sidebar")

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 28, 20, 20)
        layout.setSpacing(12)

        logo = QLabel("FLOWSTATE")
        logo.setObjectName("Logo")

        tagline = QLabel("YOUR PRODUCTIVITY SPACE")
        tagline.setObjectName("Tagline")

        layout.addWidget(logo)
        layout.addWidget(tagline)
        layout.addSpacing(35)

        section = QLabel("WORKSPACE")
        section.setObjectName("SectionLabel")

        layout.addWidget(section)

        self.buttons = {}

        navigation_items = [
            "Dashboard",
            "Tasks",
            "Focus",
            "Analytics",
            "Notes",
            "Settings",
        ]

        for name in navigation_items:
            button = QPushButton(name)
            button.setObjectName("NavButton")
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            layout.addWidget(button)
            self.buttons[name] = button

        layout.addStretch()

        footer = QLabel("Stay focused. Keep growing.")
        footer.setObjectName("Footer")

        layout.addWidget(footer)
