class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_inputEmail = 'root'
    MYSQL_inputPassword = '123456'
    MYSQL_DB = 'flask_login'
config = {
    'development': DevelopmentConfig
}