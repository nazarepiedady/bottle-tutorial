from bottle import Bottle, run


app = Bottle()


@route('/hello')
def hello():
    return 'Hello World!'


run(app, host='localhost', port=8080, debug=True)
