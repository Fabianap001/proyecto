class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_Username = 'root'
   # MYSQL_inputEmail = 'root'
    MYSQL_Password = ''
    MYSQL_DB = 'flask_login'

    db = MYSQL_DB.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask_login"
    )

config = {
    'development': DevelopmentConfig
}