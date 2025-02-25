#!/bin/bash
uvicorn src.pipelines.stream_processor:app --host 0.0.0.0 --port 8000