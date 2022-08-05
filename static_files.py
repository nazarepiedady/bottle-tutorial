from bottle import static_file, run, route


@route('/images/<filename:re:.*\.png>')
def send_image(filename):
	print(filename)
	# {root} should include an dot (.) to make reference to current directory
	return static_file(filename, root='./static/images', mimetype='image/png')


@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='./static/images')


@route('/download/<filename:path>')
def download_file(filename):
	return static_file(filename, root='./static/images', download=filename)


run(host='localhost', port=8080, debug=True)