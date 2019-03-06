from flask import Flask, render_template, request

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
		return render_template("about.html")
		#with open("name.html", "wb") as fo:
			#fo.write("<!DOCTYPE html>
			#<html><head>
			#<title>Sensorium UX Lab - CMS</title>
			#</head>
			#</html>)