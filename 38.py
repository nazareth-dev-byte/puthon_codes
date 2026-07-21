
#sys gives access to system-level functions — here it's used to pass command-line arguments to the GUI app and to properly exit the program

import sys

#QApplication — every PyQt5 app needs exactly one of these; it manages the application's overall control flow and settings.
from PyQt5.QtWidgets import QApplication, QMainWindow
#QMainWindow — a ready-made class that gives you a standard application window (complete with things like a title bar, menu bar support, etc.) that you build on top of.
from PyQt5.QtGui import QIcon
#QIcon — used to set a custom icon (like the little picture in the window's title bar/taskbar)


#This creates your own window by inheriting from QMainWindow — meaning MainWindow automatically gets all of QMainWindow's built-in behavior for free, and you can customize it further. super().__init__() calls QMainWindow's own constructor first, making sure all the standard window setup happens before you add your own customizations.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Sets the text that appears in the window's title bar — here, "My First GUI".
        self.setWindowTitle("My First GUI")
        #Controls the window's position and size. The four numbers are: x=400, y=100, width=500, height=500.
#x and y set where the top-left corner of the window appears on your screen (measured in pixels from your screen's own top-left corner).
#width and height set how big the window is.
        self.setGeometry(400, 100, 500, 500)
        #Sets a custom icon for the window (shown in the title bar and taskbar), loaded from a file called "image.jpeg". This file needs to actually exist in the same folder as your script (or you'd need to give a full/relative path to wherever it actually is) — if it's missing, the icon just silently won't show up (this typically doesn't crash the program, it just fails quietly).
        self.setWindowIcon(QIcon("image.jpeg"))

def main():
    #Creates the required QApplication object — every PyQt5 program needs exactly one of these before any windows can be shown. sys.argv passes along any command-line arguments the program was launched with (even if you don't use any yourself, PyQt5 still expects this to be passed in)
    app = QApplication(sys.argv)

    ##Creates an instance of your custom MainWindow class (running its __init__, which sets the title, size, and icon), then .show() actually makes the window appear on screen. Without calling .show(), the window object would exist in memory but never actually be visible.
    window = MainWindow()
    window.show()

    #This is the line that actually starts the GUI event loop — it's what keeps your window open and responsive (listening for clicks, key presses, resizing, etc.) instead of the program just running once and immediately closing. app.exec_() runs continuously until the user closes the window, at which point it returns an exit code, and sys.exit(...) cleanly shuts down the Python program using that code.
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
