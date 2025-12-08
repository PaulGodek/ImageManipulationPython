import cv2 as cv
import numpy as np

def compute_histogram_ng(img, nb_classes):
    assert len(img.shape) == 2 # S'assure que l'image est en niveaux de gris
    
    if np.isdtype(img.dtype, 'unsigned integer'):
        max_intensity = np.iinfo(img.dtype).max
    elif np.isdtype(img.dtype, 'real floating'):
        max_intensity = 1.0
    else:
        raise ValueError("Type d'image non supporté pour l'histogramme.")
    
    # Calcule l'histogramme
    hist = cv.calcHist(images=[img], channels=[0], mask=None,
    histSize=[nb_classes], ranges=[0, max_intensity])
    
    # Normalise l'histogramme
    hist = cv.normalize(hist, hist).flatten()
    
    # Crée une image noire pour dessiner l'histogramme
    hauteur, largeur = 512, 1024
    img_hist = np.zeros((hauteur, largeur), dtype=np.uint8)
    
    # Détermine la valeur maximale de l'histogramme
    max_val = hist.max()
    
    for h in range(nb_classes):
        # Calcule les coordonnées de la barre de l'histogramme
        p1 = (int(h * largeur / nb_classes), hauteur)
        p2 = (int((h + 1) * largeur / nb_classes),
        int(hauteur - (hist[h] / max_val * hauteur)))
        
        # Dessine le rectangle rempli en blanc
        cv.rectangle(img_hist, p1, p2, (255), -1)
        
        # Dessine le contour du rectangle en gris
        cv.rectangle(img_hist, p1, p2, (127), 1)
        
    cv.imshow("Histogramme des niveaux de gris", img_hist)


img = cv.imread("C:/Users/paulg/Pictures/Camera Roll/WIN_20251202_16_31_39_Pro.jpg")
img_ng = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Image en gris", img_ng)
compute_histogram_ng(img_ng, 1000)

cv.waitKey(0)
cv.destroyAllWindows()