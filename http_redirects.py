from config import DEVSERVER_CONFIG
from bottle import run, route, redirect


@route('/')
def redirect_to_home():
	redirect('/home')


# the route below it is only to test the redirection
@route('/home')
def home():
	return 'You were redirected to Home'


run(**DEVSERVER_CONFIG)