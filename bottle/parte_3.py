"""
Usando cookies para saber se visitei a pagina
"""

from bottle import request, route, run, response

@route('/')
def hello_again():
    string = 'olá é um prazer conhecer voce'
    if request.get_cookie('visited'):
        string = 'Olá, bem vindo de volta'
    response.set_cookie('visited', 'yes')
    return string

run(port=8080)
