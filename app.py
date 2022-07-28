from bottle import Bottle, run, template


app = Bottle()


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@app.route('/wiki/<pagename>')
def show_wiki_page(pagename):
    pass

@app.route('/<action>/<user>')
def user_api(action, user):
    pass

@app.route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@app.route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()

@app.route('/static/<path:path>')
def callback(path):
    return static_file(path, ...)


run(app, host='localhost', port=8080, debug=True)
