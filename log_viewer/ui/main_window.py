from PySide6.QtWidgets import QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget
from interfaces.data_source import ILogSource
from services.filter_strategy import NoFilter, IFilterStrategy

class MainWindow(QMainWindow):

    def __init__(self, source: ILogSource):
        super().__init__()
        self.source = source
        self.filter_strategy: IFilterStrategy = NoFilter()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Log Viewer")

        self.list_widget = QListWidget()
        self.button = QPushButton("Load Logs")
        self.button.clicked.connect(self.load_data)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def set_filter_strategy(self, strategy: IFilterStrategy):
        self.filter_strategy = strategy

    def load_data(self):
        logs = self.source.get_logs()
        filtered = self.filter_strategy.filter(logs)

        self.list_widget.clear()
        self.list_widget.addItems(filtered)