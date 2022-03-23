from flask import Flask,render_template

app=Flask(__name__) #creating an empty webapp

@app.route('/')
def index():

	return "Welcome to the Website!"

@app.route('/page1')
def page1():

	return "This is the Page 1"

@app.route('/page2')
def page2():

	return render_template('test-template.html')

app.run(debug=True)