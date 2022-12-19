import cv2 
import numpy as np
import mediapipe as mp
import time


cap =cv2.VideoCapture(1)
while True:
    success, img = cap.read()


    cv2.imshow("image",img)
    cv2.waitKey(1)
    
    