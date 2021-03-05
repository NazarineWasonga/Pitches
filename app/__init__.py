from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
app = Flask(__name__)  
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import routes, models