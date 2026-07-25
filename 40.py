
#How to add images to PyQt5

import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
#The class for QPixmap, it's used for handling images and functionality fir loading manipulating and displaying images. We will load out image to a QPixmap object then add the QPixmap object to a label(QLabel).


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        #We would createa a label.
        label = QLabel(self)
        label.setGeometry(QRect(0, 0, 400, 250))

        pixmap = QPixmap("image.jpeg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width())//2,
                          (self.height() - label.height())//2,
                          label.width(),
                          label.height())

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
