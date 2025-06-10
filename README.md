## Emotion-Aware Rule-Based Chatbot

A rule-based chatbot that identifies user emotions using predefined trigger phrases and responds with empathetic messages — built without any ML models.

Dataset Used

- train.csv, val.csv, and test.csv  
- Each file contains:  
  - Text: User statements  
  - Emotion: One of six classes (joy, sadness, anger, fear, love, surprise)  
- Used to extract common emotion-triggering phrases for building dialog_flow.json  
- No model was trained; dataset was used to improve trigger coverage

Approach Summary

- Created a JSON file with emotion-trigger keywords and phrases (dialog_flow.json)  
- Used Flask (app.py) to process user input, detect emotion via partial matching  
- Used Streamlit (stream_chat.py) for a user-friendly UI  
- Added emotion-specific enhancements like quotes, videos, and visual effects  
- Achieved 19.15% trigger match on the test dataset (383/2000 samples)

 Dependencies

- Python 3.11+
- Flask
- Streamlit
- Requests
- Pandas (for analysis scripts)

Folder Structure

emotion_chatbot_json/
├── app.py                -> Flask backend
├── dialog_flow.json      -> Emotion triggers and responses
├── stream_chat.py        -> Streamlit frontend
├── triger_rep.py         -> Trigger coverage tester
├── extract.ipynb         -> Phrase extractor from datasets 

 
Running the Project

Step 1: Start the Flask backend by running `app.py`  
Step 2: Start the Streamlit frontend by running `stream_chat.py`  
Step 3: Interact with the chatbot in your browser.

Make sure both backend and frontend are running in separate terminals.

Trigger Coverage

The chatbot’s trigger logic was tested against the test.csv dataset.

Results:

- Total test samples: 2000  
- Trigger matches: 1101  
- Coverage: 55.05%

## Decision Tree was used first but it showed much smaller accuracy with negligible amount of right emotion prediction. It was becoming biased towards a particular emotion type (eg: anger). The usage of decision tree can be seen in the convert.ipynb file
