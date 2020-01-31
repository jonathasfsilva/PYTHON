from bottle import jinja2_view, route, run, request

@route('/<area>')
@jinja2_view('pages/index.html')
def testes(area):
    return dict(nome=area)

@route('/user', method='GET')
@jinja2_view('pages/user.html')
def user():
    links = ['home', 'about', 'help']
    return dict(links=links)

run(port=8080)
