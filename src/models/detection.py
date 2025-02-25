import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn

class ObjectDetector:
    def __init__(self, model_path="models/pretrained/fasterrcnn.pth"):
        self.model = fasterrcnn_resnet50_fpn(pretrained=True)
        if model_path:
            self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def detect(self, image):
        with torch.no_grad():
            predictions = self.model([image])
        return predictions