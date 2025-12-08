import cv2 as cv
import numpy as np
import sys

pathToOutput = "output/"

pathToFile = "C:/Users/paulg/Pictures/Camera Roll/"
fileName = "WIN_20251202_16_31_39_Pro.jpg"
fileNameWithoutExtension = fileName.split(".")[0]
fileExtension = fileName.split(".")[1]

img = cv.imread(pathToFile + fileName)

if img is None:
    sys.exit("Impossible de lire l'image")

imgInvert = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
for i in range(imgInvert.shape[0]):
    for j in range(imgInvert.shape[1]):
        imgInvert[i, j, 0] = 255 - img[i, j, 0]
        imgInvert[i, j, 1] = 255 - img[i, j, 1]
        imgInvert[i, j, 2] = 255 - img[i, j, 2]


cv.imwrite(pathToOutput + fileNameWithoutExtension + "_inverted.jpg", imgInvert)


cv.imshow("Image de base", img)
cv.imshow("Image inversee", imgInvert)
cv.waitKey(0)