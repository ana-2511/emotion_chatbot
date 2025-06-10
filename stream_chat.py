import streamlit as st
import requests

# App setup
st.set_page_config(page_title="💬 Emotion-Aware Chatbot", page_icon="🧠")
st.title("🧠 Emotion-Aware Chatbot (Rule-Based)")
st.markdown("Tell me how you're feeling and I'll try to respond with empathy 💬")

# User input
user_input = st.text_input("How are you feeling today?")

# Emotion-specific follow-ups and media
follow_ups = {
    "fear": {
        "text": "Would you like a short calming video?",
        "video": "https://www.youtube.com/embed/ZToicYcHIOU"
    },
    "sadness": {
        "text": "Would a motivational quote help?",
        "quote": "💡 *“This too shall pass.”* — Ancient Proverb"
    },
    "joy": {
        "text": "Want to celebrate the moment?",
        "balloon": True
    },
    "anger": {
        "text": "Would you like a deep breathing guide?",
        "video": "https://www.youtube.com/embed/2OEL4P1Rz04"
    },
    "love": {
        "text": "Would you like to write this in your gratitude journal?",
        "quote": "💖 *“To love and be loved is to feel the sun from both sides.”* — David Viscott",
        "hearts": True
    },
    "surprise": {
        "text": "Want to share more about what surprised you?"
        
    }
}

# Chatbot logic
if user_input:
    try:
        res = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})
        data = res.json()

        st.subheader(f"📌 Detected Emotion: `{data['emotion']}`")
        st.success(data["response"])

        # Show emotion-aware extras
        emotion = data["emotion"]
        if emotion in follow_ups:
            follow = follow_ups[emotion]
            st.info(f"🤔 {follow['text']}")
            if "quote" in follow:
                st.markdown(follow["quote"])
            if "video" in follow:
                st.video(follow["video"])
            if follow.get("balloon"):
                st.balloons()
            if follow.get("hearts"):
                st.markdown("❤️❤️❤️❤️❤️")

    except:
        st.error("⚠️ Couldn't connect to backend. Please make sure `app.py` is running.")
