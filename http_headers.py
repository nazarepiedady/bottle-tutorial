from config import DEVSERVER_CONFIG
from bottle import run, route, response


@route('/wiki/<page>')
def send_wiki_page(page):
	response.set_header('content-language', 'pt')
	return f'Tu estás na página {page}'


@route('/')
def send_home_page():
	response.set_header('set-cookie', 'greeting=welcome')
	response.add_header('set-cookie', 'sweeties=cakes')
	return 'Welcome to Home Page'


run(**DEVSERVER_CONFIG)