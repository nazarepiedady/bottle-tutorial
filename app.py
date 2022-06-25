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



run(app, host='localhost', port=8080, debug=True)
