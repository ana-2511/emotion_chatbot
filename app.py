from flask import Flask, request, jsonify
import json

# Load dialog flow
with open("emotion_chatbot\dialog_flow.json", encoding="utf-8") as f:
    dialog = json.load(f)

trigger_map = dialog["triggers"]
response_map = dialog["responses"]

# Enhanced trigger matching (partial, case-insensitive)
def match_trigger(text):
    text = text.lower()
    for trigger, emotion in trigger_map.items():
        if trigger in text:
            return emotion
    return "unknown"

# Flask app
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    emotion = match_trigger(user_input)
    response = response_map.get(emotion, response_map["unknown"])
    return jsonify({"emotion": emotion, "response": response})

if __name__ == "__main__":
    app.run(debug=True)
