from flask import Flask
from random import random
from time import sleep

app = Flask(__name__)

def get_name(a_name):
	# wait 0-2 seconds
	n = random(0,20)
	sleep(0.1 * n)
	return a_name

def get_id(an_id):
	# wait 0-1 seconds
	n = random(0,10)
	sleep(0.1 * n)
	b = 1/n  # should throw div/0 exception 10% of the time
	return an_id

def get_account(an_account):
	# wait 1-3 seconds
	n = random(10,30)
	sleep(0.1 * n)
	return an_account


@app.route('/')
def hello_world():
    return 'Huzzah! Flask has been Dockerized!!!'


@app.route('/run')
def run():

	# wait 1-3 seconds
	n = random(1,10)
	sleep(0.1 * n)
	# query 1
	a = 'foo'
	a = get_name(a)
	# query 2
	a = get_id(a)
	# query 3
	a = get_account(a)



#Navigate to http://localhost:5000 to see if it works! :)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
