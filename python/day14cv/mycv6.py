import numpy as np
import cv2
from matplotlib import pyplot as plt


image = cv2.imread('bts.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

xml = 'frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)
faces = face_cascade.detectMultiScale(gray, 1.5, 2)

print("Number of faces detected: " + str(len(faces)))

if len(faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
cv2.imwrite('test2.jpg',image)
plt.xticks([]), plt.yticks([]) 
plt.show()