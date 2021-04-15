import cv2
 
img = cv2.imread('0.jpg', 1)

print(img)

print(img[0][0][0])
print('shape:',img.shape)

for i in img:
    for j in i:
        j[0] = 0
        j[1] = 0

cv2.imshow('Test Image', img)
cv2.imwrite('test2.jpg',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
 
