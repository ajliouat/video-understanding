from torch.utils.data import Dataset

class VideoDataset(Dataset):
    def __init__(self, data_path):
        self.data = self._load_data(data_path)

    def _load_data(self, data_path):
        # Load data from JSON file
        import json
        with open(data_path, "r") as f:
            return json.load(f)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]