from bytetrack import ByteTrack

class ObjectTracker:
    def __init__(self):
        self.tracker = ByteTrack()

    def track(self, detections):
        return self.tracker.update(detections)