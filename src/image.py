import cv2
import sys

img = cv2.imread("C:/Users/paulg/Pictures/Camera Roll/WIN_20251202_16_31_39_Pro.jpg")

if img is None:
    sys.exit("Impossible de lire l'image")
    
cv2.imshow("PAUL", img)
cv2.waitKey(0)