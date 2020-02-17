import os

from app import create_app

"""
Creating the app by running the create_app function and
passing in the configuration name from the OS environment variable FLASK_CONFIG.
"""
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()