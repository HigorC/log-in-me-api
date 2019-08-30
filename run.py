import os
import app_flask as app
from assets.banner import banner as banner
import routes

from flask import Flask
from routes import app_blueprint

app = Flask("__main__")
app.register_blueprint(app_blueprint)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(banner)
    print(">> A todo vapor na porta " ,port, "\n")
    app.run(host='0.0.0.0', port=port)
    print("\n>> Fim da linha meu chapa!\n")