from bottle import route

@route('/hello/<name>')
def index(name):
    return f'Hello {name}'
