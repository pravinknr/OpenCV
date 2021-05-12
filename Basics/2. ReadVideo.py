# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:57:26 2021

@author: Pravin
"""

# Reading Videos

import cv2 as cv

capture = cv.VideoCapture('path of the Video')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
            
capture.release()
cv.destroyAllWindows()