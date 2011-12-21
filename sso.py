import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return "IT WORKS!"

@app.route("/sso/lion-brand")
def sso():
    a_cookie = request.cookies.get('a_cookie')
    return jsonify() 

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=bool(os.environ.get("DEBUG", ""))
    )

