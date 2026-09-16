import RPi.GPIO as GPIO
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

Motor_A_EN = 4
Motor_B_EN = 17
Motor_A_Pin1 = 14
Motor_A_Pin2 = 15
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18


class Roue():
    vitesse=0
    servo=None

    gauche=120
    droite=0
    centre=45

    def __init__(self,pwm : PCA9685):
        self.servo=servo.Servo(pwm.channels[2])
        self.servo.angle=45

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor_A_EN, GPIO.OUT)
        GPIO.setup(Motor_B_EN, GPIO.OUT)
        GPIO.setup(Motor_A_Pin1, GPIO.OUT)
        GPIO.setup(Motor_A_Pin2, GPIO.OUT)
        GPIO.setup(Motor_B_Pin1, GPIO.OUT)
        GPIO.setup(Motor_B_Pin2, GPIO.OUT)

        self.pwm_A=GPIO.PWM(Motor_A_EN,1000)
        self.pwm_B=GPIO.PWM(Motor_B_EN,1000)

    def setVitesse(self,vitesse):
        self.vitesse=vitesse
    
    def rotation(self,val):
        if val==0:
            self.servo.angle=self.centre
        
        val=val*-1
        
        if val>0:
            ecart=self.gauche-self.centre
            result=int(ecart*val)
            self.servo.angle=result+self.centre
        
        if val<0:
            ecart=self.centre-self.droite
            result=int(ecart*val)
            self.servo.angle=result+self.centre
        

    def sens(self,value):

        if(value>0):
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            self.vitesse=100
            self.pwm_B.start(self.vitesse)

        elif(value<0):
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)
            self.vitesse=100
            self.pwm_B.start(self.vitesse)
        
        else:
            self.motorStop()

        

    def motorStop(self):
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor_A_EN, GPIO.LOW)
        GPIO.output(Motor_B_EN, GPIO.LOW)