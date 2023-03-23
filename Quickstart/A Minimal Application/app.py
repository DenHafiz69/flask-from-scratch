from flask import Flask
from markupsafe import escape

app = Flask(__name__) # creates an instance of Flask class

@app.route("/") # tell Flask which URL to trigger the function below
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"