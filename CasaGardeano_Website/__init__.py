from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import json

# App initialization
app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = "claveSecreta"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///NaicaData.db"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = "587"
app.config['MAIL_USE_TLS'] = "True"
app.config['MAIL_USERNAME'] = "correodecasagardeano@gmail.com"
app.config['MAIL_PASSWORD'] = "aquivaelpass"

# App extensions
db = SQLAlchemy(app)
mail = Mail(app)

from .CASAGARDEANO import routes


