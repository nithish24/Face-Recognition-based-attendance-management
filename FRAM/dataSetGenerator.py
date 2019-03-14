import cv2
import pymysql
import os

def create_training_data(USN, secID): 
    cam = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('Classifiers/face.xml')
    i=0
    offset=50
    conn = pymysql.connect('localhost', 'root', 'nithish24', 'Attendance')
    cur = conn.cursor()
    path_image = "dataSet/"+USN
    os.mkdir(path_image)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            i=i+1
            cv2.imwrite("dataSet/"+USN+"/"+USN+'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.waitKey(100)
        if i>20:
            cam.release()
            cv2.destroyAllWindows()
            break
    folderPath = "dataSet/"+USN
    query = "INSERT INTO TRAINIMAGES (USN, sectionID, folderName) VALUES('" + USN +"', '"+ secID +"', '"+ folderPath + "');" 

    cur.execute(query)
    conn.commit()
