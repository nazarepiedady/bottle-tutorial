from config import DEVSERVER_CONFIG
from bottle import error, run, route


@error(404)
def not_found(error):
	return 'Not found, try something else'

@route('/')
def home_page():
	return '''
	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<meta name="viewport" content="width=device-width">
			<title>Home Page</title>
		</head>
		<body>
			<h1>Welcome to Home Page</h1>
		</body>
	</html>
	'''


run(**DEVSERVER_CONFIG)