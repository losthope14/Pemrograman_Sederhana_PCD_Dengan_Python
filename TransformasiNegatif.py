import cv2

img = cv2.imread('images/mammogram.jpg')

img_1 = 255 -  img

cv2.imshow('Gambar Original', img)
cv2.imshow('Citra Negatif', img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()