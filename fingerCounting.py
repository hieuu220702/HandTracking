import cv2
import mediapipe as mp
import time
import handTrackingModule as htm
import os

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0
path = "D:\hoctap\Documents\handTracking\handFinger"
mylist = os.listdir(path)
print(mylist)
overlayList = []
tipIDs = [4,8,12,16,20]
detector = htm.handDetector()
for imPath in mylist:
    image = cv2.imread(f"{path}/{imPath}")
    # print(f"{path}/{imPath}")
    overlayList.append(image)
while True:
    access, img = cap.read()
    h, w, c = overlayList[0].shape
    
    img = detector.find_hand(img=img)
    listPosition = detector.findPosition(img=img,draw=False)
    # print(listPosition[0])
    if len(listPosition) != 0:
        finger = []
        # print(listPosition[0])
        if listPosition[tipIDs[0]][1] > listPosition[tipIDs[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)

        for id in range(1,5):
            if listPosition[tipIDs[id]][2] < listPosition[tipIDs[id]-2][2]:
                finger.append(1)
                
            else:
                finger.append(0)
        # print(finger)
        totalFinger = finger.count(1)
        # print(totalFinger)
        img[0:h,0:w] = overlayList[totalFinger-1]
        cv2.rectangle(img,(20,225),(170,425),(0,255,0),-1)
        cv2.putText(img, str(totalFinger), (45,375),cv2.FONT_HERSHEY_PLAIN,10,
                (255,0,255),thickness=25)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f"FPS:{int(fps)}", (470,70),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),thickness=2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release()
cv2.destroyAllWindows()


