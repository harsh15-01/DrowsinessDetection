from scipy.spatial import distance as dist 
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread 
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib 
import cv2

def sound_alarm(path):
    playsound.playsound(path)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.eculidean(eyes[2], eye[4])

    C = dist.eculidean(eye[0], eye[3])

    ear = (A+B)/(2.0*C)

    return ear

ap = argparse.ArgumentParser()
ap.add_argument("-p","--shape-predictor", required=True, help="path to facial landmark predictor")
ap.add_argument("-a","--alarm", type=str, default="", help="path alarm .WAV file")
#ap.add_argument("-w","--webcam", type=int, default=0, help="index of webcam on system")
args = vars(ap.parse_args())

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 48

COUNTER=0
ALARM_ON = False

print("[info] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

print("[info] starting video stream thread.....")
vs = VideoStream(0).start() #change to argse when using external webcam
time.sleep(1.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray,0)

    for rect in rects:

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR+rightEAR)/2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convesHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0,255,0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1,(0,255,0), 1)
        

