from flask_socketio import SocketIO
from Camera import CameraV2

def initialize_socketio(socketio: SocketIO):

    @socketio.on('disconnect')
    def test_disconnect(reason):
        CameraV2.cam.__del__()
        print('Client disconnected, reason:', reason)
        