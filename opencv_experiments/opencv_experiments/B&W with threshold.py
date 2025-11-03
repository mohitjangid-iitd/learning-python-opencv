import cv2
import numpy as np

rec = cv2.VideoCapture(0) #start rec. via camera 0

def bgr2bw (img,Threshold=120):
    '''Take an image and convert it to grayscale.
    Then, convert it to pure black and white ( binary channel )using a given threshold.
    Convert it again to BGR to display it with BGR channels.'''
    gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bw_img= cv2.threshold(gray_img , Threshold, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(bw_img, cv2.COLOR_GRAY2BGR) 
    
while True:
    ret, frame = rec.read()                 #Frame-by-frame analysis of a given video or live feed
    
    width = int(rec.get(3))
    height = int(rec.get(4))
    
    x,w=int(0.3*width),int(0.20*width)
    y,h=int(0.7*height),int(0.10*height)
    
    if not ret:                             #Break the loop when the video ends
        break
    
    # cropped_frame = frame[y:y+h, x:x+w]     #Modify the frame for the desired area
    
    bw_img= bgr2bw(frame,215)

    cv2.imshow('REC1',bw_img)
    
    if cv2.waitKey(100)== ord('c'): #breaks the loop while press c
        break

rec.release() #camera rec. Off
cv2.destroyAllWindows() #close all windows