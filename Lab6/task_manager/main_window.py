from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        self.title_label = QLabel("Новая задача:")
        self.title_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        main_layout.addWidget(self.title_label)

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)
        main_layout.addLayout(input_layout)

        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)

        buttons_layout = QHBoxLayout()
        self.delete_button = QPushButton("Удалить")
        self.complete_button = QPushButton("Отметить как выполненную")
        self.clear_button = QPushButton("Очистить всё")

        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.complete_button)
        buttons_layout.addWidget(self.clear_button)
        main_layout.addLayout(buttons_layout)

        self.delete_completed_button = QPushButton("Удалить выполненные")
        main_layout.addWidget(self.delete_completed_button)

        self.counter_label = QLabel("Количество задач: 0 (Выполнено: 0)")
        self.counter_label.setFont(QFont("Arial", 9))
        main_layout.addWidget(self.counter_label)

        central_widget.setLayout(main_layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.complete_button.clicked.connect(self.toggle_complete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.delete_completed_button.clicked.connect(self.delete_completed_tasks)
        self.task_list.itemDoubleClicked.connect(self.toggle_complete_task)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите название задачи! Поле не может быть пустым.",
            )
            return

        item = QListWidgetItem(text)
        item.setData(Qt.ItemDataRole.UserRole, False)
        self.task_list.addItem(item)

        self.task_input.clear()
        self.update_counter()

    def delete_task(self):
        row = self.task_list.currentRow()
        if row < 0:
            QMessageBox.warning(
                self,
                "Внимание",
                "Выберите задачу из списка для удаления.",
            )
            return

        item = self.task_list.item(row)
        answer = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f'Вы действительно хотите удалить задачу "{item.text()}"?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()

    def toggle_complete_task(self, item=None):
        if not isinstance(item, QListWidgetItem):
            row = self.task_list.currentRow()
            if row < 0:
                QMessageBox.warning(
                    self,
                    "Внимание",
                    "Выберите задачу для изменения статуса.",
                )
                return
            item = self.task_list.item(row)

        is_completed = item.data(Qt.ItemDataRole.UserRole)
        if not is_completed:
            item.setData(Qt.ItemDataRole.UserRole, True)
            item.setForeground(QColor("gray"))
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
            if not item.text().startswith("✓ "):
                item.setText(f"✓ {item.text()}")
        else:
            item.setData(Qt.ItemDataRole.UserRole, False)
            item.setData(Qt.ItemDataRole.ForegroundRole, None)
            font = item.font()
            font.setStrikeOut(False)
            item.setFont(font)
            if item.text().startswith("✓ "):
                item.setText(item.text()[2:])

        self.update_counter()

    def clear_tasks(self):
        if self.task_list.count() == 0:
            QMessageBox.information(self, "Информация", "Список задач уже пуст.")
            return

        answer = QMessageBox.question(
            self,
            "Очистка списка",
            "Вы уверены, что хотите удалить все задачи?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()

    def delete_completed_tasks(self):
        completed_count = 0
        for i in range(self.task_list.count() - 1, -1, -1):
            item = self.task_list.item(i)
            if item.data(Qt.ItemDataRole.UserRole):
                self.task_list.takeItem(i)
                completed_count += 1

        if completed_count == 0:
            QMessageBox.information(
                self,
                "Информация",
                "Нет выполненных задач для удаления.",
            )
        else:
            self.update_counter()

    def update_counter(self):
        total_count = self.task_list.count()
        completed_count = 0
        for i in range(total_count):
            item = self.task_list.item(i)
            if item.data(Qt.ItemDataRole.UserRole):
                completed_count += 1

        self.counter_label.setText(
            f"Количество задач: {total_count} (Выполнено: {completed_count})"
        )
        self.setWindowTitle(f"Менеджер задач — Всего: {total_count}")