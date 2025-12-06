# Contract Extraction Pipeline

[![Deployment Status](https://img.shields.io/badge/Railway-Active-success)](https://contract-extraction-pipeline-production.up.railway.app)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-live-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-purple)

> Production URL
> 📌 [https://contract-extraction-pipeline-production.up.railway.app](https://contract-extraction-pipeline-production.up.railway.app)

---

## 🚀 Live API Demo

| Resource         | URL                                                                                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Swagger UI       | [https://contract-extraction-pipeline-production.up.railway.app/docs](https://contract-extraction-pipeline-production.up.railway.app/docs)     |
| Health Check     | [https://contract-extraction-pipeline-production.up.railway.app/health](https://contract-extraction-pipeline-production.up.railway.app/health) |
| Extract Endpoint | `POST /extract-pdf`                                                                                                                            |

---

## ✨ Overview

LLM-powered contract extraction pipeline with:

* PDF ingestion & text normalization
* Structured JSON extraction (parties, clauses, signatures, terms)
* Retry logic, validation, error safety
* Benchmarking OpenAI vs Azure responses
* Dockerized, CI/CD enabled, Railway production

---

## 📁 Project Structure

```
contract-extraction-pipeline/
│
├── src/
│   ├── extraction/
│   ├── loaders/
│   ├── preprocess/
│   ├── benchmark/
│   ├── evaluation/
│   └── server/
│
├── data/
├── config.example.toml
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Environment Setup

### 1. Clone Repository

```bash
git clone https://github.com/diaconumadalina/contract-extraction-pipeline.git
cd contract-extraction-pipeline
```

### 2. Create Config

```bash
cp config.example.toml config.toml
```

---

## 🔐 Environment Variables

Add in **Railway → Variables**:

| Key            | Example                                                        |
| -------------- | -------------------------------------------------------------- |
| PROVIDER       | openai or azure                                                |
| OPENAI_API_KEY | sk-xxxxx                                                       |
| OPENAI_MODEL   | gpt-4o-mini                                                    |
| AZURE_API_KEY  | xxxx                                                           |
| AZURE_ENDPOINT | [https://xxx.openai.azure.com/](https://xxx.openai.azure.com/) |
| AZURE_MODEL    | gpt-4o                                                         |
| LOG_LEVEL      | info                                                           |

⚠️ NOTE: No secrets committed to `config.toml`.

---

## ▶️ Run Locally

### Install dependencies

```bash
uv sync
```

### Start API

```bash
uvicorn src.server.app:app --reload
```

Swagger:

```
http://localhost:8000/docs
```

---

## 📦 Docker

### Build & Run

```bash
docker compose up --build
```

or

```bash
docker build -t contract-api .
docker run -p 8000:8000 contract-api
```

---

## 🧪 API Example (Postman / Curl)

### **POST /extract-pdf**

**Headers**

```
Content-Type: multipart/form-data
```

**Body**

```
file: contract.pdf
```

**Response**

```json
{
  "title": "Service Agreement",
  "parties": ["Company A", "Company B"],
  "duration": "12 months",
  "clauses": [...]
}
```

---

## 📊 Benchmarking

```bash
uv run python src/benchmark/run_benchmark.py
```

Outputs:

* latency.csv
* cost_comparison.json
* charts in `/benchmark/results`

---

## 📈 Evaluation

```bash
uv run python src/evaluation/run_evaluation.py
```

Outputs:

* accuracy.csv
* heatmap.png

---

## 🚀 CI/CD (Railway Auto Deploy)

* Connected to GitHub `main`
* `Wait for CI` enabled
* Auto-deploy on merge to `main`

Push changes:

```bash
git add .
git commit -m "update"
git push
```

---

## 📜 License

MIT

---

### 🎯 Next Optional Improvements

* Add `/extract-text` endpoint
* Add `/compare-models` for OpenAI vs Azure extraction output
* Add CI test suite before deploy
