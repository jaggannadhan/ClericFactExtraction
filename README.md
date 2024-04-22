# ClericFactExtraction
Extracting facts from call logs using Chat-GPT4 LLM, as a part of Cleric's Internship Assignment, 

## How it works!

The application consists of two main screens:
1. **Input Screen**
    - This screen allows users to submit
        - A question
        - A list of call logs by providing one or more URLs.
    - After submitting the above inputs, the application creates a background job, and returns 200 response to the user.
2. **Output Screen**
    - This screen displays the final list of facts, extracted from the documents, when the "Get Answers" button is clicked.



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