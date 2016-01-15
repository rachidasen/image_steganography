# !/usr/bin/env python
import cv2.cv as cv

cover=cv.LoadImage("cover_image.bmp",0)

n=cover.height
m=cover.width

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
	
#


print len(array)
# /************************************************************************************************************************************/
# 																				INPUT IN RANDOMISE MANNER
# ***************************************************************************************************************************************
# initialise value of a and x
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




	
	
	size-=1
	array[y],array[size]=array[size],array[y]
	x=y

# print int(y)

# *******************************************************************************************************************************************
# 																						OUTPUTTING THE SAME SEQUENCE
# ********************************************************************************************************************************************						

a=2.8568234567123456789213456789876543212345
x=3.80
while(1):
	if size==0:
		break
	y=a*abs(1-x)
	y=int(y*pow(10,40))
	# print y
	y=y%(size)
	# print array[y]






	#perform operation in yth index i and j
	i=array[y][0]
	j=array[y][1]
	array[y]
	
	size-=1
	array[y],array[size]=array[size],array[y]
	x=y
											


# Implementing fisher yates now
# import argparse
# import os
# message=''
# name_count=0
# parser=argparse.ArgumentParser()
# parser.add_argument("-a","--add",nargs="+",help="hi freing")
# args=parser.parse_args()
# if args.add:
# 	print args.add
# 	name_count=1
# 	for u in args.add:
# 		print "reading_file",u
# 		with open(u,'r') as myfile:
# 			message=myfile.read().replace('\n','')
# 			print message

# 			# message.encode('unicode-escape')
# 			# message.encode("ascii","ignore")
# 			# message.dencode('string-escape')
# 			# mess=str(message)
# 			# print type(mess)
# 			# cmd = 'python image_scale.py '+message+' '+str(name_count)+' '
# 			cmd='python image_scale.py '+'"'+message+'" ' + str(name_count)
# 			# cmd=str(cmd)
# 			cmd.decode('string-escape')
# 			print cmd
# 			os.system(cmd)
# 			print "Allah is the forgiver"
# 			# os.system("python image_scale.py "+mess+' '+str(name_count))
# 			# print u
# 		name_count+=1
# 		myfile.close()


# mess='hello'
# name_count =1
# cmd="python image_scale.py "+mess+' '+str(name_count)
# os.system(cmd)
# cmd="hello "