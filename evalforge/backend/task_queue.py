import threading
import time
import uuid
import logging

logger = logging.getLogger(__name__)
queue = []
results = {}
lock = threading.Lock()


def add_task(text, models, prompt, sequential):
    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "text": text,
        "models": models,
        "prompt": prompt,
        "sequential": sequential,
        "status": "queued",
        "result": {}
    }
    with lock:
        queue.append(task)
    logger.info(f"Task {task_id} added.")
    return task_id


def get_task_status(task_id):
    with lock:
        if task_id in results:
            return results[task_id].copy()
        for task in queue:
            if task["id"] == task_id:
                return task.copy()
    return {"status": "not_found"}


def task_worker(summarizer_func):
    logger.info("Task worker started.")
    while True:
        task = None
        with lock:
            if queue:
                task = queue.pop(0)
                task["status"] = "running"
                results[task["id"]] = task
                logger.info(f"Processing task {task['id']}.")
        if task:
            try:
                summary = summarizer_func(task["text"], task["models"], task["prompt"], task["sequential"])
                with lock:
                    results[task["id"]]["status"] = "done"
                    results[task["id"]]["result"] = summary
                logger.info(f"Task {task['id']} completed.")
            except Exception as e:
                logger.exception(f"Task {task['id']} failed: {e}")
                with lock:
                    results[task["id"]]["status"] = "failed"
                    results[task["id"]]["result"] = {"error": str(e)}
        else:
            time.sleep(1)
