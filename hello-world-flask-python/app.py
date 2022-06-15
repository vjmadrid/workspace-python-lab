from flask import Flask, jsonify
from envparse import env

env.read_envfile()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"

@app.route('/json')
def json_hello_world():
    return jsonify({
        "message": "Hello, World!"
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)