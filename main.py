'''
calculator application 
calculator app with python and pyqt5

+=========================================+
| By       : Majid Isss                   |
| Email    : majidissa82@outlook.com      |
| WhatsApp : +201017398758                |
+=========================================+
'''

from PyQt5.QtCore import QSize ,Qt ,QMetaObject ,QCoreApplication ,QRect ,QPoint
from PyQt5.QtWidgets import (QMainWindow ,QApplication ,QVBoxLayout ,QHBoxLayout ,QScrollArea ,QFrame ,QLabel ,QPushButton ,QWidget)
from PyQt5.QtGui import QIcon
from MainUi import MainWindowUi
import sys ,os


class MainWindow(QMainWindow):
    window_status = 0
    def __init__(self):
        super().__init__()
		
        # set main UI frm design file
        self.ui = MainWindowUi()
        self.ui.setupUi(self)
		
        # Make Window Frame less
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        
        
        #==> SET BUTTONS FUNICTIONS
        
        ## SET CLOSE BUTTON EVENT
        self.ui.close_btn.clicked.connect(lambda: sys.exit())
        ## SET RESTORE BUTTON EVENT
        self.ui.restor_btn.clicked.connect(self.minimaxi)
        ## SET MINIMIZE BUTTON EVENT
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        
        
        
        # move the window
        self.ui.HeaderFrame.mouseMoveEvent = self.moveWindow
        
        # display the window
        self.show()
    
    def minimaxi(self):
        if self.window_status == 0:
            self.window_status = 1
            self.showMaximized()
            #self.restor_btn.setIcon(QIcon('24x24/cil-window-restore.png'))
        else:
            self.window_status = 0
            self.showNormal()
            #self.restor_btn.setIcon(QIcon('24x24/cil-window-maximize.png'))
    
    def moveWindow(self ,e):
        if e.buttons() == Qt.LeftButton:
            self.move(e.globalPos())



def run():
	App = QApplication(sys.argv)
	window = MainWindow()
	window.setWindowIcon(QIcon("Resources/icons/Calculator_icon.png"))
	sys.exit(App.exec_())

run()
