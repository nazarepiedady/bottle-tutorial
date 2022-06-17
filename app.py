from bottle import route, run

@route('/hello/<name>')
def index(name):
    return f'Hello {name}'

run(host='localhost', port=8080)
