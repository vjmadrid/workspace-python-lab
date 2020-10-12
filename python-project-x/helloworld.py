from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World !!!"

@app.route('/user', defaults={'name': 'Crack'})
@app.route('/user/<name>')
# @app.route('/user/<string:name>')
def user(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)

print("helloworld SERVER")