
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
from PySide6.QtCore import Qt


class Header(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(75)
        self.setObjectName("Header")

        self.build_ui()

    def build_ui(self):
        layout = QHBoxLayout(self)

        layout.setContentsMargins(30, 10, 30, 10)
        layout.setSpacing(20)

        # Page title
        self.page_title = QLabel("Dashboard")
        self.page_title.setObjectName("PageTitle")

        layout.addWidget(self.page_title)

        layout.addStretch()

        # Search field
        search = QLineEdit()
        search.setPlaceholderText("Search anything...")
        search.setObjectName("SearchBar")
        search.setFixedWidth(250)
        search.setClearButtonEnabled(True)

        layout.addWidget(search)

        # User profile placeholder
        profile = QLabel("USER")
        profile.setObjectName("ProfileLabel")
        profile.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(profile)

    def set_page_title(self, title):
        self.page_title.setText(title)
