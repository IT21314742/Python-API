from flask import Flask, jsonify

app = Flask(_name_)


@app.route("")
def home():
    return "Home"

if __name__ == "_main_":
    app.run(debug=True)