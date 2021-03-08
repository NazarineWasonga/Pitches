
import os


class Config:
    """
    Parent config
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY='nazarine'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'nazarine48@gmail.com.com'
    MAIL_PASSWORD = 'ze11y@jones'


class ProdConfig(Config):
    """
    Production config
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """
    Development config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:zelly@localhost/nazarine'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
