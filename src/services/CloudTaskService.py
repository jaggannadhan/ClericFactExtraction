import json, traceback
from google.cloud import tasks
from src.constants.constants import *
from google.api_core import exceptions as GoogleExceptions

CLOUD_CLIENT = tasks.CloudTasksClient()

class CloudTaskService:
    def createQueue(self):
        try:
            queue_path = CLOUD_CLIENT.queue_path(PROJECT_ID, LOCATION, QUEUE)
            max_attempts = 3
            queue = CLOUD_CLIENT.create_queue(
                parent=f"projects/{PROJECT_ID}/locations/{LOCATION}", 
                queue= {
                    "name": queue_path,
                    "rate_limits": {"max_dispatches_per_second": 1},
                    "retry_config": {"max_attempts": max_attempts},
                }
            )
            print(f"Queue created: {queue.name}")
        except GoogleExceptions.AlreadyExists:
            return True, "Queue already exists"
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to create Queue"

    
    def addOperationToQueue(self, question, documents):
        try:
            parent = CLOUD_CLIENT.queue_path(PROJECT_ID, LOCATION, QUEUE)
            
            task = {
                "app_engine_http_request": {
                    "http_method": tasks.HttpMethod.POST,
                    "relative_uri": "/cleric/push-queue",
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({
                        "question": question,
                        "documents": documents
                    }).encode()
                }
            }

            response = CLOUD_CLIENT.create_task(parent=parent, task=task)
            print(response)
            return True, "Successfully added Task to Queue"
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to add Task to Queue"
