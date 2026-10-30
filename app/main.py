from fastapi import FastAPI
from celery.result import AsyncResult
from tasks import celery_app, generate_report

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Celery Background Processing API",
        "status": "running"
    }

@app.post("/generate-report")
def create_report(report_id: int):
    task = generate_report.delay(report_id)

    return {
        "message": "Report generation started",
        "task_id": task.id
    }

@app.get("/task/{task_id}")
def task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)

    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }