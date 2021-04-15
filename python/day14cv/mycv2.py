import cv2

img = cv2.imread("0.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img)
print("shpae:",img.shape)

cv2.imshow("cat", img)
cv2.imshow("gray_cat", gray_img)

cv2.waitKey()



 
