import os
from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.security import Security, SQLAlchemyUserDatastore 

app = Flask(__name__) 
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

from app.users.views import users_blueprint
app.register_blueprint(users_blueprint) 

from app import views, models
from models import * 

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore) 