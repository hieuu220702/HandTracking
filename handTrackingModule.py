import cv2
import time
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, max_num=2,model_com=1, min_detection=0.5, min_tracking=0.5):
        self.mode = mode
        self.max_num = max_num
        self.model_com = model_com
        self.min_detection = min_detection
        self.min_tracking = min_tracking

        self.mpHand = mp.solutions.hands
        self.hands = self.mpHand.Hands(self.mode, self.max_num, self.model_com, 
                            self.min_detection, self.min_tracking)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hand(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHand.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        listPosition = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                listPosition.append([id, cx, cy])
                # print(id, cx, cy)
                if draw:
                    if id == 0:
                        cv2.circle(img,(cx,cy),15,(255,0,255),-1)
        return listPosition

def main():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    pTime = 0
    cTime = 0
    detector = handDetector()
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
        cv2.waitKey(1)

if __name__ == "__main__":
    main()