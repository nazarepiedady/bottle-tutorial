from bottle import static_file, route


@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/path/to/your/static/files')

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='/path/to/your/static/files')