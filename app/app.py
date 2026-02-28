from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! we setup flask before we were away."

if __name__ == "__main__":
    app.run(debug=True)