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
import sys

def main(arg1,arg2):
    name_count=arg2
    import os 
    dirname=os.path.dirname
    print dirname
    stego_name="stego"+name_count+arg1
    cover_name="cover_image"+arg1+".bmp"
    # cv2.imwrite(os.path.join("stego_images",stego_name),s_array);
    # print name_count
    # print type(name_count)
    # name_count=str(name_count)
    s=cv.LoadImage(os.path.join("stego_images",stego_name),0)

    # s=np.asarray(infoimage[:,:])
    print s.width, s.height
    c = [[0]*s.width for i in range(s.height)]
    i=j=0
    # l=80
    
    cover=cv.LoadImage(os.path.join("cover_images",cover_name),0)
    zero=count=0
    zero2=0
    for i in range(s.height):
      for j in range(s.width):
        if(s[i,j]!=cover[i,j]):
          count=count+1
        if(s[i,j]==0):
            zero=zero+1
            # print i,j
        if(cover[i,j]==0):
            zero2=zero2+1

    print "diff pixel",count
    print "zero",zero,zero2
    for i in range(0,s.height,2):
      for j in range(0,s.width,2):
        c[i][j]=s[i,j]

    for i in range(1,s.height,2):
        c[i][s.width-1]=round((c[i-1][s.width-1]+c[i+1][s.width-1])/2)
    for i in range(1,s.width,2):
        c[s.height-1][i]=round((c[s.height-1][i-1]+c[s.height-1][i+1])/2)


    # /***************************************************************************************************************/

    #                 EXTRACTING information from stego image

    # /***************************************************************************************************************/

    # count=l
    print s[2,3],s[3,4]
    width=s.width-1
    height=s.height-1
    for i in range(0,(height),2):
        for j in range(0,(width),2):
            Imin=c[i][j]
            Imax=c[i][j]
            L=[c[i+2][j+2],c[i+2][j],c[i][j+2]];

            for item in L:
                if(Imin>item):  
                    Imin=item
                if(Imax<item):
                    Imax=item
            
            AD=(3*Imin+Imax)/4

            c[i][j+1]=round((AD + (c[i][j]+c[i][j+2])/2)/2)
            c[i+1][j]=round((AD + (c[i][j]+c[i+2][j])/2)/2)
            c[i+1][j+1]=round((c[i][j]+c[i+1][j]+c[i][j+1])/3)

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
    # l=21
    zero=0
    counter=0
    # count=l
    inf=[]
    si=cv2.imread(os.path.join("stego_images",stego_name),0)


    n=height
    m=width

    if(n%2)!=0:
        n-=1
    if(m%2)!=0:
        m-=1
    size=(n*m/4)
    print size  
    # array=[[]]
    array=[]
    for i in range(0,n,2):
      for j in range(0,m,2):
        collect=[]
        collect.append(i)
        collect.append(j)
        # print type(c)
        # print (c)
        array.append((collect))
    # c_array=np.asarray(c)
    temp=[]
    flag=0

    a=2.8568234567123456789213456789876543212345
    x=3.80
    while(1):
        if size==0:
            break
        y=a*abs(1-x)
        y=int(y*pow(10,40))
        # print y
        y=y%(size)
        i=array[y][0]
        j=array[y][1]
        # print i,j
        #perform operation in yth index i and j
        Imin=c[i][j]
        Imax=c[i][j]
        L=[c[i+2][j+2],c[i+2][j],c[i][j+2]];

        for item in L:
            if(Imin>item):
                Imin=item
            if(Imax<item):
                Imax=item
        
        d1=Imax-c[i][j+1]if c[i][j+1]<(Imin+Imax)/2 else c[i][j+1]-Imin
        d2=Imax-c[i+1][j]if c[i+1][j]<(Imin+Imax)/2 else c[i+1][j]-Imin
        d3=Imax-c[i+1][j+1]if c[i+1][j+1]<(Imin+Imax)/2 else c[i+1][j+1]-Imin
        

        
        
        if(d1>=2):
            p=int(math.floor(math.log(d1,2)))
            b=int(round(round(c[i][j+1])-si[i][j+1]))
            # p=n1 if(count>n1) else count
            # print "b",b

            if(p > 0):

                # print "n1",p
                padder=[]

                # print "b",b,c[i][j+1],si[i][j+1]
                if(counter+p)>=8:
                    d=8-counter
                    padder=padding(d2b(b),p)
                    # read starting d bits store it in temp
                    temp.extend(padder[:d])
                    counter=counter+d
                    # Now temp is 8 bit
                    # print "lenght",len(temp),d,counter

                    counter=0
                    # zzz="#"
                    if frombits(map(int,temp))=="#":
                        # print "success"
                        flag=1
                        break
                    # if b==0:
                        # break
                    # the reaming bit (p-d) save it in temp
                    temp=[]
                    temp.extend(padder[d:])
                    counter=counter+p-d

                    # print "temp",temp
                    # saved the remaining p-d from padder to 

                else:
                    counter=counter+p
                    temp.extend(padding(d2b(b),p))

                zero=zero+p
                inf.extend(padding(d2b(b),p))

              
        if(d2>=2):
            p=int(math.floor(math.log(d2,2)))
            b=int(round(round(c[i+1][j])-si[i+1][j]))
            # p=n2 if(count>n2) else count
            # print "b",b
            # padder=[]
            if(p > 0):
                # print "d2",d2,"n2",p

                # print "b",b,c[i+1][j],si[i+1][j]

                # print n2

                # print "b",d2b(b)
                padder=[]
                count=count - p
                zero=zero+p
                if(counter+p)>=8:
                    d=8-counter
                    padder=padding(d2b(b),p)
                    # read starting d bits store it in temp
                    # c=0
                    # while c < d:
                    temp.extend(padder[:d])
                    counter=counter+d
                    # Now temp is 8 bit
                    # print "padder",padder
                    # print "lengths",len(temp),d,counter,temp,frombits(map(int,temp))

                    counter=0
                    # zzz="#"
                    if frombits(map(int,temp))=="#":
                        # print "success"
                        flag=1
                        break
                    # if b==0:
                        # break
                    # the reaming bit (p-d) save it in temp
                    temp=[]
                    temp.extend(padder[d:])
                    counter=counter+p-d
                    # print "temp",temp
                    # saved the remaining p-d from padder to 

                else:
                    counter=counter+p
                    temp.extend(padding(d2b(b),p))

                inf.extend(padding(d2b(b),p))

               
        if(d3>=2):
            p=int(math.floor(math.log(d3,2)))
            b=int(round(round(c[i+1][j+1])-si[i+1][j+1]))
            # p=n3 if(count>n3) else count
            # print "b"
            if(p > 0):
                # print "n3",p

                # print p
                padder=[]
                # print "b",b,c[i+1][j+1],si[i+1][j+1]
                # p=n3 if(count>n3) else count

                # print "b",d2b(b)
                
                zero=zero+p
                if(counter+p)>=8:
                    d=8-counter
                    padder=padding(d2b(b),p)
                    # read starting d bits store it in temp
                    # c=0
                    counter=counter+d
                    # while c < d:
                    temp.extend(padder[:d])
                
                    # Now temp is 7 bit
                    # print "length",len(temp),d,counter
                    # print "p-d d",p-d,d,

                    counter=0
                    # zzz="#"
                    if frombits(map(int,temp))=="#":
                        # print "succss"
                        flag=1
                        break
                    # if b==0:
                    #     break
                    # the reaming bit (p-d) save it in temp
                    temp=[]
                    counter=counter+p-d
                    temp.extend(padder[d:])
                    # print "padder",padder,temp
                    # print "temp",temp
                    # saved the remaining p-d from padder to 

                else:
                    counter=counter+p
                    # print "no"
                    temp.extend(padding(d2b(b),p))

                inf.extend(padding(d2b(b),p))
        if flag==1:
            break




        
        
        size-=1
        array[y],array[size]=array[size],array[y]
        x=y
    # for i in range(0,(height),2):
    #     for j in range(0,(width),2):
       



    # print "count", count
    # print inf
    # inf.append(1)
    # inf=map(int,inf)
    # print len(inf)

    # print len(inf),l,"zero",zero
    # print "hjkhkhj"
    # print inf

    print "After exttraction secret message is  "
    print frombits(inf)
    # print "hellohjh"
    # msg="i am kokab"
    # msge=tobits(msg)
    # print msge

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])