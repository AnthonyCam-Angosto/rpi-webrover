import base64
import time
from flask_socketio import SocketIO
from picamera2 import Picamera2
import cv2
import numpy as np

from pyzbar import pyzbar

from Moteur import mcam



lower_jaune = np.array([20,100,100])
upper_jaune = np.array([40,255,255])

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

class  Camera():
    type="rgb"
    game=None
    run=True

    def __init__(self) :
        self.camera = Picamera2()
        self.camera.configure(self.camera.create_video_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.camera.start()
        

        self.type="rgb"

        regV=cv2.imread('Camera/region/region1.jpeg')
        regH=cv2.imread('Camera/region/region2.jpeg')
        regC=cv2.imread('Camera/region/centre.jpeg')
        self.regionV=self.detectionSimple(regV)
        self.regionH=self.detectionSimple(regH)
        self.regionC=self.detectionSimple(regC)[0]

    def setType(self,type):
        self.type=type

    def stream(self,socketio :SocketIO):
        while self.run:
            frame=self.get_frame()

            _,frame=cv2.imencode('.jpg',frame)
            jpg_as_text = base64.b64encode(frame).decode('utf-8')
            socketio.emit('frame', jpg_as_text)



    def get_frame(self):
        frame = self.camera.capture_array()

        if(self.type!="rgb"):
            if(self.type=="detect"):
                contours=self.detectionSimple(frame,"bleu")

                for contour in contours:
                    (x,y,w,h)=cv2.boundingRect(contour)
                    if cv2.contourArea(contour)<5000:
                        continue
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            elif(self.type=="auto"):
                self.detectionAvancer(frame)

            elif(self.type=="qrcode"):
                self.qrcode(frame)



        return frame

    def capture(self):
        ret,frame=self.video.read()

        if ret:
            _,jpeg=cv2.imencode('.jpg',frame)
            cv2.imwrite("test.jpeg",frame)


    def detectionSimple(self,frame,couleur="jaune"):
        hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if(couleur=="jaune"):
            mask = cv2.inRange(hsv,lower_jaune, upper_jaune)
        if(couleur=="bleu"):
            mask = cv2.inRange(hsv,lower_blue, upper_blue)
        contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        return contours


    def detectionAvancer(self,frame):
        test=self.detectionSimple(frame,"bleu")
        if(test==[]):
            return None
        
        i=0
        for contour in self.regionV:
            i+=1
            (x,y,w,h)=cv2.boundingRect(contour)
            roi = frame[y:y+h, x:x+w]
            
            hsv= cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv,lower_blue, upper_blue)

            val=round(np.count_nonzero(mask) / np.size(mask) * 100, 1)

            if(val>=1):
                if(i==1):
                    if(mcam.valH>mcam.droite):
                        mcam.valH-=2
                        mcam.dep(1,mcam.valH)
                        break
                if(i==2):
                    if(mcam.valH<mcam.gauche):
                        mcam.valH+=2
                        mcam.dep(1,mcam.valH)
                        break
                 
        i=0
        for contour in self.regionH:
            i+=1
            (x,y,w,h)=cv2.boundingRect(contour)

            roi = frame[y:y+h, x:x+w]
            
            hsv= cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv,lower_blue, upper_blue)

            val=round(np.count_nonzero(mask) / np.size(mask) * 100, 1)

            if(val>=1):
                if(i==1):
                    if(mcam.valV>mcam.bas):
                        mcam.valV-=2
                        mcam.dep(0,mcam.valV)
                        break
                if(i==2):
                    if(mcam.valV<mcam.haut):
                            mcam.valV+=2
                            mcam.dep(0,mcam.valV)
                            break
                    

    def qrcode(self,frame):
        detectedBarcodes = pyzbar.decode(frame)

        if not detectedBarcodes:
            return
        else:
            for barcode in detectedBarcodes:
                if barcode.data=="":
                    return
                val=barcode.data.decode('ASCII')

                if(self.game!=None):
                    self.game.isdetect(val)
                    if(self.game.gagner()==True):
                        self.setType("rgb")
                        self.game=None
                else:
                    print(val)

cam:Camera=None