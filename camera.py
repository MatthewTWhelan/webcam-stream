from base_camera import BaseCamera
import cv2 as cv

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    cap = cv.VideoCapture(0)

    @staticmethod
    def frames():
        while True:
            ret, frame = Camera.cap.read()
            if ret:
                _, jpeg = cv.imencode('.jpg', frame)
                yield jpeg.tobytes()
