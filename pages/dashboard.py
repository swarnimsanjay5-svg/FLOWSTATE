
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QPushButton,
)
from PySide6.QtCore import Qt


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("DashboardPage")
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(35, 30, 35, 30)
        main_layout.setSpacing(25)

        # Welcome section
        welcome_title = QLabel("Good to see you!")
        welcome_title.setObjectName("DashboardWelcome")

        welcome_subtitle = QLabel(
            "Here's an overview of your productivity."
        )
        welcome_subtitle.setObjectName("DashboardSubtitle")

        main_layout.addWidget(welcome_title)
        main_layout.addWidget(welcome_subtitle)

        # Statistics section
        stats_layout = QGridLayout()
        stats_layout.setSpacing(18)

        stats = [
            ("TOTAL TASKS", "12", "Tasks in your workspace"),
            ("COMPLETED", "08", "Tasks finished"),
            ("PENDING", "04", "Tasks left to complete"),
            ("FOCUS TIME", "2h 30m", "Time spent focusing"),
        ]

        for index, (title, value, description) in enumerate(stats):
            card = self.create_stat_card(
                title, value, description
            )

            stats_layout.addWidget(
                card,
                0,
                index
            )

        main_layout.addLayout(stats_layout)

        # Today's tasks section
        tasks_heading = QLabel("Today's Overview")
        tasks_heading.setObjectName("DashboardSectionTitle")

        main_layout.addWidget(tasks_heading)

        tasks_card = QFrame()
        tasks_card.setObjectName("DashboardCard")

        tasks_layout = QVBoxLayout(tasks_card)
        tasks_layout.setContentsMargins(22, 20, 22, 20)
        tasks_layout.setSpacing(15)

        task_items = [
            ("Complete project documentation", "Completed"),
            ("Study Python for 1 hour", "In progress"),
            ("Organise tomorrow's schedule", "Pending"),
        ]

        for task_name, status in task_items:
            task_row = QHBoxLayout()

            task_label = QLabel(task_name)
            task_label.setObjectName("TaskPreviewName")

            status_label = QLabel(status)
            status_label.setObjectName("TaskPreviewStatus")

            task_row.addWidget(task_label)
            task_row.addStretch()
            task_row.addWidget(status_label)

            tasks_layout.addLayout(task_row)

        main_layout.addWidget(tasks_card)

        # Quick actions
        actions_heading = QLabel("Quick Actions")
        actions_heading.setObjectName("DashboardSectionTitle")

        main_layout.addWidget(actions_heading)

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)

        action_names = [
            "Create a Task",
            "Start Focus",
            "Write a Note",
        ]

        for name in action_names:
            button = QPushButton(name)
            button.setObjectName("QuickActionButton")
            button.setCursor(Qt.CursorShape.PointingHandCursor)

            actions_layout.addWidget(button)

        main_layout.addLayout(actions_layout)
        main_layout.addStretch()

    def create_stat_card(self, title, value, description):
        card = QFrame()
        card.setObjectName("DashboardCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("StatTitle")

        value_label = QLabel(value)
        value_label.setObjectName("StatValue")

        description_label = QLabel(description)
        description_label.setObjectName("StatDescription")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(description_label)

        return card
