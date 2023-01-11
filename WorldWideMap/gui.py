from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
import sys


class GuiMappa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mappa")
        self.resize(1280, 750)
        self.layout = QVBoxLayout(self)

        self.mappa = QWebEngineView()
        self.mappa.load(QUrl("file:///WorldWideMap//Mappa.html"))
        self.layout.addWidget(self.mappa)

    @staticmethod
    def start():
        app = QApplication(sys.argv)
        window = GuiMappa()
        window.show()
        app.exec_()
        sys.exit(app.exec_())
