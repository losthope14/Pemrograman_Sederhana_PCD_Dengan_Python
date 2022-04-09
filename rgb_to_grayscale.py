import cv2

img = cv2.imread('images/Lenna.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('Gambar Lenna Original', img)
cv2.imshow('Gambar Lenna Grayscale', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()