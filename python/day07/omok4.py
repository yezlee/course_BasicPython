import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from conda.common._logic import TRUE, FALSE
from _socket import close


form_class = uic.loadUiType("omok4.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.end = True
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.arr2dpb = []
        self.arr2d = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                    ]
        
        
        
        for i in range(10):
            line = []
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(j*40, i*40, 40, 40)
                button.setIconSize(QSize(40, 40))
                button.setIcon(self.icon0) 
                button.setToolTip(str(i)+","+str(j))
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2dpb.append(line)
        self.myrender()
        self.pb_reset.clicked.connect(self.pb_click_reset)
    def pb_click_reset(self):
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
        self.myrender()
        self.flag_wb = True
        self.end = True
                
                
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0 :
                    self.arr2dpb[i][j].setIcon(self.icon0) 
                elif  self.arr2d[i][j] == 1 :    
                    self.arr2dpb[i][j].setIcon(self.icon1) 
                elif  self.arr2d[i][j] == 2 :    
                    self.arr2dpb[i][j].setIcon(self.icon2)   

    def pb_click(self) :
        
                
        if self.end == False:
            return   
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        
        if self.arr2d[i][j] > 0 :
            return
        
        stone_info = 0
        if self.flag_wb :
            
            self.arr2d[i][j]=1
            stone_info = 1
        
        else:
            self.arr2d[i][j]=2
            stone_info = 2
            
        up = self.getUP(i,j,stone_info)
        dw = self.getDW(i,j,stone_info)
        le = self.getLE(i,j,stone_info)
        ri = self.getRI(i,j,stone_info)
         
        ur = self.getUR(i,j,stone_info)
        ul = self.getUL(i,j,stone_info)
        dr = self.getDR(i,j,stone_info)
        dl = self.getDL(i,j,stone_info)
        
        print("up:",up)
        print("dw:",dw)
        print("le:",le)
        print("ri:",ri)
         
        print("ur:",ur)
        print("ul:",ul)
        print("dr:",dr)
        print("dl:",dl)

            
        self.myrender()
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        if d1==5 or d2==5 or d3==5 or d4 == 5:
            if self.flag_wb:
                QMessageBox.about(self,"Omok","백돌이 이겼습니다.")
                self.end = not self.end
            else :
                QMessageBox.about(self,"Omok","흑돌이 이겼습니다.")
                self.end = not self.end   
             
        self.flag_wb = not self.flag_wb
                      
    
        
        
           
        
        
    def getUP(self,i,j,stone_info):
        cnt = 0
        while True:
            i -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt            
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
    def getDW(self,i,j,stone_info):
        cnt = 0
        while True:
            i += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getLE(self,i,j,stone_info):
        cnt = 0
        while True:
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getRI(self,i,j,stone_info):
        cnt = 0
        while True:
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getUR(self,i,j,stone_info):
        cnt = 0
        while True:
            i -= 1
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getUL(self,i,j,stone_info):
        cnt = 0
        while True:
            i -= 1
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getDL(self,i,j,stone_info):
        cnt = 0
        while True:
            i += 1
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
            
    def getDR(self,i,j,stone_info):
        cnt = 0
        while True:
            i += 1
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info :
                    cnt += 1
                else:
                    return cnt 
            except: 
                return cnt 
if __name__ == "__main__" :
   
    app = QApplication(sys.argv) 

  
    myWindow = WindowClass() 

  
    myWindow.show()

    app.exec_()
    
    
    
    
    
    
    
    