# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:36:26 2021

@author: pragy
"""
import cv2
# Reading the image
image = cv2.imread("hatch.jfif")
#Setting window size
cv2.namedWindow("HATCH :)",cv2.WINDOW_NORMAL)
cv2.resizeWindow("HATCH :)", 420, 630)
cv2.imshow("HATCH :)", image)
cv2.waitKey(0)
#Setting window size
cv2.namedWindow("Hatch go gray",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hatch go gray", 420, 630)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2GRAY,cv2.COLOR_RGB2BGR,cv2.COLOR_BGR2HSV
cv2.imshow("Hatch go gray", gray_image)
cv2.waitKey(0)
#Setting window size
cv2.namedWindow("Hatch trying inverted colors",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hatch trying inverted colors", 420, 630)
inverted_image = 255 - gray_image
cv2.imshow("Hatch trying inverted colors", inverted_image)
cv2.waitKey(0)
#Setting window size
cv2.namedWindow("Sketch",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Sketch", 420, 630)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
 # used for smoothing images
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch*25)
cv2.waitKey(0)
cv2.destroyAllWindows() 
#cv2.imshow("original image", image)
#cv2.imshow("pencil sketch", pencil_sketch)
#cv2.waitKey(0)
