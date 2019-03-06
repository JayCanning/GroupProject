from flask import Flask, render_template, request, redirect, url_for
from butter_cms import ButterCMS
client = ButterCMS('44810487d10339615131b21a39643604b13dc981')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/news')
def news():
	return render_template("about.html")
	
@app.route('/people')
def people():
	return render_template("about.html")
	
@app.route('/projects')
def projects():
	return render_template("about.html")
	
@app.route('/collaboration')
def collaboration():
	return render_template("about.html")
	
@app.route('/equipment')
def equipment():
	return render_template("about.html")
	
@app.route('/contact')
def contact():
	return render_template("about.html")
	
@app.route('/admin', methods = ['GET', 'POST', 'DELETE'])
def admin():
	if request.method == 'GET':
		return render_template("cms.html")
	
	if request.method == 'POST':
		return redirect('/about')
		#with open("name.html", "wb") as fo:
			#fo.write("<!DOCTYPE html>
			#<html><head>
			#<title>Sensorium UX Lab - CMS</title>
			#</head>
			#</html>)