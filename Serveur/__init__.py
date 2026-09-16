from flask import Flask
from flask_socketio import SocketIO, emit
from Camera import CameraV2
from Serveur.Routeur import *

from Serveur.socket import initialize_socketio

app=None
socketio :SocketIO=SocketIO()

def start(ip_robot:str):
    global app,socketio
    app=Flask(__name__,template_folder="Web/Template",static_folder="Web/Static")
    app.config['SECRET_KEY'] = 'secret!'
    app.debug=False


    app.register_blueprint(app_Router)

    socketio.init_app(app,cors_allowed_origins="*",async_mode='threading')
    socketio.start_background_task(capture_frames)

    initialize_socketio(socketio)


    socketio.run(app,ip_robot)


def capture_frames():
    CameraV2.cam.stream(socketio)