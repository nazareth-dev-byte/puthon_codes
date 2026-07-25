
#Introduction to labels in PyQt5

import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt — a module containing lots of constants used throughout PyQt5, including alignment options (like Qt.AlignCenter).

from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

#QLabel — a widget specifically for displaying text (or images) inside a window.
        label = QLabel("Hello World", self) #Creates a new label widget displaying the text "Hello World".
        # The second argument, self, tells PyQt5 that this label belongs inside MainWindow — meaning it'll actually show up within this window, rather than floating separately or not appearing at all.
        #QFont — lets you control font family and size.
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #293236;" 
                            "background-color: #E2ECE9;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: none;")
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        label.setAlignment(Qt.AlignCenter)
        #label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignLeft)

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
