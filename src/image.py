import cv2
import sys

img = cv2.imread("src/img.jpg")

if img is None:
    sys.exit("Impossible de lire l'image")
    
cv2.imshow("PAUL", img)
cv2.waitKey(0)