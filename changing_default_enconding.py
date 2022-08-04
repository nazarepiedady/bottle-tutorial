from bottle import run, route, response


@route('/iso')
def get_iso():
	#response.charset = 'ISO-8859-15'
	response['charset'] = 'ISO-8859-15'
	return u'This will be sent with ISO-8859-15 enconding.'


run(host='localhost', port=8080, debug=True)