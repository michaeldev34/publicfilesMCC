class Config:
    pass


#DEFINICION DE LA BASE DE DATOS SIN ENCRIPCION POR FALTA DE TIEMPO
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
}