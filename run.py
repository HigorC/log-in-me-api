import os
import app_flask as app
from assets.banner import banner as banner
import routes

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(banner)
    print(">> A todo vapor na porta " , port, "\n")
    app.create_app().run(host='0.0.0.0', port=port)
    print(">> Fim da linha meu chapa!\n")