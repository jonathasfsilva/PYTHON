"""
Exemplo de usando os metodos:
    GET,
    POST,
    request
"""

from bottle import route, run, request

@route('/', method='GET')
def index_get():
    return '''
    <form action="/" method="post">
        Username: <input name="username" type="text" />
        </br>
        Password: <input name="password" type="password" />
        </br>
        <input value="Login" type="submit" />
    </form>
    '''

@route('/', method='POST')
def index_post():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return f'''
    <h1>Suas informações</h1>
    </br>
    <h2>username: {username}</h2>
    </br>
    <h2>password: {password}</h2>
    '''

run(port=8080)
