from flask import Flask
from random import randint
from time import sleep
import logging


log = logging.getLogger(__name__)
app = Flask(__name__)

def get_name(a_name):
    # wait 0-2 seconds
    n = randint(0,20)
    sleep(0.1 * n)
    app.logger.info('{"function": "%s", "duration": %s}', "get_name", 0.1 * n)
    return a_name

def get_id(an_id):
    # wait 0-1 seconds
    n = randint(0,10)
    sleep(0.1 * n)
    try: 
        b = 1/n  # should throw div/0 exception 10% of the time
    except Exception as e:
        app.logger.exception("error retrieving id: %s", e)
    app.logger.info('{"function": "%s", "duration": %s}', "get_id", 0.1 * n)
    return an_id

def get_account(an_account):
    # wait 1-3 seconds
    n = randint(10,30)
    sleep(0.1 * n)
    app.logger.info('{"function": "%s", "duration": %s}', "get_account", 0.1 * n)
    return an_account


@app.route('/')
def hello_world():
    return 'Huzzah! Flask has been Dockerized!!!'


@app.route('/run')
def run():

    # wait 1-3 seconds
    n = randint(1,10)
    sleep(0.1 * n)
    # query 1
    a = 'foo'
    a = get_name(a)
    # query 2
    a = get_id(a)
    # query 3
    a = get_account(a)
    app.logger.info('Run complete')
    return 'Run complete'


#Navigate to http://localhost:5000 to see if it works! :)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
