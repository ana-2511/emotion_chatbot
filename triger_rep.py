import pandas as pd
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load dataset
df = pd.read_csv("test.csv")

# Load trigger map
with open("emotion_chatbot\dialog_flow.json") as f:
    dialog = json.load(f)
trigger_map = dialog["triggers"]

# Match function
def trigger_coverage(df, trigger_map):
    count = 0
    for text in df["Text"]:
        if any(trigger in text.lower() for trigger in trigger_map):
            count += 1
    return count, len(df), round(count / len(df) * 100, 2)

matched, total, percent = trigger_coverage(df, trigger_map)
print(f"✅ Trigger coverage on test set: {matched}/{total} → {percent}%")
