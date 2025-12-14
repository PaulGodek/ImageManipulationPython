import cv2

img = cv2.imread("src/img.jpg")
img_ng = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image niveau gris',img_ng)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()