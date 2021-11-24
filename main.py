import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Git и желтые окружности")
        self.doRepaint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.doRepaint = True
        self.repaint()
        self.doRepaint = False

    def paintEvent(self, event):
        if self.doRepaint:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor(255, 255, 0))
            radius = random.randint(20, 120)
            painter.drawEllipse(230, 211, radius, radius)
            painter.end()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    execute = YellowCircles()
    execute.show()
    sys.exit(application.exec_())