#!flask/bin/python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
	
@app.route('/api/brew/<int:cups>', methods=['GET'])
def brew_coffee(cups):
	#print(cups)
	if (cups >= 1 and cups <= 12):
		cmd = "start cmd /c python smarter.py brew " + str(cups)
		returned_value = os.system(cmd)  # returns the exit code in unix
		print(returned_value)
		#os.system(arg)
		return ("Brewing ") + str(cups) + (" cup[s] of coffee")
	else:
		return ("Please select number of cups 1-12..")

@app.route('/api/reset/', methods=['GET'])		
def reset_coffee():
	cmd = "start cmd /c python smarter.py reset"
	returned_value = os.system(cmd)  # returns the exit code in unix
	print(returned_value)
	return ("Default settings applied")
	
if __name__ == '__main__':
    app.run(debug=True)