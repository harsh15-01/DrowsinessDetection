from scipy.spatial import distance as dist 
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread 
from keras import models
import numpy as np
import playsound
import argparse
import imutils
import time
# import dlib 
import cv2

model = models.load_model('C:\\Users\\Spyder\\Dev\\DrowsinessDetection\\ManualModel\\drowniness_stage1.h5')
                            #    include_top=False, input_tensor=(shape=(256,256,3)) )

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    # cv2.imshow('Arnav Randi', np.squeeze(results.render()))
    cv2.imshow('Arnav Randi', results)
    # image = cv2.resize(image, (480, 640))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()