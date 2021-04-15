import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("hello7.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.num_clicked)
        self.pb2.clicked.connect(self.num_clicked)
        self.pb3.clicked.connect(self.num_clicked)
     
    def num_clicked(self) :
        com = random.random()
        
        if com > 0.3 :
            a = "가위"
        elif com > 0.6:
            a = "바위"
        else:
            a = "보"
        
        user = self.sender().text()
        
        if a == user:
            b = "비겼습니다"
         
        elif a > user:
            b = "졌습니다"
        else :
            b = "이겼습니다"
        
        self.le1.setText(user)
        self.le2.setText(a)
        self.le3.setText(b)
        
      
        
        


if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()