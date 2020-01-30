"""
introdução sobre rotas

dinamicas e estaticas
"""

from bottle import run, route

@route('/')
def index():
    """Rota estática para o index do site"""
    return '<h1>Olá mundo</h1>'

@route('/teste')
def index():
    """Rota estática para o /teste do site"""
    return '<h1>TESTE</h1>'

@route('/<person>')
def index(person):
    """Exemplo de rota dinamica"""
    str = f'<h1>olá {person}</h1>'
    if person == "lula":
        str = '<h1>vc não é bem-vindo aqui</h1>'
    return str

run(port=8080)
