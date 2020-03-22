import cv2
import numpy as np

##############
## FUNCTION ##
##############


def drawing(event,x,y,flags,param):
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),radius = 100,color = (255,0,0),thickness = -1)
    
    elif(event == cv2.EVENT_RBUTTONDOWN):
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img,'Poorya',(x,y),fontFace = font,fontScale=2,color=(0,0,255),
           thickness=3,lineType=cv2.LINE_AA)
        
    elif(event == cv2.EVENT_MOUSEWHEEL):
        cv2.rectangle(img,pt1=(0,0),pt2=(1023,1023),color=(0,0,0),thickness=-1)
    
    
cv2.namedWindow(winname = 'My_draw') 

cv2.setMouseCallback('My_draw',drawing)
    

############################
## SHOW IMAGE WITH OPENCV ##
############################

img = np.zeros((1024,1024,3))



while True:
    cv2.imshow('My_draw',img)
    
    if(cv2.waitKey(20) & 0xFF == 27):
        break
        
cv2.destroyAllWindows()

