import cv2
import json

def preprocess_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame.tolist())
    cap.release()

    with open(output_path, "w") as f:
        json.dump(frames, f)