from flask import Flask

app = Flask(__name__) # creates an instance of Flask class

@app.route("/") # tell Flask which URL to trigger the function below
def hello_world():
    return "<p>Hello, World!</p>"