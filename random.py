from scipy.spatial import distance as dist 
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread 
import numpy as np
import playsound
import argparse
import imutils
import time
# import dlib 
import cv2

vs = VideoStream(0).start()
time.sleep(1.0)

while True:
    frame = vs.read()    
    # frame = imutils.resize(frame, width=450)
    # (h, w) = frame.shape[:2]

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
