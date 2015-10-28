import cv2
import cv2.cv as cv
filename = "image.jpg"
oriimage = cv2.imread(filename)
k=2
newx,newy = oriimage.shape[1]/k,oriimage.shape[0]/k #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
cv2.imwrite("new.jpg",newimage)
# cv.SaveImage("new.jpg", newimage)
im = cv.LoadImage("new.jpg")
# displaying the matrix form of image
for i in range(im.height):
    for j in range(im.width):
        print im[i,j],

    print "\n",i	


# cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
# cv2.waitKey(0)