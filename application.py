from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return '<h1>hello this is second test message for you.</h1>'

