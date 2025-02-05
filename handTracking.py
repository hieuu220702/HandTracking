import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)
if not cap.isOpened():
 print("Cannot open camera")
 exit()

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
               h,w,c = img.shape
               cx, cy = int(lm.x*w), int(lm.y*h)
               print(id, cx, cy)
               if id == 0:
                  cv2.circle(img,(cx,cy),15,(255,0,255),-1)
            mpDraw.draw_landmarks(img, handLms,mpHand.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_COMPLEX,3,
                (255,255,0),thickness=2)
    cv2.imshow("Image",img)
    cv2.waitKey(1)