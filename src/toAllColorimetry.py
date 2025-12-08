import cv2
import numpy as np

# Function to convert RGB to CMYK
def rgb_to_cmyk(img):
    # Allocate CMYK components
    cmyk = [np.zeros(img.shape[:2], dtype=np.uint8) for _ in range(4)]

    # Split the image into RGB channels
    b, g, r = cv2.split(img)

    # Normalize RGB values to [0, 1]
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # Compute K channel
    k = 1 - np.maximum(np.maximum(r, g), b)

    # Avoid division by zero
    k_safe = np.where(k < 1, k, 1)

    # Compute C, M, Y channels
    cmyk[0] = ((1 - r - k_safe) / (1 - k_safe) * 255).astype(np.uint8)
    cmyk[1] = ((1 - g - k_safe) / (1 - k_safe) * 255).astype(np.uint8)
    cmyk[2] = ((1 - b - k_safe) / (1 - k_safe) * 255).astype(np.uint8)
    cmyk[3] = (k * 255).astype(np.uint8)

    return cmyk


img = cv2.imread("C:/Users/paulg/Pictures/Camera Roll/WIN_20251202_16_31_39_Pro.jpg")

img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_YUV = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_CieLab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
img_CMYK = rgb_to_cmyk(img_RGB)
img_XYZ = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)



cv2.imshow("Image originale", img)
cv2.imshow("Image en RGB", img_RGB)
cv2.imshow("Image en HSV", img_HSV)
cv2.imshow("Image en YUV", img_YUV)
cv2.imshow("Image en Cie-Lab", img_CieLab)

#cv2.imshow("Image en CMYK", img_CMYK)

# Comme on a pas de convertisseur CMYK natif, j'en ai un manuel
# mais il ne permet d'afficher que les couleurs individuelles 
# (Je n'ai pas réussi à merge les couleurs)
cv2.imshow("CMYK Cyan", img_CMYK[0])
cv2.imshow("CMYK Magenta", img_CMYK[1])
cv2.imshow("CMYK Yellow", img_CMYK[2])
cv2.imshow("CMYK Black", img_CMYK[3])

cv2.imshow("Image en XYZ", img_XYZ)

cv2.waitKey(0)
cv2.destroyAllWindows()