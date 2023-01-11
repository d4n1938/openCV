import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0 
cTime = 0
    
Arr = []


while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
  
    # print(results.multi_hand_landmarks)
    
    

    # Display the resulting frame
    if results.multi_hand_landmarks:
      for handLms in results.multi_hand_landmarks:
        for id ,lm in enumerate(handLms.landmark):
          # print(lm)
          h,w,c = img.shape
          cx, cy = int(lm.x*w),int(lm.y*h)
          if id == 0 or id == 4 or id == 8:
            cv2.circle(img,(cx,cy),20,(255,0,0),cv2.FILLED)
         
        mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)
    

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow('frame',img)
    cv2.waitKey(1)
    


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()