import time
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class MoteurCam:
    bas=0
    haut=110


    centreV=55
    gauche=130
    droite=0
    centreH=50

    valV=centreV
    valH=centreH

    def __init__(self,pwm:PCA9685):
        self.servo=servo.Servo(pwm.channels[0])
        self.servo1=servo.Servo(pwm.channels[1])

        self.servo.angle=self.centreV
        self.servo1.angle=self.centreH



    def dep(self,servo,val):
        if(servo==0):
            self.servo.angle=val
        else:
            self.servo1.angle=val

    def vertical(self,val):
        if val==0:
            self.servo.angle=self.centreV

        val=val*-1
        
        if val>0:
            ecart=self.haut-self.centreV
            result=int(ecart*val)
            self.servo.angle=result+self.centreV

            self.valV=result+self.centreV
        
        if val<0:
            ecart=self.centreV-self.bas
            result=int(ecart*val)
            self.servo.angle=result+self.centreV

            self.valV=result+self.centreV

    
    def horizontal(self,val):
        if val==0:
            self.servo1.angle=self.centreH

        val=val*-1
        
        if val>0:
            ecart=self.gauche-self.centreH
            result=int(ecart*val)

            self.servo1.angle=result+self.centreH


            self.valH=result+self.centreH
        
        if val<0:
            ecart=self.centreH-self.droite
            result=int(ecart*val)
            self.servo1.angle=result+self.centreH


            self.valH=result+self.centreH

    

    
    