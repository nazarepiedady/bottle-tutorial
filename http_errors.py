from config import DEVSERVER_CONFIG
from bottle import run, route, abort


@route('/redirected')
def redirected():
	abort(401, 'Sorry, access denied.')


run(**DEVSERVER_CONFIG)