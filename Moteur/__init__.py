from adafruit_pca9685 import PCA9685
import board
from Moteur.MCam import MoteurCam
from Moteur.Roue import Roue

i2c=board.I2C()
pwm=PCA9685(i2c)
pwm.frequency=50


roue=None
mcam=None

if(roue is None):
    roue=Roue(pwm)
    roue.setVitesse(100)

if(mcam is None):
    mcam=MoteurCam(pwm)