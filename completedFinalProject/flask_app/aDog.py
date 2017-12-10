#Class:cst205
#title:flask app
#Authors: Cody and Anna
#Date:8th December 2017
#Who did what:
#Cody: def home, dog_info
#Anna: random feature, html page
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from random import randint
from PIL import Image
#Cody
#This program is called when the captcha is successful,
#and a random doggo gif is open on the web browser.

app = Flask(__name__)
Bootstrap(app)

dog_info = [#dictionary for the doggos
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
	x1 = randint(0,6)#which doggo is it this time?
	return render_template('doggo.html', data = dog_info, doggo = x1)