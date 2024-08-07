from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"

if __name__ == "_main_":
    app.run(debug=True)