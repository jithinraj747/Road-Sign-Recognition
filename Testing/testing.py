import cv2
import numpy as np
from keras import models

# loading the model
model = models.load_model('road_sign_recognition')

# loading the label dictionary
label_dict = np.load('label_dict.npy',allow_pickle=True)
label_dict = label_dict.item()

cap = cv2.VideoCapture('Presentation1.mp4')
# cap = cv2.VideoCapture('traffic-sign-to-test.mp4')
cap.set(3,640)
cap.set(4,480)

img_size=100

while True:
    success, imgOriginal = cap.read()
    # image preprocessing
    img = np.asarray(imgOriginal)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

    imgCanny = cv2.Canny(imgBlur, 2, 2)
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    flag = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # to prevent area calculation of noise
            flag = True
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgOriginal, (x, y), (x + w, y + h), (0, 255, 0), 2)
            imgCropped = imgGray[y:y+h, x:x+w]
            imgResized = cv2.resize(imgCropped, (img_size, img_size))

    if flag == False:
        imgResized = cv2.resize(imgBlur, (img_size, img_size))

    imgOriginal = cv2.resize(imgOriginal,(640,480))
    imgResized = np.expand_dims(imgResized,axis=0)
    imgResized = np.expand_dims(imgResized, axis=3)
    imgResized = imgResized/255.0
    # model prediction
    pred_prob = model.predict(imgResized)
    pred_val = pred_prob.argmax(axis=1)
    if pred_prob[0].max()>=0.85:
        cv2.putText(imgOriginal,label_dict[pred_val[0]],(130,25),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3,cv2.LINE_AA)
        cv2.putText(imgOriginal,str(round(pred_prob[0].max()*100))+'%',(150,80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2,cv2.LINE_AA)
    cv2.imshow('Video: ', imgOriginal)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break