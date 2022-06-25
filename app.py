from bottle import Bottle, run


app = Bottle()


@route('/hello')
def hello():
    return 'Hello World!'


run(host='localhost', port=8080, debug=True)
