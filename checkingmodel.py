import tensorflow as tf
import cv2
import os
import matplotlib.pyplot as plt 
import numpy as np

new_model = tf.keras.models.load_model("ManualModel//drowniness_Stage1.h5")

img_size = 256
img_array = cv2.imread("C:\\Users\\Spyder\\Dev\\Train_Dataset\\mrlEyes_2018_01\\open_eyes\\s0001_02944_0_1_1_2_0_01.png", cv2.IMREAD_GRAYSCALE)
backtorgb = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
new_array = cv2.resize(backtorgb, (img_size, img_size))
x_input = np.array(new_array).reshape(-1,img_size, img_size, 3)
prediction = new_model.predict(x_input)
print(prediction)