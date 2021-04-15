import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("hello3.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
     
    def pb_clicked(self) :
        a = int(self.le1.text())
        b = int(self.le2.text())
        self.le3.setText(str(a+b))


if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()