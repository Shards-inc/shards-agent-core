# Shards AI Agent System Deployment Guide

This guide provides instructions for deploying the Shards AI Agent System in various environments.

## 1. Prerequisites
- Python 3.11+
- `pip` package manager
- Git
- Docker (for containerized deployment)
- Access to Shards Foundation MCP servers (if applicable)

## 2. Local Deployment

### 2.1 Clone the Repository
```bash
git clone https://github.com/Shards-inc/shards-agent-core.git
cd shards-agent-core
```

### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 2.3 Run the System
```bash
python main.py
```

## 3. Containerized Deployment (Docker)

### 3.1 Build Docker Image
Create a `Dockerfile` in the root of the `shards-agent-core` directory:

```dockerfile
# Dockerfile
FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

Then, build the Docker image:
```bash
docker build -t shards-agent-system .
```

### 3.2 Run Docker Container
```bash
docker run -p 8000:8000 shards-agent-system
```

## 4. Cloud Deployment (NVIDIA NIM Integration)

For high-performance, scalable deployments, the Shards AI Agent System can be integrated with NVIDIA NIM (Inference Microservices).

### 4.1 Prepare Model for NIM
Ensure your agent models (e.g., Nemotron-based reasoning models) are compatible with NIM. This typically involves exporting them in a supported format (e.g., ONNX, TensorRT).

### 4.2 Create NIM Microservice
Follow NVIDIA's documentation to create a NIM microservice for your agent. This will containerize your agent and expose it via an API endpoint.

### 4.3 Deploy to NVIDIA AI Enterprise
Deploy your NIM microservice to an NVIDIA AI Enterprise platform for managed inference and scaling.

## 5. Configuration
Configuration parameters (e.g., MCP server URLs, API keys) can be managed via environment variables or a dedicated configuration file (e.g., `config.ini` or `settings.py`).

## 6. Monitoring and Logging
- Agent logs are output to standard output and can be captured by container orchestration systems.
- Integrate with Prometheus/Grafana for metrics collection and visualization.
- Utilize Shards Foundation's `Kloc-kernel-level-oversight-council` for advanced monitoring and governance.
