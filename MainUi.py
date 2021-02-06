#======< Calculator Application With Python And PyQt5 liberarry >==========+
#    By: Majid Issa                                                        |
#                                                                          |
#    copy rghits: © 2020 2021                                              |
#==========================================================================+

from PyQt5.QtCore import QSize ,Qt
from PyQt5.QtWidgets import QFrame ,QWidget ,QVBoxLayout ,QHBoxLayout ,QGridLayout ,QSpacerItem ,QSizePolicy ,QPushButton ,QLineEdit
from functools import partial

# import style sheet file
with open("Resources/styleSheet.css" ,"r") as f:
    Ss = f.read()


class MainWindowUi(object):
    
    # window status minimiz or maximize
    window_status = 0
    
    def setupUi(self, MainWindow):
        MainWindow.resize(350,550)
        MainWindow.move(500 ,100)
        
        self.MainFram = QWidget(MainWindow)
        self.MainFram.setObjectName(u"MainFram")
        self.MainFram.setStyleSheet(Ss)
        
        self.HeaderFrame = QFrame(self.MainFram)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setMinimumSize(QSize(0, 25))
        self.HeaderFrame.setMaximumSize(QSize(1000000, 25))
        self.HeaderFrame.setFrameShape(QFrame.NoFrame)
        self.HeaderFrame.setFrameShadow(QFrame.Raised)
        self.HeaderFrame.setStyleSheet(Ss)
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        self.NavBtnFrame = QFrame(self.HeaderFrame)
        self.NavBtnFrame.setObjectName(u"NavBtnFrame")
        self.NavBtnFrame.setMinimumSize(QSize(50, 0))
        self.NavBtnFrame.setMaximumSize(QSize(100, 16777215))
        self.NavBtnFrame.setFrameShape(QFrame.NoFrame)
        self.NavBtnFrame.setFrameShadow(QFrame.Raised)
        
        self.minimize_btn = QPushButton(self.NavBtnFrame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(14, 14))
        self.minimize_btn.setMaximumSize(QSize(14, 14))
        self.minimize_btn.setStyleSheet(Ss)
        
        self.restor_btn = QPushButton(self.NavBtnFrame)
        self.restor_btn.setObjectName(u"restor_btn")
        self.restor_btn.setMinimumSize(QSize(14, 14))
        self.restor_btn.setMaximumSize(QSize(14, 14))
        self.restor_btn.setStyleSheet(Ss)
        
        self.close_btn = QPushButton(self.NavBtnFrame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(14, 14))
        self.close_btn.setMaximumSize(QSize(14, 14))
        self.close_btn.setStyleSheet(Ss)
        
        self.DisplayCanvas = QLineEdit(self.MainFram)
        self.DisplayCanvas.setObjectName(u"DisplayCanvas")
        self.DisplayCanvas.setMinimumSize(QSize(0, 100))
        self.DisplayCanvas.setMaximumSize(QSize(1000000, 100))
        self.DisplayCanvas.setCursorPosition(4)
        self.DisplayCanvas.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.DisplayCanvas.setReadOnly(True)
        self.DisplayCanvas.setCursorPosition(4)
        self.DisplayCanvas.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        
        self.BtnsFrame = QWidget(self.MainFram)
        self.BtnsFrame.setObjectName(u"BtnsFrame")
        self.BtnsFrame.setStyleSheet(Ss)
        
        
        ##==> SET LAYOUTS
        MainWindow.setCentralWidget(self.MainFram)
        
        self.MainLayout = QVBoxLayout(self.MainFram)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
        ###<!|!>###
        self.MainLayout.addWidget(self.HeaderFrame)
        self.MainLayout.addWidget(self.DisplayCanvas)
        self.MainLayout.addWidget(self.BtnsFrame)
        
        
        self.HeaderFrameLayout = QHBoxLayout(self.HeaderFrame)
        self.HeaderFrameLayout.setObjectName(u"horizontalLayout")
        self.HeaderFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderFrameLayout.setSpacing(0)
        ###<!|!>###
        self.HeaderFrameLayout.addItem(self.horizontalSpacer)
        self.HeaderFrameLayout.addWidget(self.NavBtnFrame)

        
        self.NavBtnLayout = QHBoxLayout(self.NavBtnFrame)
        self.NavBtnLayout.setObjectName(u"NavBtnLayout")
        self.NavBtnLayout.setContentsMargins(0, 0, 5, 0)
        self.NavBtnLayout.setSpacing(5)
        ###<!|!>###
        self.NavBtnLayout.addWidget(self.minimize_btn)
        self.NavBtnLayout.addWidget(self.restor_btn)
        self.NavBtnLayout.addWidget(self.close_btn)
        
        
        self.BtnsFrameLayout = QGridLayout(self.BtnsFrame)
        ###<!|!>###
        
        
        ##------ Set Key Bord Buttons -------##
        
        self.btn_dict = {'C': (0, 0) ,'%': (0, 1) ,'>': (0, 2) ,'/': (0, 3) ,
                         '7': (1, 0) ,'8': (1, 1) ,'9': (1, 2) ,'*': (1, 3) ,
                         '4': (2, 0) ,'5': (2, 1) ,'6': (2, 2) ,'-': (2, 3) ,
                         '1': (3, 0) ,'2': (3, 1) ,'3': (3, 2) ,'+': (3, 3) ,
                        '00': (4, 0) ,'0': (4, 1) ,'.': (4, 2) ,'=': (4, 3)}
        btns = {}
        
        for btn_txt ,pos in self.btn_dict.items():
            btns[btn_txt] = QPushButton(btn_txt)
            btns[btn_txt].clicked.connect(partial(self.startCalculate ,btn_txt))
            
            if pos[0] == 0 or pos[1] == 3:
                btns[btn_txt].setObjectName(u"KeyBordSympol")
            else:
                btns[btn_txt].setObjectName(u"KeyBord")
            
            btns[btn_txt].setFixedSize(50 ,50)
            self.BtnsFrameLayout.addWidget(btns[btn_txt] ,pos[0] ,pos[1])

        
    def startCalculate(self ,text):
        current_text = self.DisplayCanvas.text()
        
        if text not in {'C' ,'=' ,'>'}:
            self.DisplayCanvas.setText(current_text+text)
        
        elif text == 'C':
            self.DisplayCanvas.setText("")
            self.DisplayCanvas.setPlaceholderText("")
            
        elif text == '>':
            self.DisplayCanvas.setText(current_text[:-1])
        
        elif text in {'='}:
            try:
                self.DisplayCanvas.setText(str(eval(current_text)))
            
            except Exception:
                self.DisplayCanvas.setText("")
                self.DisplayCanvas.setPlaceholderText('Error')
            
        
        
        
