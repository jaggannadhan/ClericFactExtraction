# ClericFactExtraction
Extracting facts from call logs using Chat-GPT4 LLM, as a part of Cleric's Internship Assignment, 

## How it works!

1. **Input**
    - Users can input a question.
    - Users can input a list of URLs pointing to text files.
    - Submit button triggers a POST request with the inputs.
    - A 200 response is returned to the user.
2. **Backend**
    - The question is written to the database with a status of "processing".
    - A background task is triggered to extract facts related to the question from the text files using the OpenAI APIs.
    - The extracted facts are stored in the database entity corresponding to the question an status "done".
3. **Output**
    - This screen displays the list of facts, question, and status, when the "Get Answers" button is clicked.


## Run the following steps sequentially to deploy to Appengine
#### make create-venv
#### make setup
#### make deploy-default
#### make deploy-queue

## Include a constants/constants.py file under src directory with the follwing
#### LOCATION = "gae-location"
#### PROJECT_ID = "your-gae-prj-id"
#### QUEUE = "your-queue-name"
#### API_KEY = "your-OPENAI-APIKEY"

## Enjoy the app from <https://hopeful-flame-420906.uc.r.appspot.com/cleric/>