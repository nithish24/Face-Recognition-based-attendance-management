
import numpy as np
import cv2
import datetime
import pymysql

def upload_photo(secID, subID, hour):
    conn = pymysql.connect('localhost', 'root', 'nithish24', 'attendance')
    cur = conn.cursor()
    date = datetime.date.today()
    imgPath = "classPhoto/"+str(date)+str(secID)+str(subID)+str(hour)+".jpg"
    cam = cv2.VideoCapture(0)
    while True:
        red, im = cam.read()
        cv2.imshow("PRESS c TO CAPTURE", im)
        if(cv2.waitKey(1) & 0xFF == ord('c')):
            break
    
    cv2.imwrite(imgPath, im)
    del(cam)
    cv2.destroyAllWindows()

    query = "INSERT INTO CLASSPHOTO(imgPath, sectionID, subjectID, date_, hour) VALUES ('" + imgPath +"', '"+ str(secID) +"', '"+ str(subID) +"', '"+ str(date) +"', '"+ str(hour) + "')"
    cur.execute(query)
    conn.commit()
    

