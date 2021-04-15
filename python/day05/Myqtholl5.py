import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


form_class = uic.loadUiType("hello5.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
     
    def pb_clicked(self) :
        com = random.random()
        user = self.le1.text()
        
        if com > 0.5 :
            a = "홀"
        else:
            a = "짝"
        
        if a == user:
            self.le3.setText("이겼습니다")
            self.le3.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: white;"
                             "border-radius: 3px;"
                             "background:green;")
        else:
            self.le3.setText("졌습니다")
            self.le3.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF;"
                              "background:red;")
                
        self.le2.setText(a)
      
        
        


if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()