import os
import requests
import json
from giphy_api_key import api_key
from flask import Flask, render_template, session, redirect, request, url_for, flash
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, PasswordField, BooleanField, SelectMultipleField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from werkzeug.security import generate_password_hash, check_password_hash


api_key = "NXSRc2T72koBky3Jzu9JaAQU1NdnPdT7"
q = 'funny'
limit = 5 
data = requests.get('http://api.giphy.com/v1/gifs/search?q={}&limit={}&api_key={}'.format(q,limit,api_key))
json_data = json.loads(data.text)
gif_dict = json_data['data']
print(type(gif_dict))
print(len(gif_dict))
print(gif_dict[0]['title'])