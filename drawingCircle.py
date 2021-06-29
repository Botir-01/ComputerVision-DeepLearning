import cv2
import numpy as np

############Funtion###########

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_TRIPLEX
        # cv2.putText(image,'WoW',(x-70,y),font,2,(255,0,0),4) for curiosity :)
        cv2.circle(image,(x,y),50,(0,0,255),-1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image,(x,y),50,(255,0,0),-1)

cv2.namedWindow(winname='drawing')

cv2.setMouseCallback('drawing', draw_circle)

############Show Image with OPENCV###########

image = np.zeros((512,512,3)) # np.int8 for gray

while True:
    
    cv2.imshow('drawing', image)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()