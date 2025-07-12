from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)
DATA_DIR = "/data"

@app.route("/")
def hello():
    timestamp = datetime.now().isoformat()
    msg = f"Hello from Bhaskara Rao GHCR! Time: {timestamp}\n"

    # Write to file in /data
    with open(os.path.join(DATA_DIR, "requests.log"), "a") as f:
        f.write(msg)

    return msg
