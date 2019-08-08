from flask import Flask

def create_app():
    app = Flask(__name__)
    # Reload automático
    app.run(debug=True)
    return app