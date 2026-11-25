
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)

from components.sidebar import Sidebar
from components.header import Header


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("FLOWSTATE")
        self.resize(1200, 760)
        self.setMinimumSize(950, 600)

        self.build_interface()

    def build_interface(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        # Main content area
        content_widget = QWidget()
        content_widget.setObjectName("ContentArea")

        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Header
        self.header = Header()
        content_layout.addWidget(self.header)

        # Page content placeholder
        self.page_content = QWidget()
        page_layout = QVBoxLayout(self.page_content)

        page_layout.setContentsMargins(35, 35, 35, 35)

        welcome = QLabel("Welcome to FLOWSTATE")
        welcome.setObjectName("WelcomeTitle")

        description = QLabel(
            "Your workspace. Your focus. Your progress."
        )
        description.setObjectName("WelcomeDescription")

        page_layout.addWidget(welcome)
        page_layout.addWidget(description)
        page_layout.addStretch()

        content_layout.addWidget(self.page_content)

        main_layout.addWidget(content_widget)

        self.setCentralWidget(central_widget)

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #111318;
            }

            QWidget#Sidebar {
                background-color: #171A21;
            }

            QLabel#Logo {
                color: #F8FAFC;
                font-size: 23px;
                font-weight: 800;
                letter-spacing: 2px;
            }

            QLabel#Tagline {
                color: #64748B;
                font-size: 9px;
                font-weight: 600;
            }

            QLabel#SectionLabel {
                color: #64748B;
                font-size: 10px;
                font-weight: 700;
                padding-bottom: 8px;
            }

            QPushButton#NavButton {
                background-color: transparent;
                color: #A1A1AA;
                border: none;
                border-radius: 8px;
                padding: 12px;
                text-align: left;
                font-size: 13px;
            }

            QPushButton#NavButton:hover {
                background-color: #252A35;
                color: #FFFFFF;
            }

            QWidget#ContentArea {
                background-color: #111318;
            }

            QWidget#Header {
                background-color: #171A21;
                border-bottom: 1px solid #292D38;
            }

            QLabel#PageTitle {
                color: #F8FAFC;
                font-size: 18px;
                font-weight: 700;
            }

            QLineEdit#SearchBar {
                background-color: #222630;
                color: #F8FAFC;
                border: 1px solid #303644;
                border-radius: 8px;
                padding: 9px 12px;
                font-size: 12px;
            }

            QLineEdit#SearchBar:focus {
                border: 1px solid #818CF8;
            }

            QLabel#ProfileLabel {
                background-color: #343A50;
                color: #FFFFFF;
                border-radius: 18px;
                min-width: 36px;
                max-width: 36px;
                min-height: 36px;
                max-height: 36px;
                font-size: 10px;
                font-weight: 700;
            }

            QLabel#WelcomeTitle {
                color: #F8FAFC;
                font-size: 30px;
                font-weight: 700;
            }

            QLabel#WelcomeDescription {
                color: #94A3B8;
                font-size: 14px;
            }

            QLabel#Footer {
                color: #64748B;
                font-size: 10px;
            }
        """)
