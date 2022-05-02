from src2 import src2

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!!!"