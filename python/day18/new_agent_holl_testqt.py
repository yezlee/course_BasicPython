import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
from collections import deque
from random import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys


COUNT = 50


def build_model():
	
	model = Sequential()
	model.add(Dense(10, input_dim = 1, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(10, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(2, activation = 'linear', kernel_initializer = 'he_uniform'))
	model.compile(loss = 'mse', optimizer = Adam(lr = 0.001))
	return model


form_class = uic.loadUiType("hj.ui")[0]
class WindowClass(QMainWindow, form_class) :
	def __init__(self) :
		self.score = 0
		self.arr_com = []
		self.seq = 0
		self.seq_end = COUNT
		
		super().__init__()
		self.setupUi(self)
		self.pb_holl.clicked.connect(self.pb_holl_clicked)
		self.pb_jjak.clicked.connect(self.pb_jjack_clicked)
     
	def pb_holl_clicked(self,mine) :
		self.myselect(0)
	def pb_jjack_clicked(self) :
		self.myselect(1)
	def myselect(self,mine):
		model = build_model()
		model.load_weights('save_model/mdl_origin.h5')
			
		mine = randint(0,1)

		numpy_mine = np.array([mine])
		numpy_mine = np.reshape(numpy_mine, [1, 1])
		numpy_mine = np.float32(numpy_mine)
		
		q_values = model.predict(numpy_mine)
		print(q_values)
		com = np.argmax(q_values[0])
	
			# 데이터 출력
		if mine == 0:
			self.le_mine.setText("홀")
		elif mine == 1:
			self.le_mine.setText("짝")
				
		if com == 0:
			self.le_com.setText("홀")
		elif com == 1:
			self.le_com.setText("짝")
				
		if mine == com :
			self.le_result.setText("승리")
			self.score += 1
		else:
			self.le_result.setText("패배")
			
		self.le_jumsu.setText(str(self.score))	
		self.le_seq.setText(str(self.seq))	
			
		self.seq += 1	

if __name__ == "__main__":
	app = QApplication(sys.argv) 
	myWindow = WindowClass() 
	myWindow.show()
	app.exec_()
	

# 	model = build_model()
# 	model.load_weights('save_model/mdl_origin.h5')
# 	
# 	model.summary()
# 
# 
# 	jumsu = 0
# # 	for i in range(50):
# 	mine = randint(0,1)
# 
# 	numpy_mine = np.array([mine])
# 	numpy_mine = np.reshape(numpy_mine, [1, 1])
# 
# 		# 인공지능의 출력을 받는다 
# 	numpy_mine = np.float32(numpy_mine)
# 	q_values = model.predict(numpy_mine)
# 	print(q_values)
# 	com = np.argmax(q_values[0])
# 
# 		# 데이터 출력
# 	if mine == 0:
# 		print('mine: 홀',end=" ")
# 	elif mine == 1:
# 		print('mine: 짝',end=" ")
# 			
# 	if com == 0:
# 		print('com: 홀',end=" ")
# 	elif com == 1:
# 		print('com: 짝',end=" ")
# 			
# 	if mine == com :
# 		jumsu+=1
# 	
# 	print("jumsu:",jumsu)
# 	
