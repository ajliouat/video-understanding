import cv2
from src.pipelines.video_processing import VideoProcessor

class StreamProcessor:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.processor = VideoProcessor()

    def start(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            tracks = self.processor.process_frame(frame)
            # Display or save results
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    processor = StreamProcessor()
    processor.start()