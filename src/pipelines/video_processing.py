import cv2
from src.models.detection import ObjectDetector
from src.models.tracking import ObjectTracker

class VideoProcessor:
    def __init__(self):
        self.detector = ObjectDetector()
        self.tracker = ObjectTracker()

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        tracks = self.tracker.track(detections)
        return tracks