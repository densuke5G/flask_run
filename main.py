from flask import Flask, render_template

app = Flask(__name__)

from flaskr.db import Session

@app.teardown_appcontext
def shutdown_session(exception=None):
    Session.remove()

@app.route('/')
def hello_world():
    message = "Hello, World!"
    name = "Daisuke"
    return render_template('hello_world.html', name = name)
    # return "<p>hello, world<p>"

if __name__ == '__main__':
    app.run(debug=True)