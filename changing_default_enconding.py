from bottle import run, route, response


@route('/iso')
def get_iso():
	#response.charset = 'ISO-8859-15'
	response['charset'] = 'ISO-8859-15'
	return u'This will be sent with ISO-8859-15 enconding.'

@route('/latin9')
def get_latin():
	response.content_type = 'text/html; charset=latin9'
	return u'ISO-8859-15 is also known as latin9.'


run(host='localhost', port=8080, debug=True)