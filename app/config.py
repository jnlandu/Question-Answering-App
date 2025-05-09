class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = '/path/to/upload/folder'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
