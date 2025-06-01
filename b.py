# app.py
from flask import Flask, request, render_template, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key="AIzaSyCjyRCboK7hQ2AElUezRu1INsoSM-H5l2E")

system_prompt = """
You are a polite and helpful assistant for a tuition class named "Bright Minds Academy".
make your answers short 
Details:
- Subjects: Math, Science, English (5th to 10th Std, State & CBSE)
- Fees: ₹1500/month per subject
- Timings: Monday to Saturday, 5 PM – 8 PM
- Location: Shivaji Nagar, Pune
- Contact: +91-9876543210
Offer trial classes too.

Always answer clearly and helpfully like a real assistant would.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message")
    prompt = system_prompt + "\n\nUser: " + user_msg + "\nAssistant:"
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"reply": "Sorry, something went wrong."})

if __name__ == "__main__":
    app.run(debug=True)
