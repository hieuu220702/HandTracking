import cv2
import time
import mediapipe as mp
import handTrackingModule as htmd


cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
pTime = 0
cTime = 0
detector = htmd.handDetector()
while True:
    success, img = cap.read()
    img = detector.find_hand(img)
    listPosition = detector.findPosition(img)
    if len(listPosition) != 0:
        print(listPosition[4])
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_COMPLEX,3,
                (255,255,0),thickness=2)
    cv2.imshow("Image" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release()
cv2.destroyAllWindows()