import cv2 as cv
import numpy as np

# Création d'une image de taille 512x256 (256 lignes et 512 colonnes)
# en niveau de gris (1 canal) codée à l'aide de float (np.float32)
# Les valeurs des pixels sont comprises entre 0 (noir) et 1 (blanc)
imgNG = np.zeros((256,512,1), np.float32)
for i in range(imgNG.shape[0]):
    for j in range(imgNG.shape[1]):
        # A votre avis, que dessine le code suivant ?
        imgNG[i, j] = (np.cos((i + j) / 512.0 * 6.28 * 10.0) + 1.0) / 2.0
        
cv.imshow("Image en niveaux de gris", imgNG)

# Création d'une image de taille 512x256 (256 lignes et 512 colonnes)
# en couleur (3 canaux) codée à l'aide d'unsigned char (np.uint8)
# Les valeurs des composantes sont comprises entre 0 (noir) et 255 (blanc)
imgCoul = np.zeros((256, 512, 3), np.uint8)
for i in range(imgCoul.shape[0]):
    for j in range(imgCoul.shape[1]):
        # Composante Bleu :
        imgCoul[i, j, 0] = int((np.cos((i + j) / 512.0 * 6.28 * 10.0) + 1.0) * 127)
        # Composante Vert :
        imgCoul[i, j, 1] = int((np.cos((i + j) / 512.0 * 6.28 * 5.0) + 1.0) * 127)
        # Composante Rouge :
        imgCoul[i, j, 2] = int((np.cos((i + j) / 512.0 * 6.28 * 2.5) + 1.0) * 127)
        
cv.imshow("Image en couleur", imgCoul)
cv.waitKey(0)
cv.destroyAllWindows()