from flask import Flask, jsonify
from flask_restful import Api, Resource
from envparse import env

env.read_envfile()

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

class Hello(Resource):
    def get(self):
        return "Hello World!!!"

class HelloJson(Resource):
    def get(self):
        return jsonify({
            "message": "Hello, World!"
        })

api.add_resource(Hello,'/')
api.add_resource(HelloJson,'/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)