from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'dqBRi3KW6bSdPAGBD8V99SZGXT3H2C'

  from .views import views

  app.register_blueprint(views, url_prefix='/')

  return app