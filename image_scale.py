def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '0000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 7):
        byte = bits[b*7:(b+1)*7]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

import cv2
import cv2.cv as cv
import numpy as np
import scipy
import Image
import math
filename = "ipimage1.bmp"
zero=0
count=0
info="hell##"
# /******************************************************************************************************************


#                         READING A SECRET INFORMATION

# /*******************************************************************************************************************
# infoimage=cv.LoadImage("new.jpg",0)
# info_str=[]
# info_array=np.asarray(infoimage[:,:])

# for i in range(infoimage.height):
#     for j in range(infoimage.width):
#         info_str.extend(bin(info_array[i,j])[2:]),
#     # print "\n"
# # print info_array
# # Converting info_str into integer list
# for i in range(len(info_str)):
#     info_str[i]=int(info_str[i])
#     # print info_str[i]
# ig_str = cv2.imencode('.jpg', info_array)[1].tostring()
# # T2 = [map(int, x) for x in ig_str]
# print "info imafge"
# print type(ig_str)
# print info_str
# steg=strinfo = ''.join(info_str)
# image reading steg=info_str
# print info_str
# print strinfo
steg=tobits(info)
l=len(steg)

oriimage = cv2.imread(filename,0)
k=2
newx,newy = oriimage.shape[1]/k,oriimage.shape[0]/k #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imwrite("scaledim.bmp",newimage)
# cv.SaveImage("new.jpg", newimage)
im = cv.LoadImage("scaledim.bmp",0)
k*im.width
print "h",im.width
print k*im.width
c = [[0]*(k*im.width-1) for i in range(k*im.height-1)]
s = [[0]*(k*im.width-1) for i in range(k*im.height-1)]
print k*im.width-1,k*im.height-1
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
    	# print im[i,j],
    # print "\n",i,j,	
print i,j
for i in range(1,k*im.height-1,2):
    s[i][k*im.width-2]=c[i][k*im.width-2]=round((s[i-1][k*im.width-2]+s[i+1][k*im.width-2])/2)
for i in range(1,k*im.width-1,2):
    s[k*im.height-2][i]=c[k*im.height-2][i]=(round(s[k*im.width-2][i-1]+s[k*im.width-2][i+1])/2)
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
count21=0
count=0
for i in range(0,(k*im.height-2),2):
    for j in range(0,(k*im.width-2),2):
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

    	s[i][j+1]=c[i][j+1]=round((AD + (c[i][j]+c[i][j+2])/2)/2)
    	s[i+1][j]=c[i+1][j]=round((AD + (c[i][j]+c[i+2][j])/2)/2)
    	s[i+1][j+1]=c[i+1][j+1]=round((c[i][j]+c[i+1][j]+c[i][j+1])/3)
    	d1=Imax-c[i][j+1]if c[i][j+1]<(Imin+Imax)/2 else c[i][j+1]-Imin
    	d2=Imax-c[i+1][j]if c[i+1][j]<(Imin+Imax)/2 else c[i+1][j]-Imin
    	d3=Imax-c[i+1][j+1]if c[i+1][j+1]<(Imin+Imax)/2 else c[i+1][j+1]-Imin
        # print Imin,Imax,c[i][j+1],c[i+1][j],c[i+1][j+1],d1,d2,d3

    #/****************************************************************************************************/

     #                        GENERATING STEGO IMAGE

    #/***********************************************************************************************/
        flag=0
        if(count<l):
    	   n1=int(math.floor(math.log(d1,2)))
           if(n1!=0):
                count21=count21+1
                start=count
                count= count+n1 if(l>count+n1) else l
                print "n1",count-start
                b1=bina=0
                
              # embed
                for kokab in range(count-1,start-1,-1):
                    # print i,j+1
                    b1=pow(2,bina)*steg[kokab]+b1
                    bina=bina+1
                print "b1",b1,c[i][j+1],s[i+1][j+1]
                s[i][j+1]=s[i][j+1]-b1
             
        if(count<l):
            n2=int(math.floor(math.log(d2,2)))
            if(count<l and n2!=0):
                count21=count21+1
                start=count
                count= count+n2 if(l>count+n2) else l
                print "d2",d2,"n2",count-start
                b2=bina=0
                for kokab in range(count-1,start-1,-1):
                    # print i+1,j
                    # print kokab
                    b2=pow(2,bina)*steg[kokab]+b2
                    bina=bina+1
                print "b2",b2,c[i+1][j],s[i+1][j]
                s[i+1][j]=s[i+1][j]-b2
        # print "d1",d1
        if(count<l):
            n3=int(math.floor(math.log(d3,2)))
            if(count<l and n3!=0):
                start=count
                count=count+n3 if(l>count+n3) else l
                count21=count21+1
                print "n3",count-start
                b3=bina=0
                for kokab in range(count-1,start-1,-1):
                    # print i+1,j+1
                    b3=pow(2,bina)*steg[kokab]+b3
                    bina=bina+1
                print "b3",b3,c[i+1][j+1],s[i+1][j+1]
                s[i+1][j+1]=s[i+1][j+1]-b3
# print n1,n2,n3

c_array=np.asarray(c)
s_array=np.asarray(s)



print "No of pixels getting changed actually",count21,count

# /********************************************************************************************************/

#                         CHECKING NO OF ZERO IN STEGO IMAGE

# /*********************************************************************************************************/
# print "\n",o
zero=0
zero2=0
different=0
for i in range(k*im.height-1):
    for j in range(k*im.width-1):
        if(c[i][j]<=1):
            zero=zero+1
        if(s[i][j]<=1):
            zero2=zero2+1
        if(c[i][j]!=s[i][j]):
            # print i,j,c[i][j],s[i][j]
            different=different+1
        # print c[i][j],
        # print s_array[i,j],
        # print oriimage[i][j],
    # print "\n"
# print i,j
# /*******************************************************************************************************************
    
#                                                 TESTING OPERATION

# /*******************************************************************************************************************
print "No of zeo in cover image",zero
print "len of string",l,"type of l",type(steg)
print "No of zero in stego image",zero2
print "value of count",count
print "different no of pixels in cover and stego", different
if(count>=l):
    print "stego image successfully generated"
else:
    print "Unsuccessful stego"


# /********************************************************************************************************

#                                     SAVING THE IMAGE


# /********************************************************************************************************
cv2.imwrite("stego_image.bmp",s_array);
cv2.imwrite("cover_image.bmp",c_array);

# import scipy.misc
# scipy.misc.imsave("cover_image.bmp",c)
# scipy.misc.imsave("stego_image.bmp",s)


# cover=cv.LoadImage("cover_image.bmp",0)
# count=0
# zero=0
# for i in range(cover.height):
#   for j in range(cover.width):
#     if(cover[i,j]!=c[i][j]):
#       count=count+1
#     if(cover[i,j]==0):
#         zero=zero+1
#         print i,j
# print "Actual Count and zero",count,zero

# ime = Image.fromarray(c_array)
# if ime.mode != 'RGB':
#     ime = ime.convert('RGB')
# ime.save("your_file.bmp")


# s=cv.LoadImage("your_stego.bmp",0)
# c=cv.LoadImage("your_file.bmp",0)
# count=0
# for i in range(c.height):
#   for j in range(c.width):
#     if(s_array[i,j]!=c[i,j]):
#       count=count+1
# print "count", count


# imgs = Image.fromarray(s_array)
# if imgs.mode != 'RGB':
#     imgs = ime.convert('RGB')
# imgs.save("your_stego.bmp")

# s=cv.LoadImage("your_stego.bmp",0)
# c=cv.LoadImage("your_file.bmp",0)
# count=0
# for i in range(s.height):
#   for j in range(s.width):
#     if(s[i,j]!=c[i,j]):
#       count=count+1
# print count
print c[508][480],c[509][481],c[510][484]
print 'succ'
# cv2.imshow("original image",oriimage)
# cv2.imshow("resize image",newimage)
# cv2.imshow("hello","your_stego.bmp")
print 'error'
print steg
print frombits(steg)
cv2.waitKey(40000)