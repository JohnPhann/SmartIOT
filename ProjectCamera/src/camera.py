import cv2
from imutils.video import VideoStream
import imutils
import os
import time
import numpy as np
import datetime
import pytz

classifier = cv2.CascadeClassifier("models/facial_recognition_model.xml")  # an opencv classifier

frame = np.zeros((480,640,3), np.uint8)
found_objects = False
rectangles_face = 0

class VideoCamera(object):   
    def __init__(self, flip=False):
        # self.vs = PiVideoStream().start()
        self.vs = VideoStream(src=0).start()
        # self.vs = cv2.VideoCapture(0)
        self.flip = flip
        
        cv2.putText(frame, "Opening Camera!", (15,15),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 1)
        time.sleep(2.0)
        print("***INFO***\r\nInitialized Camera!")

    def __del__(self):
        self.vs.stop()
        # self.video.release()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def capture(self):
        global frame
        global found_objects
        
        # frame = self.flip_if_needed(self.vs.read())
        frame = self.vs.read()
        tz = pytz.timezone('Asia/Ho_Chi_Minh')
        timestamp = datetime.datetime.now(tz=tz)
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (14, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
                    
    def detect(self):
        global frame
        global found_objects
        global rectangles_face
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # process detect face
        rectangles_face = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if len(rectangles_face) > 0:
            found_objects = True
        else:
            found_objects = False

    def upload(self):
        global frame
        global found_objects
        
        # Draw a rectangle around the objects
        if(found_objects == True):
            for (x, y, w, h) in rectangles_face:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()

    def get_image(self, file_name):
        frame = self.flip_if_needed(self.vs.read())
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (14, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
        objects = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # print(objects)
        # Draw a rectangle around the objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imwrite(file_name + ".jpeg", frame)
        # print(frame)
        return frame, file_name
