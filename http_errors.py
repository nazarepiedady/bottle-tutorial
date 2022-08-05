from bottle import run, route, abort


server = dict(host='localhost', port=8080, debug=True)

@route('/redirected')
def redirected():
	abort(401, 'Sorry, access denied.')


run(**server)