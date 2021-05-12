# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:24:55 2021

@author: Pravin
"""

import cv2 as cv

img = cv.imread('E:\OpenCV\Photos\Pikachu.jpg')



def rescaleFrame(frame, scale = 0.72):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)


cv.imshow('Pikachu', img) #('Name for the window', Image)

cv.imshow('Resized Image', resized_image)

cv.waitKey(0)