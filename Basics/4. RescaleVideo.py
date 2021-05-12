# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:19:15 2021

@author: Pravin
"""

import cv2 as cv



def rescaleFrame(frame, scale = 0.72):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('path of the Video')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Rescaled Video', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
            
capture.release()
cv.destroyAllWindows()