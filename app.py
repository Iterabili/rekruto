from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    message = request.args.get('message') 
    if name and message:
        return f'Hello {name}! <br> {message}!'
    return 'Empty page'