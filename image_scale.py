def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

import cv2
import cv2.cv as cv
import numpy as np
import scipy
import Image
import math
filename = "image.bmp"
zero=0
info="i am kokab"
steg=tobits(info)
l=len(steg)
o=frombits(steg)
oriimage = cv2.imread(filename,0)
k=2
newx,newy = oriimage.shape[1]/k,oriimage.shape[0]/k #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imwrite("new.bmp",newimage)
# cv.SaveImage("new.jpg", newimage)
im = cv.LoadImage("new.bmp",0)
k*im.width
c = [[0]*k*im.width for i in range(k*im.height)]
s = [[0]*k*im.width for i in range(k*im.height)]

# c[][]=[k*im.height][k*im.width]

# displaying the matrix form of image
# gray = cv2.cvtCOLOR(im, cv2.COLOR_BGR2GRAY)
# print gray

# /********************************************************************************************************88

#                             MAKING COVER IMAGE

# /***********************************************************************************************************/
for i in range(im.height):
    for j in range(im.width):
    	# print im[i,j],
    	# if(i%2==0):
    	s[2*i][2*j]=c[2*i][2*j]=im[i,j]
    	# print c[i][j],
    # print "\n",i,j,	
print i,j
# Making  a cover image 
# Algo is to make a array of the original size say 
# 	h=k*im.height;
# 	l=k*im.width;
# then copy unchanged pixel of im array to array C;
# that is c[i`,j`]=im[i,j]; where i`=2*i,j`=2*j;

# for i in range()
b1=b2=b3=0

# scipy.misc.imsave('outfile.jpg', image_array)

# /*********************************************************************************************************/

#                         MAKING COVER IMAGE AS WELL AS STEGO IMAGE

# /********************************************************************************************************/
counter=0
for i in range(0,(k*im.height)-2,2):
    for j in range(0,(k*im.width)-2,2):
    	# print c[i][j],
    	Imin=c[i][j]
    	Imax=c[i][j]
    	L=[c[i+2][j+2],c[i+2][j],c[i][j+2]];

    	for item in L:
    		if(Imin>item):
    			Imin=item
    		if(Imax<item):
    			Imax=item
    	
    		

    	AD=(3*Imin+Imax)/4
    	c[i][j+1]=AD + (c[i][j]+c[i][j+2])/4
    	c[i+1][j]=AD + (c[i][j]+c[i+2][j])/4
    	c[i+1][j+1]=(c[i][j]+c[i+1][j]+c[i][j+1])/3
    	d1=Imax-c[i][j+1]if c[i][j+1]<(Imin+Imax)/2 else c[i][j+1]-Imin
    	d2=Imax-c[i+1][j]if c[i+1][j]<(Imin+Imax)/2 else c[i+1][j]-Imin
    	d3=Imax-c[i+1][j+1]if c[i+1][j+1]<(Imin+Imax)/2 else c[i+1][j+1]-Imin
    	n1=int(math.floor(math.log(d1,2)))
    	n2=int(math.floor(math.log(d2,2)))
    	n3=int(math.floor(math.log(d3,2)))
    	# for ind in range(counter,counter+n1):
    	# 	b1=b1+steg[ind]*pow(2,n1-ind-1)
    	# counter+=n1
    	# for ind in range(counter,counter+n2):
    	# 	b2=b2+steg[ind]*pow(2,n2-ind-1)
    	# counter+=n2
    	# for ind in range(counter,counter+n3):
    	# 	b3=b3+steg[ind]*pow(2,n3-ind-1)
    	# counter+=n3
     # 	counter+=(counter+n1+n2+n3)
      # s[i][j]=
      # s[i][j+1]=
      # s[i+1][j]=
      # s[i+1][j+]=
    	# j+=2

    # print "\n",i,
    # i+=2
print n1,n2,n3
# print steg
print l
print steg[0:3]



# /********************************************************************************************************/

#                         CHECKING NO OF ZERO IN STEGO IMAGE

# /*********************************************************************************************************/
# print "\n",o


for i in range(k*im.height):
    for j in range(k*im.width):
        if(c[i][j]==0):
            zero=zero+1
            # print i,j
        print c[i][j] ,
    print "\n"

print zero
c_array=np.asarray(c)
ime = Image.fromarray(c_array)
if ime.mode != 'RGB':
    ime = ime.convert('RGB')
ime.save("your_file.bmp")

cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
cv2.waitKey(400)