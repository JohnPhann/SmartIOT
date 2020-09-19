import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
import threading
import time
import camera
import datetime
import pytz
from upload import upload_images
from request import upload_request

lock = threading.Lock()

email_update_interval = 5  # sends an email only once in this time interval
video_camera = VideoCamera(flip=False)  # creates a camera object, flip vertically
object_classifier = cv2.CascadeClassifier("models/facial_recognition_model.xml")  # an opencv classifier

# App Globals (do not edit)
app = Flask(__name__)

limit_fps_capture = 20.0
limit_fps_backend = 50.0
fps_capture = 0
fps_detection = 0
fps_preview = 0
ext_name = ".jpg"


@app.route('/')
def index():
    return render_template('index.html')


class Thread_capture(threading.Thread):
    def run(self):
        global fps_capture
        frame_counter = 0
        while True:
            # measure fps
            if frame_counter == 0:
                time_start = time.time()
            frame_counter += 1

            video_camera.capture()
            time.sleep(1 / limit_fps_capture)

            # display fps
            time_elapsed = time.time() - time_start
            if time_elapsed >= 1.0:
                fps_capture = frame_counter
                frame_counter = 0


class Thread_detect(threading.Thread):
    def run(self):
        global fps_detection
        frame_counter = 0
        while True:
            # measure fps
            if frame_counter == 0:
                time_start = time.time()
            frame_counter += 1

            video_camera.detect()

            # display fps
            time_elapsed = time.time() - time_start
            if time_elapsed >= 1.0:
                fps_detection = frame_counter
                frame_counter = 0


class Thread_upload_dropbox(threading.Thread):
    def run(self):
        while True:
            # doing upload save file to storage then upload to dropbox
            if camera.found_objects == True:
                tz = pytz.timezone('Asia/Ho_Chi_Minh')
                timestamp = datetime.datetime.now(tz=tz)
                file_name = timestamp.strftime("%Y%m%d_%H%M%S") + ext_name
                cv2.imwrite(file_name, camera.frame)
                upload_request(file_name)
                upload_images(file_name)


def upload_html():
    frame_counter = 0
    global fps_preview
    while True:
        # measure fps
        if frame_counter == 0:
            time_start = time.time()
        frame_counter += 1

        frame = video_camera.upload()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # display fps
        time_elapsed = time.time() - time_start
        if time_elapsed >= 1.0:
            fps_preview = frame_counter
            frame_counter = 0
            print("###################################")
            print("FPS capture: " + str(fps_capture))
            print("FPS detection: " + str(fps_detection))
            print("FPS preview: " + str(fps_preview))


@app.route('/video_feed')
def video_feed():
    return Response(upload_html(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # start thread first
    task_capture = Thread_capture()
    task_capture.start()

    task_detect = Thread_detect()
    task_detect.start()

    task_dropbox = Thread_upload_dropbox()
    task_dropbox.start()

    # final start server
    app.run(host='0.0.0.0', debug=False)






