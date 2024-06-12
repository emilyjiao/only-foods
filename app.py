from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        result = request.form
        posts.append(result)
    return render_template("index.html", posts=posts)

@app.route('/signup', methods=['POST', 'GET'])
def result():
    return render_template('signup.html')
    
@app.route('/signedup')
def signedup():
    if request.method == "POST":
        name = request.form["name"]
        return render_template('signedup.html', name=name)

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == "POST":
        result = request.form
        posts.append(result)
        return render_template("new.html", posts=posts)

