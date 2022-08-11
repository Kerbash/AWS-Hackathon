from flask import Flask, abort, request
import json

from .config import Config


# blueprint
from .html.blueprint import main_blueprint

class AwsServer():
    """
    Create a server
    do run() to run the server on a separate thread
    """

    def __init__(self, name="AWS Server"):
        super().__init__()
        # create a Flask web app
        self.webApp = Flask(name)
        # load the config
        self.webApp.config.from_object(Config)
        # load the static file folder js css image etc
        self.webApp.static_folder = self.webApp.config["STATIC_FILE_PATH"]
        # load the blueprints ig the html function
        self.webApp.register_blueprint(main_blueprint)

    def run(self):
        # host the app at port 8080
        self.webApp.run(self.webApp.config["HOSTNAME"], port="8080")
