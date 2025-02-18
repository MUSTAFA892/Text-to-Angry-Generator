import os
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json
from google import genai

app = Flask(__name__)
CORS(app)  # Enable CORS for Flask routes
socketio = SocketIO(app, cors_allowed_origins="*")  # Enable CORS for SocketIO

# Get API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("API key for Gemini AI is not set. Please set it as an environment variable.")

# Initialize the genai client
client = genai.Client(api_key=API_KEY)

# Function to generate emoji response using Gemini AI
def get_emoji_response(text):
    try:
        # Generating response using Gemini model
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Give me the output only in emojis, not in any other text: {text}"
        )
        return response.text.strip()  # return the emoji response
    except Exception as e:
        print(f"Error generating emoji response: {e}")
        return "❌ Error generating response. Please try again later."

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("generate_emoji")
def generate_emoji(data):
    text = data.get("text", "").strip()
    if not text:
        emit("emoji_response", json.dumps({"text": "", "emoji": "❌ Please provide a valid text."}))
        return
    emoji_response = get_emoji_response(text)
    emit("emoji_response", json.dumps({"text": text, "emoji": emoji_response}))

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
