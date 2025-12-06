FROM python:3.12-slim

# Work directory inside container
WORKDIR /app

# Copy project files
COPY . /app

COPY config.example.toml config.toml

# Install system dependencies (if PDF + OCR needed later)
RUN apt-get update && apt-get install -y \
    poppler-utils \
 && apt-get clean

# Install uv
RUN pip install --no-cache-dir uv

# Install deps from pyproject.toml
RUN uv sync --frozen

# Expose service port
EXPOSE 8000

# Start API
CMD ["uv", "run", "uvicorn", "src.server.app:app", "--host", "0.0.0.0", "--port", "8000"]
