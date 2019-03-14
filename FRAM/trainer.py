import cv2,os
import numpy as np
from PIL import Image 
import pymysql
def train():
    conn = pymysql.connect('localhost', 'root' ,'nithish24', 'Attendance')
    cur = conn.cursor()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascadePath = "data/haarcascade_frontalface_alt2.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    image_paths = []

    def paths_baba(path):
        for f in os.listdir(path):
            image_paths.append(os.path.join(path, f))


    def get_images_and_labels():
         #image_paths = []
         #image_paths = [os.path.join(path, f) for f in os.listdir(path)]
         #for f in os.listdir(path):
          #    image_paths.append(os.path.join(path, f))
         # images will contains face images
         images = []
         # labels will contains the label that is assigned to the image
         labels = []
         for image_path in image_paths:
             # Read the image and convert to grayscale
             image_pil = Image.open(image_path).convert('L')
             # Convert the image format into numpy array
             image = np.array(image_pil, 'uint8')
             # Get the label of the image
             nbr = os.path.split(image_path)[1].split(".")[0]
             #nbr=int(''.join(str(ord(c)) for c in nbr))
             print (nbr)
             query1 = "SELECT label FROM TRAINIMAGES WHERE USN = " + "'" + nbr + "';"
             cur.execute(query1)
             row = cur.fetchone()
             label = row[0]
             # Detect the face in the image
             faces = faceCascade.detectMultiScale(image)
             # If face is detected, append the face to images and the label to labels
             for (x, y, w, h) in faces:
                 images.append(image[y: y + h, x: x + w])
                 labels.append(label)
                 cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                 cv2.waitKey(10)
         # return the images list and labels list
         return images, labels

    query = "SELECT folderName FROM TRAINIMAGES"
    cur.execute(query)

    row = cur.fetchone()
    while row is not None:
        #print(row)
        paths_baba(row[0])
        row = cur.fetchone()
    images, labels = get_images_and_labels()
    cv2.imshow('test',images[0])
    cv2.waitKey(1)

    recognizer.train(images, np.array(labels))
    recognizer.write('trainer/trainer.yml')
    cv2.destroyAllWindows()
