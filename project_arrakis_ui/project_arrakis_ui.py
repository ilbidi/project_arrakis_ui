# Project Arrakis UI
#  user interface to access data of project Arrakis
import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Create application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(SECRET_KEY='PAUISK')
app.config.from_envvar('PROJECT-ARRAKIS-UI-SETTIINGS', silent=True)

@app.route('/')
def index():
    return 'Hello'

@app.route('/credits')
def credits():
    flash('Credits flashed')
    return render_template('credits.html')
