import cvzone
from cvzone.ColorModule import ColorFinder
import cv2
import socket

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

success, img = cap.read()
h, w, _ = img.shape

myColorFinder = ColorFinder(False)
# Passer ColorFinder en True pour pouvoir set la couleur correctement en copiant collant ici-bas les valeurs HSV
hsvVals = {'hmin': 75, 'smin': 0, 'vmin': 0, 'hmax': 99, 'smax': 255, 'vmax': 255}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5053) # Changer le port si celui-ci ne fonctionne pas

while True:
    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img, hsvVals)
    imgContour, contours = cvzone.findContours(img, mask) # Récupération des contours

    if contours:
        data = contours[0]['center'][0], \
               h - contours[0]['center'][1], \
               int(contours[0]['area']) 
        print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort) # Envoi des données au serveur

    imgContour = cv2.resize(imgContour, (0, 0), None, 0.5, 0.5)
    cv2.imshow("ImageContour", imgContour) # Affichage de l'image avec les contours

    if cv2.waitKey(1) == 27:  # Echap pour quitter que je me trompe plus
        break