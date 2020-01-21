
class Config(object):

	# Common configurations


class DevelopmentConfig(Config):

	DEBUG = True
	SQLALCHEMY_ECHO = True


class ProductionConfig(Config):

	DEBUG = False


app_config = {
	'development': DevelopmentConfig
	'production': ProductionConfig
}