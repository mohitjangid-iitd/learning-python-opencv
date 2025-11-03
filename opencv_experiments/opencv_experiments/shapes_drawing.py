import cv2
import numpy as np

rec = cv2.VideoCapture(0) #start rec. via camera 0

while True:
    ret, frame = rec.read()
    
    width = int(rec.get(3)) #from 17 infos of capture we are reading no. 3 as width 
    height = int(rec.get(4)) #and no. 4 as height
    
    img= frame.copy() #making a copy of frame to use it sapratly
    
    img= cv2.line(img, (0,0),(width,height), (0,255,255),5)
    img= cv2.rectangle(img,(25,25),(width-25,height-25), (255,255,0),10)
    img= cv2.circle(img, (width//2,height//2), 25, (255,0,255),-1) #-1 thickness to fill it entirly
    
    font = cv2.FONT_ITALIC
    
    img= cv2.putText(img, 'cam 0', (35,height-35), font , 2, (255,255,255), 5) # 2-> font size 5-> font thickness
    
    # cv2.imshow('REC',frame)
    cv2.imshow('REC1',img)
    
    if cv2.waitKey(1)== ord('c'): #breaks the loop while press c
        break

rec.release() #camera rec. off
cv2.destroyAllWindows() #close all windows