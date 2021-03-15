
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
    MAIL_USERNAME = 'nazarinewasonga48@gmail.com'
    MAIL_PASSWORD = 'naz48810'


class ProdConfig(Config):
    """
    Production config
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """
    Development config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:naz48810/nazarine'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
