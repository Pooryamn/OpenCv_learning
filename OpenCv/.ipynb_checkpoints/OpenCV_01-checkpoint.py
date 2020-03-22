# Open and work with opencv in script files : 

import cv2

img = cv2.imread('00-puppy.jpg')

while True:
    
    cv2.imshow('Poorya',img)

    # if we've waited at least 1 ms AND we've pressed the Esc(0xFF == ord('q') close it with press 'q') 
    if (cv2.waitKey(1) & 0xFF == 27):
        break


cv2.destroyAllWindows()