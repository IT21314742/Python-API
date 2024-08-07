from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"

GET
POST


if __name__ == "__main__":
    app.run(debug=True)