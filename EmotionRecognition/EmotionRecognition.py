#IMPORTS
import cv2 as cv
import argparse
import numpy as np
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image

import os
#Removing the output logs of tensorflow
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'



#FUNCTIONS
def detect_and_display(frame, classifier, emotion_labels):
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_frame = cv.equalizeHist(gray_frame)

    faces = face_cascade.detectMultiScale(gray_frame)

    for (x,y,w,h) in faces:
        frame = cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray_frame[y : y + h, x : x + w]
        roi_gray = cv.resize(roi_gray, (48, 48), interpolation = cv.INTER_AREA)

        
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis = 0)

            prediction = classifier.predict(roi)[0]
            label = emotion_labels[prediction.argmax()]
            label_position = (x, y)
            
            cv.putText(frame, label, label_position, cv.FONT_HERSHEY_SIMPLEX,1,(0,255,255), 2)

        else:
            
            cv.putText(frame,'No Faces',(30,80),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        
    cv.imshow('Capture - Face detection', frame)


#Argument Parser to organize the arguments required
parser = argparse.ArgumentParser()
parser.add_argument('--face_cascade', help = 'Path to face cascade', default="haarcascade_frontalface_alt.xml")
parser.add_argument('--camera', help = 'Camera divide number', type = int, default = 0)
args = parser.parse_args()

#Face Cascading
face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('Error')
    exit(0)

#Video Capturing
camera_device = args.camera
cap = cv.VideoCapture(camera_device)

#Model loading
classifier = load_model("model.h5")
emotion_labels = ['Angry', '', 'Fear', 'Happy','Neutral', 'Sad', 'Surprise']


#Reading captured video and invoking the detection function
while True:
    ret, frame = cap.read()
    if frame is None:
        print('No camera')
        break
    
    flipped_frame = cv.flip(frame, 1)
    detect_and_display(flipped_frame, classifier, emotion_labels)

    if cv.waitKey(1) == ord('q'):
        break

#Releasing the Video Capture object
cap.release()
cv.destroyAllWindows()


