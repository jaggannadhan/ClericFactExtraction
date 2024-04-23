import json, requests, traceback
from src.constants.constants import *

from src.services.DatastoreService import DatastoreService
from src.services.CloudTaskService import CloudTaskService
from src.services.OpenAIService import OpenAIService

OPENAI_CLIENT = OpenAIService()
TASKQUEUE_CLIENT = CloudTaskService()
DS_CLIENT = DatastoreService()

class ClericService:
    
    def manageSubmit(self, data):
        print(data)
        question = data.get("question")
        documents = data.get("documents")

        call_logs = self.getCallLogs(documents)
        if not call_logs:
            return False, {"status": 404}

        success, msg = DS_CLIENT.add(question)
        if not success:
            return success, msg
        
        success, msg = TASKQUEUE_CLIENT.addOperationToQueue(question, call_logs)
        if not success:
            DS_CLIENT.deleteEntity()
        
        return success, msg

    def processSubmit(self, data):
        print(data)
        question = data.get("question")
        call_logs = data.get("callLogs")

        answer = OPENAI_CLIENT.extractTextFromOpenAI(question, call_logs)
        DS_CLIENT.update(answer)
        return answer
        
    
    def getCallLogs(self, documents): 
        call_log_dict = {}
        for url in documents:
            try:
                response = requests.get(url)
                log = response.text
                call_log_dict[url] = log
            except Exception:
                print(traceback.format_exc())
                return None
            
        combined_logs = list(call_log_dict.values())
        print(combined_logs)
        return combined_logs
                
    def getQuestionAndFacts(self):
        success, entity = DS_CLIENT.get()

        if not entity: return "No entities available"

        if success and entity["status"] == "done":
            DS_CLIENT.deleteEntity()

        print(type(entity))
        try:
            facts = entity["facts"]
        except KeyError:
            return {
                "question": entity["question"],
                "facts": [],
                "status": entity["status"]
            }

        return entity
