from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Web App! Jojin has done it → Docker → Git → ACR → AKS → Jenkins automation."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)