import tensorflow as tf
import cv2
from tensorflow.python.keras.models import load_model
import numpy as np

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

img = cv2.imread('image/shoes.jpg', cv2.IMREAD_GRAYSCALE)
img2 = 1-cv2.resize(img, (28, 28))
img3 = (img2.reshape((1, 28 * 28))/255)

for i in img3 :
      
    for j in i :
        if j > 30:
            print("0",end=" ")
        else :
            print(" ",end=" ")
    print("")


model = load_model("mymodel")

img_np = model.predict(img3)
index = np.argmax(img_np[0])

print("---------------------------------------------------")
print(img3)
print("---------------------------------------------------")
print(img_np)
print("---------------------------------------------------") 
print(index)
print("---------------------------------------------------") 
