import unittest
from src.models.tracking import ObjectTracker

class TestTracking(unittest.TestCase):
    def test_track(self):
        tracker = ObjectTracker()
        detections = [
            {"bbox": [100, 150, 200, 300], "score": 0.9},
            {"bbox": [110, 160, 210, 310], "score": 0.8}
        ]
        tracks = tracker.track(detections)
        self.assertIsNotNone(tracks)

if __name__ == "__main__":
    unittest.main()