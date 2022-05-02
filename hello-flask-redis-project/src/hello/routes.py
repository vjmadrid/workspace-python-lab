from . import hello_bp

@hello_bp.route('/')
@hello_bp.route('/index')
def index():
    return "Hello World BP!!!"