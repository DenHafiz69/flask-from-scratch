from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# run using "flask run --debug" to make the server
# changes when the code is changed