import unittest
from src.models.action_recognition import ActionRecognizer

class TestActionRecognition(unittest.TestCase):
    def test_recognize(self):
        recognizer = ActionRecognizer()
        video_clip = torch.randn(1, 3, 16, 112, 112)  # Example input
        predictions = recognizer.recognize(video_clip)
        self.assertIsNotNone(predictions)

if __name__ == "__main__":
    unittest.main()