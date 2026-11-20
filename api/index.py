from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'MonkeyTaggers The Best'

@app.route('/Cool')
def about():
    return 'meow'
