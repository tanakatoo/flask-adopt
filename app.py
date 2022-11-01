from flask import Flask, request, jsonify, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///outer_space'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'ohsosecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False
debug=DebugToolbarExtension(app)

connect_db(app)