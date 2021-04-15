import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("hello4.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
     
    def pb_clicked(self) :
        a = int(self.le1.text())
        b = int(self.le2.text())
        c = 0
        for i in range(a,b+1):
            c += i
        self.le3.setText(str(c))  
        


if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()