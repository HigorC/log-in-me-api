import os
from flask import Flask

app = Flask(__name__)

@app.route("/itWorks")
def defaultRoute():
    return "Yes, it works!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)