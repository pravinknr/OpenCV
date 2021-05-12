# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:42:27 2021

@author: Pravin
"""



import cv2 as cv

img = cv.imread('E:\OpenCV\Photos\Pikachu.jpg')

cv.imshow('Pikachu', img) #('Name for the window', Image)

cv.waitKey(0)



