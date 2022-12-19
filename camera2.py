import cv2


cap = cv2.VideoCapture(0)
#Kamera aygıtına bağlanılabildi mi?
while(cap.isOpened()):
#Görüntüyü oku ve görüntüle
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()