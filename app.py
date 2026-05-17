from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my DevOps HD Task project!"

if __name__ == "__main__":
    app.run()