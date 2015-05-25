from app import app
from flask import render_template
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
	friends = ["pp1","pp2","pp3","pp4"]
	return render_template("index.html",friends = friends)

@app.route('/abhinav')
def abhi():
	user = {'nickname': 'Divyank'}  # fake user
	title = "friends"
	friends = ["aa1","aa2","aa3","aa4"]
	return render_template("index.html",friends = friends)

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

