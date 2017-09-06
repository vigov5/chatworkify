from flask import Flask
from chatpy.api import API
from chatpy.auth import TokenAuthHandler

app = Flask(__name__)
app.config.from_object('config')

chatwork = API(auth_handler=TokenAuthHandler(app.config['CHATWORK_TOKEN']))

from app.endpoint import *
