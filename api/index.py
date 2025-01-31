# from app.create_app import create_app
# import sys
# import os

# # Ensure the parent directory is in sys.path
# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)







from flask import Flask
from flask_session import Session
import redis

app = Flask(__name__)

# Redis session configuration
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "flask_session:"
app.config["SESSION_REDIS"] = redis.StrictRedis(host="redis-connection-url", port=6379, decode_responses=True)

Session(app)

@app.route("/")
def home():
    return "Hello, Vercel with Redis!"

if __name__ == "__main__":
    app.run(debug=True)
