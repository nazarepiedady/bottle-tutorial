from bottle import Bottle, run


@route('/hello')
def hello():
    return 'Hello World!'


run(host='localhost', port=8080, debug=True)
