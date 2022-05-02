import os
from src2 import src2

if __name__ == "__main__":
    src2.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))