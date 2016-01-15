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
  	c=[]
  	c.append(i)
  	c.append(j)
  	# print type(c)
  	# print (c)
  	array.append((c))
	
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
	print i,j
	#perform operation in yth index i and j

	array[y]
	
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
	print array[y]





	
	#perform operation in yth index i and j
	i=array[y][0]
	j=array[y][1]
	array[y]
	
	size-=1
	array[y],array[size]=array[size],array[y]
	x=y
											