#!/usr/bin/env python
import cv2
import cv2.cv as cv
import numpy as np
import scipy
import Image
import math
import sys

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

def main(arg1,arg2,arg3):
    
    # from fisheryates import message,name_count
    filename = arg1
    zero=0
    count=0
    # message=arg2
    name_count=arg3
    with open(arg2,'r') as myfile:
        message=myfile.read()
        message+='#'    
    # message="Hera this message is for you  wherever you are, Remember you are my love. I don't know how but you are, so please keep this photo#"
    # message="Hera mera Land tera choot kya combination mera land tere moo me this dessage is for you  wherever you are remember you are my love i don't know how but you are so please keep this photo this is a token of love from me if you like me I love your face I need you so that i could study concentration I need you for sex for blowjob for fucking I want to touch boobs pussy women body want to bath along with you please marry me you will also enjoy a lot with being with me we would have great concentration for study as the great source of distraction for me is porn and a great source of sin Imaging your action will lead to attainment of good for a person#"

    # /*******************************************************************************************************************

    steg=tobits(message)
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


    # /********************************************************************************************************88

    #                             MAKING COVER IMAGE

    # /***********************************************************************************************************/
    for i in range(im.height):
        for j in range(im.width):
        	s[2*i][2*j]=c[2*i][2*j]=im[i,j]

    for i in range(1,k*im.height-1,2):
        s[i][k*im.width-2]=c[i][k*im.width-2]=round((s[i-1][k*im.width-2]+s[i+1][k*im.width-2])/2)
    for i in range(1,k*im.width-1,2):
        s[k*im.height-2][i]=c[k*im.height-2][i]=round((s[k*im.width-2][i-1]+s[k*im.width-2][i+1])/2)
    b=0



    # /*********************************************************************************************************/

    #                         MAKING COVER IMAGE AS WELL AS STEGO IMAGE

    # /********************************************************************************************************/
    counter=0
    pixel_modify_count=0
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

        #/****************************************************************************************************/

         #                        GENERATING STEGO IMAGE

        #/***********************************************************************************************/

    n=k*im.height-2
    m=k*im.width-2

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
        
        AD=(3*Imin+Imax)/4
        d1=Imax-c[i][j+1]if c[i][j+1]<(Imin+Imax)/2 else c[i][j+1]-Imin
        d2=Imax-c[i+1][j]if c[i+1][j]<(Imin+Imax)/2 else c[i+1][j]-Imin
        d3=Imax-c[i+1][j+1]if c[i+1][j+1]<(Imin+Imax)/2 else c[i+1][j+1]-Imin
        # print Imin,Imax,c[i][j+1],c[i+1][j],c[i+1][j+1],d1,d2,d3

        flag=0
        if count >l:
            break
        if(d1>=2):
           n1=int(math.floor(math.log(d1,2)))
           if(n1!=0 and count <l):
                pixel_modify_count=pixel_modify_count+1
                start=count
                count= count+n1 
                # print "n1",count-start
                if count > l:
                    steg+=(count-l)*[0]
                b=bina=0
                
              # embed
                for kokab in range(count-1,start-1,-1):
                    # print i,j+1
                    b=pow(2,bina)*steg[kokab]+b
                    bina=bina+1
                # print "b",b,c[i][j+1],s[i+1][j+1]
                if(b>=s[i][j+1]):
                    b=0
                    count=count-n1

                s[i][j+1]=s[i][j+1]-b
             
        if(d2>=2):
            n2=int(math.floor(math.log(d2,2)))
            if(count<l and n2!=0):
                pixel_modify_count=pixel_modify_count+1
                start=count
                count= count+n2 
                # print "d2",d2,"n2",count-start
                b=bina=0
                if count > l:
                    steg+=(count-l)*[0]
                for kokab in range(count-1,start-1,-1):
                    # print i+1,j
                    # print kokab
                    b=pow(2,bina)*steg[kokab]+b
                    bina=bina+1
                # print "b",b,c[i+1][j],s[i+1][j]
                if(b>=s[i+1][j]):
                    b=0
                    count=count-n2
                s[i+1][j]=s[i+1][j]-b
        # print "d1",d1
        if(d3>=2):
            n3=int(math.floor(math.log(d3,2)))
            if(count<l and n3!=0):
                start=count
                count=count+n3 
                pixel_modify_count=pixel_modify_count+1
                # print "n3",count-start
                b=bina=0
                if count > l:
                    steg+=(count-l)*[0]
                for kokab in range(count-1,start-1,-1):
                    # print i+1,j+1
                    b=pow(2,bina)*steg[kokab]+b
                    bina=bina+1
                # print "b",b,c[i+1][j+1],s[i+1][j+1]
                if(b>=s[i+1][j+1]):
                    b=0
                    count=count-n3
                    
                s[i+1][j+1]=s[i+1][j+1]-b



        
        
        size-=1
        array[y],array[size]=array[size],array[y]
        x=y

    # for i in range(0,(k*im.height-2),2):
    #     for j in range(0,(k*im.width-2),2):
        

    # print n1,n2,n3

    c_array=np.asarray(c)
    s_array=np.asarray(s)



    print "No of pixels getting changed actually",pixel_modify_count,count

    # /*******************************************************************************************************************
        
    #                                                 TESTING OPERATION

    # /*******************************************************************************************************************
    print "len of string",l,"type of l",type(steg)

    # /********************************************************************************************************

    #                                     SAVING THE IMAGE


    # /********************************************************************************************************
    # i=0
    # dirname=""
    import os 
    dirname=os.path.dirname
    print dirname
    stego_name="stego"+name_count+"kb"+arg1
    cv2.imwrite(os.path.join("stego_images",stego_name),s_array);
    cover_name="cover_image"+arg1+"kb.bmp"
    cv2.imwrite(os.path.join("cover_images",cover_name),c_array);



    print "Message Successfully hiden"
    print frombits(steg)
    cv2.waitKey(40000)

if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))