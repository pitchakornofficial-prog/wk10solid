import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from services.factory import SourceFactory

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # เปลี่ยนตรงนี้เพื่อสลับ Source ได้ทันที
    source = SourceFactory.create_source("mock")

    window = MainWindow(source)
    window.show()

    sys.exit(app.exec())