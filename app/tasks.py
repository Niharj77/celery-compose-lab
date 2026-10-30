import time
import os
from celery import Celery

celery_app = Celery(
    "background_tasks",
    broker=os.getenv("REDIS_URL", "redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379/0")
)

@celery_app.task
def generate_report(report_id):
    print(f"Generating report: {report_id}")

    time.sleep(20)

    print(f"Report completed: {report_id}")

    return {
        "report_id": report_id,
        "status": "completed"
    }