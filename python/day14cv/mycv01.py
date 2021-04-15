import cv2
 
img = cv2.imread('rgb.png', 1)


print(img)
# img[0][0][0] = 255
# img[0][0][1] = 255
# img[0][0][2] = 255
# 
# img[0][1][0] = 255
# img[0][1][1] = 255
# img[0][1][2] = 255
# 
# img[1][0][0] = 255
# img[1][0][1] = 255
# img[1][0][2] = 255
# 
# img[1][1][0] = 255
# img[1][1][1] = 255
# img[1][1][2] = 255

print(img[0][0][0])
print('shape:',img.shape)

cv2.imshow('Test Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
 
