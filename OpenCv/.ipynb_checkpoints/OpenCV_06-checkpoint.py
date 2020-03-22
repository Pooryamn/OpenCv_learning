import cv2
from random import randint

def Draw_Circle(event,x,y,flags,param):

    global img,r,Red,G,B

    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img,(x,y),r,(Red,G,B),3)
        Red = randint(0,255)
        G = randint(0,255)
        B = randint(0,255)
        r += 5

        if(r >= 100):
            r= 20
        

    elif(event == cv2.EVENT_MOUSEHWHEEL):
        img = cv2.imread('dog_backpack.jpg')
        img = cv2.resize(img,(512,720))


cv2.namedWindow(winname = 'Poorya')

cv2.setMouseCallback('Poorya',Draw_Circle)

img = cv2.imread('dog_backpack.jpg')
img = cv2.resize(img,(512,720))

r = 20
Red = 0
G = 0
B = 0

while True:
    
    cv2.imshow('Poorya',img)

    # if we've waited at least 1 ms AND we've pressed the Esc(0xFF == ord('q') close it with press 'q') 
    if (cv2.waitKey(1) & 0xFF == 27):
        break


cv2.destroyAllWindows()