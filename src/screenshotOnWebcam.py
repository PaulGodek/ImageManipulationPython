import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")
else:
    print("Accès à la webcam !")
    
ret, frame = cap.read()

if ret:
    cv2.imshow("image capturee", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erreur .")
    
cap.release()   