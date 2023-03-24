from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__) # creates an instance of Flask class

@app.route("/") # tell Flask which URL to trigger the function below
def index():
    return "Index Page"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# show the directory of each function when the python file is executed
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello')) 
