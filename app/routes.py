from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joshua'}
    return '''
<html>
    <head>
        <title>Home Page - Courses</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
