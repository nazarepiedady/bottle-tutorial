from bottle import static_file, run, route


@route('/images/<filename:re:.*\.png>')
def send_image(filename):
	print(filename)
	# {root} should include an dot (.) to make reference to current directory
	return static_file(filename, root='./static/images', mimetype='image/png')


run(host='localhost', port=8080, debug=True)