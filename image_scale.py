import cv2
import cv2.cv as cv
import numpy as np
import scipy
import Image

filename = "image.bmp"

oriimage = cv2.imread(filename,0)
k=2
newx,newy = oriimage.shape[1]/k,oriimage.shape[0]/k #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imwrite("new.bmp",newimage)
# cv.SaveImage("new.jpg", newimage)
im = cv.LoadImage("new.bmp",0)
k*im.width
c = [[0]*k*im.width for i in range(k*im.height)]

# c[][]=[k*im.height][k*im.width]

# displaying the matrix form of image
# gray = cv2.cvtCOLOR(im, cv2.COLOR_BGR2GRAY)
# print gray
for i in range(im.height):
    for j in range(im.width):
    	# print im[i,j],
    	# if(i%2==0):
    	c[2*i][2*j]=im[i,j]
    	# print c[i][j],
    # print "\n",i,j,	
# Making  a cover image 
# Algo is to make a array of the original size say 
# 	h=k*im.height;
# 	l=k*im.width;
# then copy unchanged pixel of im array to array C;
# that is c[i`,j`]=im[i,j]; where i`=2*i,j`=2*j;

# for i in range()

# scipy.misc.imsave('outfile.jpg', image_array)

for i in range(k*im.height):
    for j in range(k*im.width):
    	print c[i][j],
    print "\n",i,

c_array=np.asarray(c)
ime = Image.fromarray(c_array)
if ime.mode != 'RGB':
    ime = ime.convert('RGB')
ime.save("your_file.bmp")

cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
cv2.waitKey(40)