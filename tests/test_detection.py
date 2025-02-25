import unittest
from src.models.detection import ObjectDetector

class TestDetection(unittest.TestCase):
    def test_detect(self):
        detector = ObjectDetector()
        image = torch.randn(3, 224, 224)  # Example input
        detections = detector.detect(image)
        self.assertIsNotNone(detections)

if __name__ == "__main__":
    unittest.main()