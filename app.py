from flask import Flask
import time

app = Flask(__name__)

# Record the start time of the app
start_time = time.time()

@app.route("/")
def home():
    # Calculate uptime in seconds
    uptime_seconds = int(time.time() - start_time)
    uptime_minutes = uptime_seconds // 60
    uptime_seconds = uptime_seconds % 60
    return f"Hello from Jojin's Web App!<br>Uptime: {uptime_minutes} min {uptime_seconds} sec<br>1.36 pm → Docker → Git → ACR → AKS → Jenkins automation."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
