from picamera2 import Picamera2
import cv2
import time
import os

def gen_frames():
    picam2 = Picamera2()
    picam2.start()
    while True:
        frame = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')