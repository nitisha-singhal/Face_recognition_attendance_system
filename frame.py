import numpy as np
import cv2
import face_recognition
from PIL import Image

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
image = face_recognition.load_image_file('shrawan.jpeg')
face_locations1 = face_recognition.face_locations(image)
top, right, bottom, left = face_locations1[0]
face1 = image[top:bottom, left:right]
known_image = face1
biden_encoding = face_recognition.face_encodings(known_image)[0]

while(True):
    ret, frame = cap.read()
    face_locations = face_recognition.face_locations(frame)
    if (face_locations != []) :
        top, right, bottom, left = face_locations[0]
        unknown_image = frame[top:bottom, left:right]
        if (face_recognition.face_encodings(unknown_image) != []) :
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            print(results)
            print("done")
        cv2.imshow('frame', unknown_image)

    else :
        cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()