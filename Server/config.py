import pathlib

class Config:
    # IP of where its being hosted
    HOSTNAME = "10.0.0.206"

    # get the absolute path to the static files, js, css, etc
    STATIC_FILE_PATH = str(pathlib.Path(__file__).parent.absolute()) + "\html\static"
