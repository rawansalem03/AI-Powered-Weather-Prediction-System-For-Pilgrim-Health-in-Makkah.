from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI-Powered Weather Prediction System for Pilgrim Health in Makkah</h1>
    <p>The project has been deployed successfully.</p>
    <p>This system uses AI and weather analytics to support pilgrim health and safety.</p>
    """
