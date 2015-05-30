import tasks
from app import app
from flask import render_template,request
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Divyank'}  # fake user
    title = "friends"
    friends = ["ds","abhi","gyan","arun"]
    return render_template("index.html",title = title,friends = friends)

@app.route('/pawan')
def pp():
	user = {'nickname': 'Divyank'}  # fake user
	title = "friends"
	val = tasks.add_together_pawan.delay(5,6)
	friends = ["pp1","pp2","pp3","pp4",val]
	return render_template("index.html",friends = friends)

@app.route('/abhinav/', methods=['POST'])
def abhi():
	username = request.form["username"]
	password = request.form ["password"]
	user = {'nickname': 'Divyank'}  # fake user
	title = "friends"
	friends = ["aa1","aa2","aa3","aa4", username, password]
	return render_template("index.html",friends = friends)
	#return str(friends)

@app.route('/divyank')
def ds():
	user = {'nickname': 'Divyank'}  # fake user
	title = "friends"
	friends = ["ds1","ds2","ds3","ds4"]
	return render_template("index.html",friends = friends)

@app.route('/gyanendra')
def gyan():
	user = {'nickname': 'Divyank'}  # fake user
	title = "friends"
	friends = ["gy1","gy2","gy3","gy4"]
	return render_template("index.html",friends = friends)

