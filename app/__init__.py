from flask import Flask
from mongoengine import connect
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(20)
connect(os.environ.get("MONGODB_DB"),
        username=os.environ.get("MONGODB_USERNAME"), password=os.environ.get("MONGODB_PASSWORD"),
        authentication_source="admin",
        host=os.environ.get("MONGODB_HOST"), port=int(os.environ.get("MONGODB_PORT")))
from .routes import *
