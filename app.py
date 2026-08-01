from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running on port 443", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Received:", data) 
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 443))
    app.run(host="0.0.0.0", port=port)
