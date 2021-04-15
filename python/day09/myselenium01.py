from selenium import webdriver
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
 
browser = webdriver.Chrome()
browser.get("http://localhost:8081/HELLOWEB2/mycrawl")
 

form_class = uic.loadUiType("01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
     
    def pb_clicked(self) :
        td = browser.find_elements_by_css_selector('td')
        for text in td:
            print(text.text)
        
if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()