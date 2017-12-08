from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from random import randint
from PIL import Image

app = Flask(__name__)
Bootstrap(app)

dog_info = [
	{
		"id" : "christmas",
		"text" : "Merry Christmas from Doggo"
	},
	{
		"id" : "easy",
		"text" : "Doggo nuut impersed",
	},
	{
		"id" : "infiltrated",
		"text" : "Doggo iz in, too ez",
	},
	{
		"id" : "moon",
		"text" : "One small step for doggos",
	},
	{
		"id" : "pizza",
		"text" : "Gud job, doggo has food 4 u",
	},
	{
		"id" : "playTime",
		"text" : "Work is done, doggo wants to play",
	}
	]
@app.route('/')
def home():
	x1 = randint(0,6)
	return render_template('doggo.html', data = dog_info, doggo = x1)