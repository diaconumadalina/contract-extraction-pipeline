# Contract Extraction Pipeline

LLM-powered contract data extraction pipeline with PDF ingestion, text chunking, structured extraction, benchmarking, and deployment-ready API.

## Features

- PDF loading & preprocessing
- Chunking + normalization
- LLM structured extraction (OpenAI / Azure)
- Retry, logging, JSON validation
- Benchmark OpenAI vs Azure latency & cost
- FastAPI server + Docker deployment
- Config-based provider switching (no code changes)

## Installation

### 1. Clone repository
git clone https://github.com/USERNAME/contract-extraction-pipeline.git
cd contract-extraction-pipeline

### 2. Create configuration
cp config.example.toml config.toml

Edit `config.toml` with your keys.

---

## Running locally

uv sync
uv run python src/pipeline/run_pipeline.py

---

## API Usage

Start server:
uvicorn src.server.app:app --reload

Open docs:
http://localhost:8000/docs

Upload a PDF → returns JSON extracted fields.

---

## Docker Deployment

docker compose up --build

Public start:
docker run -p 8000:8000 USERNAME/contract-api:v1

---

## Benchmark OpenAI vs Azure

uv run python src/benchmark/run_benchmark.py

Outputs:
- benchmark_results.csv
- latency_graph.png

---

## Evaluation

uv run python src/evaluation/run_evaluation.py

Generates:
- accuracy.csv
- heatmap.png

---

## Configuration

All settings are controlled by:

config.toml

Switch provider without code changes:

provider = "openai"
# or
provider = "azure"

---

## Project Structure

contract-extraction-pipeline/
│
├── src/
│   ├── extraction/
│   ├── loaders/
│   ├── benchmark/
│   ├── evaluation/
│   └── server/
│
├── data/
│   ├── raw/
│   └── sample/
│
├── Dockerfile
├── docker-compose.yml
├── config.example.toml
├── .gitignore
├── pyproject.toml
├── README.md
└── LICENSE
---

## License

MIT

# 📄 Contract Extraction Pipeline

[![Deployment Status](https://img.shields.io/badge/Railway-Active-success)](https://contract-extraction-pipeline-production.up.railway.app)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-live-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-purple)

> Production URL: https://contract-extraction-pipeline-production.up.railway.app


## 🚀 Live Demo

API Live (Production):  
👉 https://contract-extraction-pipeline-production.up.railway.app

Swagger Docs:  
👉 https://contract-extraction-pipeline-production.up.railway.app/docs


