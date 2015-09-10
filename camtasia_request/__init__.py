from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from os import urandom


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = SignedCookieSessionFactory(
        urandom(64),
        secure=False, #CURRENTLY CAUSING KEY ERROR ACCESSING SESSION VALUE WHEN TRUE 
        # Need to determine how to use https on campus server
        httponly=True
        )
    #prefix = '/camtasia-request-dev'
    prefix = ''
    config = Configurator(
        session_factory=session_factory,
        settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('/', '/')
    config.add_route('logout', prefix + '/logout')
    config.add_route('login', prefix + '/login')
    config.add_route('auth', '/auth')
    config.add_route('request', prefix + '/request')
    config.add_route('confirmation', prefix + '/confirmation')
    config.scan()
    return config.make_wsgi_app()
