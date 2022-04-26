from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from api.models.db import db
from config import Config

# ============ Import Models ============
from api.models.user import User
from api.models.profile import Profile
from api.models.beer import Beer
from api.models.shop import Shop
from api.models.tasting import Tasting

# ============ Import Views ============
from api.views.auth import auth
from api.views.beers import beers
from api.views.shops import shops

cors = CORS()
migrate = Migrate() 
list = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE', 'LINK']

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  cors.init_app(app, supports_credentials=True, methods=list)

  # ============ Register Blueprints ============
  app.register_blueprint(auth, url_prefix='/api/auth')
  app.register_blueprint(beers, url_prefix='/api/beers')
  app.register_blueprint(shops, url_prefix='/api/shops') 

  return app

app = create_app(Config)