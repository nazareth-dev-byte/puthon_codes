
#PyQt5 layouts
#Radio Buttons  in PyQt5
#With radio buttons, we're limited to only just one option. That's the essence of radio buttons.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        #With the default behaviour of PyQt5, all radio buttons unless explicitly stated, are all part of the same group.
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Master Card", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.buttonGroup1 = QButtonGroup(self)
        self.buttonGroup2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size:35px;"
                           "font-family:Verdana;"
                           "padding:10px;"
                           "}")

        self.buttonGroup1.addButton(self.radio1)
        self.buttonGroup1.addButton(self.radio2)
        self.buttonGroup1.addButton(self.radio3)
        self.buttonGroup2.addButton(self.radio4)
        self.buttonGroup2.addButton(self.radio5)

        #Each radio button don't quite do anything yet so let's connect them to a signal

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
