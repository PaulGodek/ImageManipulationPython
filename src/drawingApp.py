import cv2
import colorsys as cs
import numpy as np

# Fonction pour mettre à jour les valeurs des sliders
def nothing(x):
    pass

# Création de la fenêtre pour les sliders
cv2.namedWindow("Sliders")
cv2.createTrackbar("Lower H", "Sliders", 70, 255, nothing)
cv2.createTrackbar("Lower S", "Sliders", 255, 255, nothing)
cv2.createTrackbar("Lower V", "Sliders", 100, 255, nothing)
cv2.createTrackbar("Upper H", "Sliders", 100, 255, nothing)
cv2.createTrackbar("Upper S", "Sliders", 255, 255, nothing)
cv2.createTrackbar("Upper V", "Sliders", 255, 255, nothing)

cv2.createTrackbar("Color for drawing", "Sliders", 255, 255, nothing)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")
else:
    print("Accès à la webcam !")

# Valeurs par défaut
canvas = None
old_point = None
ret = True

while ret:
    ret, frame = cap.read()
    if ret:
        # Initialiser le canvas si nécessaire
        if canvas is None:
            canvas = np.zeros_like(frame)

        # Lire les valeurs des sliders
        lower_h = cv2.getTrackbarPos("Lower H", "Sliders")
        lower_s = cv2.getTrackbarPos("Lower S", "Sliders")
        lower_v = cv2.getTrackbarPos("Lower V", "Sliders")
        upper_h = cv2.getTrackbarPos("Upper H", "Sliders")
        upper_s = cv2.getTrackbarPos("Upper S", "Sliders")
        upper_v = cv2.getTrackbarPos("Upper V", "Sliders")
        drawing_color = cv2.getTrackbarPos("Color for drawing", "Sliders")

        # Conversion en espace de couleur HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (5, 5), 0)

        # Définir la plage de couleurs à partir des sliders
        lower_bound = np.array([lower_h, lower_s, lower_v])
        upper_bound = np.array([upper_h, upper_s, upper_v])

        # Créer un masque pour les objets dans la plage de couleurs
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Trouver les contours des objets détectés
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Trouver le plus gros contour
            largest_contour = max(contours, key=cv2.contourArea)

            # Trouver le point le plus au nord-est
            northest_point = tuple(largest_contour[largest_contour[:, :, 0].argmax()][0])

            # Dessiner sur le canvas
            if old_point is None:
                old_point = northest_point
                
            new_color = cs.hsv_to_rgb(drawing_color/255, 1, 1)
            new_color = tuple(int(c * 255) for c in new_color)
                
            cv2.line(canvas, old_point, northest_point, new_color, 5)
            old_point = northest_point

        # Combiner le canvas avec le flux vidéo
        combined = cv2.add(frame, canvas) # L'addition rend la ligne un peu transparente mais tant pis

        # Afficher les différentes fenêtres
        cv2.imshow("Masque", mask)
        cv2.imshow("Dessin", combined)

        if cv2.waitKey(1) == 27:  # Echap pour quitter que je me trompe plus
            ret = False
    else:
        print("Erreur lors de la capture vidéo.")

cv2.destroyAllWindows()
cap.release()