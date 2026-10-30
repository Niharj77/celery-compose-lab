# Advanced Docker Compose – Background Job Processing

A containerized background task processing system built using **FastAPI, Celery, Redis, and Docker Compose**.

This project demonstrates asynchronous task execution, message brokering, container orchestration, resource management, service health checks, and horizontal worker scaling.

## Architecture

```text
                 USER
                   |
                   v
                FASTAPI
                   |
                   v
              REDIS BROKER
                   |
             +-----+-----+
             |           |
             v           v
         CELERY       CELERY
         WORKER 1     WORKER 2
             |           |
             +-----+-----+
                   |
              TASK RESULTS
                   |
                   v
                 REDIS
```

## Technology Stack

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| FastAPI | REST API |
| Celery | Background task processing |
| Redis | Message broker and result backend |
| Python | Application development |

## Project Structure

```text
celery-compose-lab/
│
├── docker-compose.yml
│
├── app/
│   ├── main.py
│   ├── tasks.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── worker/
│   └── Dockerfile
│
├── redis/
│
└── README.md
```

## Features

- Multi-container orchestration using Docker Compose
- Asynchronous background task execution
- Redis message broker integration
- Celery worker architecture
- Multiple worker scaling
- Custom Docker bridge networking
- Internal network isolation
- Redis persistent storage using named volumes
- Container health checks
- Service dependency management
- CPU resource limits
- Memory resource limits
- Automatic container restart policies

## Getting Started

### Prerequisites

- Docker Desktop
- Docker Compose
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/celery-compose-lab.git

cd celery-compose-lab
```

### 2. Build the containers

```bash
docker compose build
```

### 3. Start the application

```bash
docker compose up -d
```

### 4. Check running containers

```bash
docker compose ps
```

### 5. View container logs

```bash
docker compose logs -f
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application status |
| POST | `/generate-report?report_id=101` | Submit a background task |
| GET | `/task/{task_id}` | Check task status and result |

### Example API Request

```bash
curl -X POST "http://localhost:8000/generate-report?report_id=101"
```

Example response:

```json
{
  "message": "Report generation started",
  "task_id": "generated-task-id"
}
```

Check task status:

```bash
curl "http://localhost:8000/task/generated-task-id"
```

## Worker Scaling

Scale Celery workers horizontally:

```bash
docker compose up -d --scale worker=3
```

Check the running workers:

```bash
docker compose ps
```

View worker logs:

```bash
docker compose logs -f worker
```

Each worker can independently consume tasks from the Redis queue.

## Resource Management

The project uses Docker Compose CPU and memory limits.

| Service | CPU Limit | Memory Limit |
|---|---:|---:|
| Redis | 0.25 | 192 MB |
| FastAPI | 0.5 | 384 MB |
| Celery Worker | 0.5 | 384 MB |

Monitor resource consumption:

```bash
docker stats
```

## Docker Networking

The application uses a custom internal bridge network.

- FastAPI communicates with Redis using the service name `redis`.
- Celery workers communicate with Redis using the same service name.
- Redis is not directly exposed to the host.
- Services communicate through Docker's internal DNS.

## Data Persistence

Redis uses a named Docker volume:

```yaml
volumes:
  - redis_data:/data
```

This enables Redis persistence across container recreation when its persistence configuration is enabled.

## Useful Docker Compose Commands

```bash
# Start containers
docker compose up -d

# Stop containers
docker compose stop

# Start stopped containers
docker compose start

# Stop and remove containers and networks
docker compose down

# Rebuild images
docker compose build --no-cache

# Inspect services
docker compose ps

# View logs
docker compose logs -f

# Scale workers
docker compose up -d --scale worker=3

# Monitor resources
docker stats
```

## Learning Outcomes

Through this project, I explored:

1. Docker Compose multi-service orchestration.
2. Asynchronous processing using Celery.
3. Redis as a message broker.
4. Horizontal scaling of worker containers.
5. Docker networking and service discovery.
6. Persistent storage using Docker volumes.
7. Container health checks and restart policies.
8. CPU and memory resource management.

## Future Enhancements

- Flower dashboard for Celery monitoring.
- Prometheus and Grafana integration.
- Docker secrets for sensitive configuration.
- Production-ready logging.
- Dedicated task queues and worker types.
- Development and production Compose configurations.

## Author

**Nihar J.**

Cloud & DevOps Engineering | Docker | AWS | Terraform | Kubernetes | CI/CD

