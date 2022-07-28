from bottle import static_file, route


@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/path/to/your/static/files')