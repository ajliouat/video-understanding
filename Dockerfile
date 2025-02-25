FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    python3-pip \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python3", "src/pipelines/stream_processor.py"]