from bottle import route, run

@route('/hello/<name>')
def index(name):
    return f'Hello {name}'
