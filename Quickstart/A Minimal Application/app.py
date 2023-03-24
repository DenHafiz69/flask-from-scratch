from flask import Flask

app = Flask(__name__) # create an instance of Flask class

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"