from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}!"

@app.route("/index")
def index():
    return "<h1>Index Page</h1>"