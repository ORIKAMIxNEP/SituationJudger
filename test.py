from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def API():
    return "test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
