from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/<name>')
def specific_name(name):
    return 'Hello ' + name

@app.route('/calculator')
def calc_page()
	return render_template("calculator.html")

@app.route('/calculator/<num1><op><num2>')
def calculate(num1, op, num2):
	num1 = int(num1)
	num2 = int(num2)
	result = 0
	if op == '+':
		result = num1+num2
	elif op == '-':
		result = num1-num2
	elif op == '*':
		result = num1*num2
	elif op == ':':
		if num2 == 0:
			#result = str(result)
			result = "invalid"
		else:
			result = num1/num2

	return str(result)
