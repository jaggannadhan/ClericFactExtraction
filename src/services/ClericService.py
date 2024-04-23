import json, requests, traceback
from openai import OpenAI
from src.constants.constants import *

from src.services.DatastoreService import DatastoreService
from src.services.CloudTaskService import CloudTaskService

TASKQUEUE_CLIENT = CloudTaskService()
OPENAI_CLIENT = OpenAI(api_key=API_KEY)
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

        answer = self.extractTextFromOpenAI(question, call_logs)
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
            

    def extractTextFromOpenAI(self, question, logs):
        
        stringifiedPromptsArray = json.dumps(logs)
        prompts = [
            {
                "role": "user",
                "content": stringifiedPromptsArray
            }
        ]

        batchInstruction = {
            "role": "system",
            "content": f"Answer the following question concisely for every element of the array. {question} Reply with an array of answers."
        }

        prompts.append(batchInstruction)
        
        response = OPENAI_CLIENT.chat.completions.create(
            model="gpt-4",
            messages=prompts,
            max_tokens=1000
        )

        choices = response.choices[0]
        answer = choices.message.content
        print(answer)
        answer = json.loads(answer)

        success, msg = DS_CLIENT.update(answer)
        if not success:
            return success, msg
        
        return answer
    
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
