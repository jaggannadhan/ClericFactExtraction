# ClericFactExtraction
Extracting facts from call logs using Chat-GPT4 LLM, as a part of Cleric's Internship Assignment, 

## How it works, App Design:
1.  **Input**
    - User is expected to provide a question and list of file locations in their respective text boxes.
    - The Submit button triggers a POST request to the Back-end, where we check the POST body for the validity of links etc.
    - If the POST request body successfully passes the checks, then a response with status code 200 is sent back to Front-end.

2)  **Back-end**
    - The back-end will now construct a GetResponse-Json-Object with the status set to "processing". The GetResponse-Json-Object is what will be sent to the frontend.
    - The back-end also initiates a google-cloud-task, that invokes OPENAI API ( the user question and the contents of the call logs are both inputs to the OPENAI API)
    - IF the OPENAI API successfully returns, the results will be populated in the GetResponse-Json-Object.

3)  **Output Page**
    - The only user action here is to click the "Get Answers" button. The button triggers a GET request to the backend, which will inturn return GetResponse Json 
    - If the OPENAI API is running and hasn't yet been completed, the response will have status as "processing", else if it is successful the response will have the facts and status as "done".


## Run the following steps sequentially to deploy to AppEngine
#### make create-venv
#### make setup
#### make deploy-default
#### make deploy-queue

## Include a constants/constants.py file under the src directory with the following
#### LOCATION = "gae-location"
#### PROJECT_ID = "your-gae-prj-id"
#### QUEUE = "your-queue-name"
#### API_KEY = "your-OPENAI-APIKEY"

## Enjoy the app from <https://hopeful-flame-420906.uc.r.appspot.com/cleric/>
