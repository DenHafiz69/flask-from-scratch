from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route('/hello') # set a 'link' so it is more memorable
def hello():
    return 'Hello, World.'