from config import DEVSERVER_CONFIG
from bottle import run, route, response


@route('/wiki/<page>')
def send_wiki_page(page):
	response.set_header('content-language', 'pt')
	return f'Tu estás na página {page}'


run(**DEVSERVER_CONFIG)