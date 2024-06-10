from picamera2 import Picamera2, MappedArray
import cv2

#picam2 = Picamera2()
#picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
#picam2.start()

def gen_frames():
    while True:
        frame = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
