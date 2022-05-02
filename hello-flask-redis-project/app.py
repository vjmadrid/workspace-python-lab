import os

from src import create_app
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app = create_app()

    # Run the app
    app.run(host="0.0.0.0", port=8080)
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))