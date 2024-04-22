# ClericFactExtraction
Extracting facts from call logs using Chat-GPT4 LLM, as a part of Cleric's Internship Assignment, 

## Run the following steps sequentially to deploy to Appengine
#### make create-venv
#### make setup
#### make deploy-default
#### make deploy-queue

## Include a constants/constants.py file under src directory with the follwing
LOCATION = "<gae-location>"
PROJECT_ID = "<your-gae-prj-id>"
QUEUE = "<your-queue-name>"
API_KEY = "<your-OPENAI-APIKEY>"

## Enjoy the app from <https://hopeful-flame-420906.uc.r.appspot.com/cleric/>