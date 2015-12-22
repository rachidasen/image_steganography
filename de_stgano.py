def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def padding(num, pad):
    while len(num) < pad:
        num = '0' + num
    return num

def reverse(num):
    i = len(num) - 1
    x = ""
    while i >= 0:
        x += num[i]
        i -= 1
    return x

def d2b(dec):
    b = ""
    while dec:
        b += str(dec%2)
        dec /= 2
    b = reverse(b)
    # b = padding(b,5)
    # print(b)        
    return b



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

s=cv.LoadImage("stego_image.bmp",0)

# s=np.asarray(infoimage[:,:])
print s.width, s.height
c = [[0]*s.width for i in range(s.height)]
i=j=0
# l=80
cover=cv.LoadImage("cover_image.bmp",0)
zero=count=0
zero2=0
for i in range(s.height):
  for j in range(s.width):
    if(s[i,j]!=cover[i,j]):
      count=count+1
    if(s[i,j]==0):
        zero=zero+1
        print i,j
    if(cover[i,j]==0):
        zero2=zero2+1

print "diff pixel",count
print "zero",zero,zero2
for i in range(0,s.height,2):
  for j in range(0,s.width,2):
    c[i][j]=s[i,j]

for i in range(1,s.height,2):
    c[i][s.width-1]=(c[i-1][s.width-1]+c[i+1][s.width-1])/2
for i in range(1,s.width,2):
    c[s.height-1][i]=(c[s.height-1][i-1]+c[s.height-1][i+1])/2


# /***************************************************************************************************************/

#                 EXTRACTING information from stego image

# /***************************************************************************************************************/

# count=l

for i in range(0,(s.height-1),2):
    for j in range(0,(s.width-1),2):
        Imin=c[i][j]
        Imax=c[i][j]
        L=[c[i+2][j+2],c[i+2][j],c[i][j+2]];

        for item in L:
            if(Imin>item):
                Imin=item
            if(Imax<item):
                Imax=item
        
        AD=(3*Imin+Imax)/4

        c[i][j+1]=(AD + (c[i][j]+c[i][j+2])/2)/2
        c[i+1][j]=(AD + (c[i][j]+c[i+2][j])/2)/2
        c[i+1][j+1]=(c[i][j]+c[i+1][j]+c[i][j+1])/3

test_cover=np.asarray(c);
cv2.imwrite("test.bmp",test_cover);

n=cv.LoadImage("test.bmp",0)

# /******************************************************************************************************************************************************/
#                                                             CHECKING BOTH THE IMAGES

# /*****************************************************************************************************************************************************/
diff=0
for i in range(0,s.height,1):
    for j in range(0,s.width,1):
            if(n[i,j]!=cover[i,j]):
                print i,j
                diff=diff+1

print "\n The difference in the pixel value are",diff


#/****************************************************************************************************/
# 
#                            Extracting Secret information

#/****************************************************************************************************/
l=48
zero=0
count=l
inf=[]
# c_array=np.asarray(c)
for i in range(0,(s.height)-1,2):
    for j in range(0,(s.width)-1,2):
        Imin=n[i,j]
        Imax=n[i,j]
        L=[n[i+2,j+2],n[i+2,j],n[i,j+2]];

        for item in L:
            if(Imin>item):
                Imin=item
            if(Imax<item):
                Imax=item
        
        d1=Imax-n[i,j+1]if n[i,j+1]<(Imin+Imax)/2 else n[i,j+1]-Imin
        d2=Imax-n[i+1,j]if n[i+1,j]<(Imin+Imax)/2 else n[i+1,j]-Imin
        d3=Imax-n[i+1,j+1]if n[i+1,j+1]<(Imin+Imax)/2 else n[i+1,j+1]-Imin
        


        if(d1>=2):
            n1=int(math.floor(math.log(d1,2)))
            b1=int(n[i,j+1]-s[i,j+1])
            p=n1 if(count>n1) else count
            # print p
            if(n1 >=1 and p > 0):
                # print "b1",b1
                print p

                # print "b1",d2b(b1)
                count = count - p
                zero=zero+p
                inf.extend(padding(d2b(b1),p))

              
        if(d2>=2):
            n2=int(math.floor(math.log(d2,2)))
            b2=int(n[i+1,j]-s[i+1,j])
            p=n2 if(count>n2) else count
            # print p

            if(n2 >=1 and p > 0):
                # print "b2",b2
                print p

                # print n2

                # print "b2",d2b(b2)
                count=count- p
                zero=zero+p
                inf.extend(padding(d2b(b2),p))

               
        if(d3>=2):
            n3=int(math.floor(math.log(d3,2)))
            b3=int(n[i+1,j+1]-s[i+1,j+1])
            p=n3 if(count>n3) else count
            if(n3 >=1 and p > 0):
                print p

                # print "b3",b3
                # p=n3 if(count>n3) else count

                # print "b3",d2b(b3)
                count=count - p
                zero=zero+p
                inf.extend(padding(d2b(b3),p))



# print "count", count
# print inf
print len(inf)
# inf.append(1)
inf=map(int,inf)
# print len(inf),l,"zero",zero
# print "hjkhkhj"
print inf

print frombits(inf)
# print "hellohjh"
# msg="i am kokab"
# msge=tobits(msg)
# print msge
count=0
# print frombits(inf)
