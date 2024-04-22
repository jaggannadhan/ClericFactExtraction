# ClericFactExtraction
Extracting facts from call logs using Chat-GPT4 LLM, as a part of Cleric's Internship Assignment, 

## How it works!
###  After getting the data(questions and documents) from the post request, 
#### >> Created a DB entity for the request, with fields -> question, status="processing".
#### >> Created a google-cloud-task that runs in the background for Fact Extraction from the Call Logs using OPENAI client.
#### >> Retured a suitable response with code 200 to the user.

###  Background google-cloud-task:
#### >>  Iterated through each URL in the document and get the call logs.
#### >>  Used OPENAI's chat completion API with """relevant batch prompt""" to extract the facts.
#### >>  With the response from OPENAI, saved the facts in the created DB entity and mark the status as "done".

###  When a get_question_and_facts request is received, served the DB entity and delete it.

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