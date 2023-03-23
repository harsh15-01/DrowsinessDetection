import pandas as pd 
# import numpy as np 
import torch
import cv2
import tensorflow as tf
import imutils

torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('ultralytics/yolov5', 'yolov5s',  pretrained=True)
#loaded_model = tf.keras.models.load_model("D:\\Dev 2\\DrowsinessDetection\\ManualModel\\drowniness_stage1.h5")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    frame = imutils.resize(frame, width=450)
    # results2 = loaded_model(frame)
    # print(results2)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()