import cv2 as cv
import numpy as np

def compute_histogram_ng(img, nb_classes):
    assert img.shape[2] == 3 # S'assure que l'image a bien 3 canaux de couleur
    
    if np.isdtype(img.dtype, 'unsigned integer'):
        max_intensity = np.iinfo(img.dtype).max
    elif np.isdtype(img.dtype, 'real floating'):
        max_intensity = 1.0
    else:
        raise ValueError("Type d'image non supporté pour l'histogramme.")
    
    # Calcule l'histogramme
    hist1 = cv.calcHist(images=[img], channels=[0], mask=None,
    histSize=[nb_classes], ranges=[0, max_intensity])
    hist2 = cv.calcHist(images=[img], channels=[1], mask=None,
    histSize=[nb_classes], ranges=[0, max_intensity])
    hist3 = cv.calcHist(images=[img], channels=[2], mask=None,
    histSize=[nb_classes], ranges=[0, max_intensity])
    
    # Normalise l'histogramme
    hist1 = cv.normalize(hist1, hist1).flatten()
    hist2 = cv.normalize(hist2, hist2).flatten()
    hist3 = cv.normalize(hist3, hist3).flatten()
    
    # Crée une image noire pour dessiner l'histogramme
    hauteur, largeur = 512, 1024
    img_hist = np.zeros((hauteur, largeur, 3), dtype=np.uint8)
    
    # Détermine la valeur maximale de l'histogramme
    max_val1 = hist1.max()
    max_val2 = hist2.max()
    max_val3 = hist3.max()
    
    # Valeur par défaut pour les points de base
    oldPR = (0, hauteur)
    oldPG = (0, hauteur)
    oldPB = (0, hauteur)
    
    for h in range(nb_classes):
        for k in range(3):
            # Calcule les coordonnées de la barre de l'histogramme
            match k:
                case 0:
                    p1 = oldPR
                    p2 = (int((h + 1) * largeur / nb_classes),
                    int(hauteur - (hist1[h] / max_val1 * hauteur)))
                    
                    # Dessine la ligne rouge
                    cv.line(img_hist, p1, p2, (255, 0, 0), 2)
                    
                    oldPR = p2
                    break
                case 1: 
                    p1 = oldPG
                    p2 = (int((h + 1) * largeur / nb_classes),
                    int(hauteur - (hist2[h] / max_val2 * hauteur)))
                    
                    # Dessine la ligne verte
                    cv.line(img_hist, p1, p2, (0, 255, 0), 2)
                    
                    oldPG = p2
                    break
                case _:
                    p1 = oldPB
                    p2 = (int((h + 1) * largeur / nb_classes),
                    int(hauteur - (hist3[h] / max_val3 * hauteur)))
                    
                    # Dessine la ligne bleue
                    cv.line(img_hist, p1, p2, (0, 0, 255), 2)
                    
                    oldPB = p2
                    break
            
            
        
    cv.imshow("Histogramme des couleurs", img_hist)


img = cv.imread("C:/Users/paulg/Pictures/Camera Roll/WIN_20251202_16_31_39_Pro.jpg")

cv.imshow("Image d'origine", img)
compute_histogram_ng(img, 10)

cv.waitKey(0)
cv.destroyAllWindows()