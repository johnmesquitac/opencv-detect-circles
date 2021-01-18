
import numpy as np
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

im = cv2.imread(args["image"])
height, width, depth = im.shape
print(height, width, depth)
thresh = 132
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgray,(5,5),0)
edges = cv2.Canny(blur,thresh,thresh*2)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(im,contours,-1,(0,255,0),-1)

#centroid_x = M10/M00 and centroid_y = M01/M00
M = cv2.moments(cnt)
x = int(M['m10']/M['m00'])
y = int(M['m01']/M['m00'])
print(x,y)
print(width/2.0,height/2.0)
print(width/2-x,height/2-y)


cv2.circle(im,(x,y),1,(0,0,255),2)
cv2.putText(im,"center of Sun contour", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
cv2.circle(im,(width//2,height//2),1,(255,0,0),2)
cv2.putText(im,"center of image", (width//2,height//2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0))
cv2.imshow('contour',im)
cv2.waitKey(0)
cv2.destroyAllWindows()