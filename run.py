import os
import app_flask as app

import routes

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.create_app().run(host='0.0.0.0', port=port)