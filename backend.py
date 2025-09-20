from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "backend alive"}), 200

@app.route("/check_nat")
def check_nat():
    # Call an external API (so request goes through NAT Gateway)
    r = requests.get("https://api.ipify.org?format=json")
    return jsonify({
        "your_public_ip_seen_by_internet": r.json()["ip"],
        "message": "This request went out via NAT Gateway if backend is in private subnet"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
