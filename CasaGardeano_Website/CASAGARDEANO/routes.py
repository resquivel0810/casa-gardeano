from datetime import datetime, timedelta
from flask import render_template, request, make_response, redirect, flash, url_for, send_file
from datetime import datetime, timedelta
from flask_mail import Message
import json
import io

# Local modules
from CasaGardeano_Website import app, mail, db

# Forms and models
from .forms import ContactInfoForm
from .models import ContactInfo

@app.route('/setcookie/')
def setcookie():
    response = make_response(redirect(request.referrer))
    today = datetime.utcnow()
    response.set_cookie(
        key='last_visit',
        value=datetime.strftime(today, '%Y-%m-%d'),
        expires=today + timedelta(365)
    )

    return response

@app.route('/')
def index():
    return render_template('index.html')


