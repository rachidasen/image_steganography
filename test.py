import cv2
import cv2.cv as cv
import numpy as np
import scipy
import Image
import math

s=cv.LoadImage("test.bmp",0)
c=cv.LoadImage("cover_image.bmp",0)
count=0
print "s.height",s.height,s.width
print "c info",c.width,c.height

zero=0
for i in range(s.height):
  for j in range(s.width):
    if(s[i,j]!=c[i,j]):
      count=count+1
    if(s[i,j]==0):
    	zero=zero+1
    if(c[i,j]==0):
    	print i,j
print count
print zero


