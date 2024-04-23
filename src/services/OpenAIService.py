import json
from openai import OpenAI
from src.constants.constants import *

OPENAI_CLIENT = OpenAI(api_key=API_KEY)

class OpenAIService:
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
        return answer
