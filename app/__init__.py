"""Creating an instance of app and create_app function."""
# Third party import
from flask import Flask

# Local Import
from instance.config import APP_CONFIG

def create_app(config_name):
    """Create App function."""
    app = Flask(__name__, instance_relative_config=True)

    # Adding Configurations.
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    
    return app
