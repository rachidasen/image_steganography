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
    b = padding(b,5)
    print(b)        

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

s=cv.LoadImage("your_stego.bmp",0)
info_str=[]
# s=np.asarray(infoimage[:,:])
print s.width, s.height
c = [[0]*s.width for i in range(s.height)]
i=j=0



# /***************************************************************************************************************/

#                 EXTRACTING information from stego image

# /***************************************************************************************************************/
for i in range(0,(s.height)-4,2):
    for j in range(0,(s.width)-4,2):
        # print c[i][j],
        Imin=s[i,j]
        Imax=s[i,j]
        L=[s[i+2,j+2],s[i+2,j],s[i,j+2]];

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
        print d1,d2,d3
        n1=int(math.floor(math.log(d1, 2)))
        n2=int(math.floor(math.log(d2, 2)))
        n3=int(math.floor(math.log(d3, 2)))
        b1=c[i][j+1]-s[i,j+1]
        b2=c[i+1][j]-s[i+1,j]
        b3=c[i+1][j+1]-s[i+1,j+1]

if __name__ == '__main__':
    d2b(10)
    d2b(5)