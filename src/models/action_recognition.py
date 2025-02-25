import torch
from torchvision.models.video import r3d_18

class ActionRecognizer:
    def __init__(self, model_path="models/pretrained/r3d_18.pth"):
        self.model = r3d_18(pretrained=True)
        if model_path:
            self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def recognize(self, video_clip):
        with torch.no_grad():
            predictions = self.model(video_clip)
        return predictions