from flask import Flask

app = Flask(__name__)

@app.route('/projects/') # can also go to '/projects'
def projects():
    return 'The project page'

@app.route('/about') # cannot go to '/about/'
def about():
    return 'The about page'