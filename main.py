from flask import Flask, render_template

app = Flask(__name__)

from flaskr.db import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_world():
    message = "Hello, World!"
    name = "Daisuke"
    return render_template('hello_world.html', name = name)
    # return "<p>hello, world<p>"

if __name__ == '__main__':
    app.run(debug=True)