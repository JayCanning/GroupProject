from flask import Flask, render_template, request
import os
#from butter_cms import ButterCMS
#client = ButterCMS('44810487d10339615131b21a39643604b13dc981')

app = Flask(__name__)
app.secret_key = "sensorium"
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/news')
def news():
	return render_template("news.html")
	
@app.route('/people')
def people():
	return render_template("people.html")
	
@app.route('/projects')
def projects():
	return render_template("projects.html")
	
@app.route('/collaboration')
def collaboration():
	return render_template("collaboration.html")
	
@app.route('/equipment')
def equipment():
	return render_template("equipment.html")
	
@app.route('/contact')
def contact():
	return render_template("contact.html")
	
@app.route('/admin', methods = ['GET', 'POST', 'DELETE'])
def admin():
	if request.method == 'GET':
		return render_template("cms.html")
	
	if request.method == 'POST':
		if os.path.exists('test.txt') == False:
			file = open("test.txt", "w")
			file.write("test")
			file.close()
		return render_template("cms.html")
		
	if request.method == 'DELETE':
		if os.path.exists('test.txt') == True:
			os.remove("test.txt")
		return render_template("cms.html")
		
		