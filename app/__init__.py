from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/creche'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = "root_123"

from app.controllers import default

