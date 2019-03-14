import cv2,os
import numpy as np


def face_recognize(imgPath):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "data/haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    path = 'dataSet'
    ids = []

    im = cv2.imread(imgPath)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        ids.append(nbr_predicted)
    print(ids)
    return ids








