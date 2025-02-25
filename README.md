# Real-time Video Understanding Pipeline

A high-performance video understanding system that combines **object detection**, **tracking**, and **action recognition**. The pipeline is optimized for real-time processing on edge devices.

## Features
- **Multi-object tracking** with ByteTrack.
- **Action recognition** using 3D CNNs.
- **TensorRT optimization** for inference.
- **Stream processing** with multi-threading.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Project Structure](#project-structure)
5. [File Generation](#file-generation)
6. [Workflows](#workflows)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

### Prerequisites
- Python 3.9+
- CUDA-enabled GPU
- Docker (for deployment)

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### Training
To train the object detection and action recognition models:
```bash
./scripts/train.sh
```

### Evaluation
To evaluate the pipeline on benchmark datasets:
```bash
./scripts/evaluate.sh
```

### Deployment
To deploy the pipeline as a real-time video processing service:
```bash
./scripts/deploy.sh
```

---

## Configuration

The project is configured using YAML files in the `configs/` directory:
- **`train_config.yaml`**: Configuration for model training (e.g., learning rate, batch size).
- **`eval_config.yaml`**: Configuration for evaluation (e.g., datasets, metrics).
- **`deploy_config.yaml`**: Configuration for deployment (e.g., API host, port).

---

## Project Structure

```
video-understanding/
├── README.md
├── LICENSE
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── scripts/
│   ├── train.sh
│   ├── evaluate.sh
│   ├── deploy.sh
├── src/
│   ├── data/
│   │   ├── dataloader.py
│   │   ├── preprocess.py
│   ├── models/
│   │   ├── detection.py
│   │   ├── tracking.py
│   │   ├── action_recognition.py
│   ├── utils/
│   │   ├── tensorrt_utils.py
│   │   ├── torchscript_utils.py
│   │   ├── logger.py
│   ├── pipelines/
│   │   ├── video_processing.py
│   │   ├── stream_processor.py
├── notebooks/
│   ├── object_tracking_demo.ipynb
│   ├── action_recognition_demo.ipynb
│   ├── inference_benchmark.ipynb
├── tests/
│   ├── test_detection.py
│   ├── test_tracking.py
│   ├── test_action_recognition.py
├── configs/
│   ├── train_config.yaml
│   ├── eval_config.yaml
│   ├── deploy_config.yaml
├── models/
│   ├── pretrained/
│   ├── fine_tuned/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── videos/
├── logs/
│   ├── training.log
│   ├── evaluation.log
```

---

## File Generation

The following files and directories are **generated or populated** during the setup and execution of the pipeline:

### 1. **Data Files**
- **`data/raw/`**: Contains raw video datasets (e.g., MOT17, UCF101).
- **`data/processed/`**: Contains preprocessed video frames and annotations (e.g., `train.json`, `val.json`).
- **`data/videos/`**: Contains sample videos for testing and demonstration (e.g., `sample.mp4`).

### 2. **Model Files**
- **`models/pretrained/`**: Contains pretrained model files (e.g., `fasterrcnn.pth`, `r3d_18.pth`).
- **`models/fine_tuned/`**: Contains fine-tuned model files generated during training (e.g., `r3d_18.pth`).

### 3. **Log Files**
- **`logs/training.log`**: Logs generated during model training.
- **`logs/evaluation.log`**: Logs generated during pipeline evaluation.

### 4. **Notebooks**
- **`notebooks/object_tracking_demo.ipynb`**: Demonstrates multi-object tracking with ByteTrack.
- **`notebooks/action_recognition_demo.ipynb`**: Demonstrates action recognition using 3D CNNs.
- **`notebooks/inference_benchmark.ipynb`**: Benchmarks the inference performance of the pipeline.

### 5. **Test Files**
- **`tests/test_detection.py`**: Unit tests for the object detection module.
- **`tests/test_tracking.py`**: Unit tests for the multi-object tracking module.
- **`tests/test_action_recognition.py`**: Unit tests for the action recognition module.

---

## Workflows

### Training Pipeline
1. **Data Preprocessing**: Raw video data is preprocessed into frames and annotations.
2. **Model Training**: Object detection and action recognition models are trained.
3. **Evaluation**: The trained models are evaluated on benchmark datasets.

### Deployment Pipeline
1. **API Deployment**: The pipeline is deployed as a real-time video processing service.
2. **Monitoring**: Model performance and API usage are monitored in real-time.

### Retraining Pipeline
1. **Performance Monitoring**: Model performance is continuously monitored.
2. **Automated Retraining**: If performance drops below a threshold, the models are automatically retrained.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.