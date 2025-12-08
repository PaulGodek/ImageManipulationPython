import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: pas accès à la webcam.")
else:
    print("Accès à la webcam !")
    
ret = True
while ret:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("image capturee", frame)
        if cv2.waitKey(1) == 27:
            ret = False
    else:
        print("Erreur .")
    
cv2.destroyAllWindows()
cap.release()   