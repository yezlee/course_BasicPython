import cv2

img = cv2.imread("4.png",cv2.IMREAD_GRAYSCALE)

img2 = cv2.resize(img,(28,28))

print(img2)
for i in img2:
    for j in i:
        if j >0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()



cv2.imshow("test image", img)
cv2.waitKey()

cv2.destroyAllWindows()



 
