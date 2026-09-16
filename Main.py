import argparse

import Serveur
from Camera import CameraV2
from Moteur import *

if __name__ == "__main__":
    
    parse=argparse.ArgumentParser()
    parse.add_argument("ip",help="IP address of the robot",type=str)

    arg=parse.parse_args()
    ip_robot=arg.ip

    CameraV2.cam=CameraV2.Camera()
    Serveur.start(ip_robot)

        