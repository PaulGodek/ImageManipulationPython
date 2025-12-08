import cv2 as cv
import numpy as np

# Création d'une image de taille 512x256 (256 lignes et 512 colonnes)
# en niveau de gris (1 canal) codée à l'aide de float32 (np.float32)
# Les valeurs des pixels sont comprises entre 0 (noir) et 1 (blanc)
imgNG = np.zeros((256,512,1), np.float32)
for i in range(imgNG.shape[0]):
    for j in range(imgNG.shape[1]):            
        if (i // 16 + j // 16) % 2 == 0:
            imgNG[i, j] = 1
        else:
            imgNG[i, j] = 0
        
cv.imshow("Damier", imgNG)

cv.waitKey(0)
cv.destroyAllWindows()