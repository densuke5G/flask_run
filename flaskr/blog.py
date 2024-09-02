from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr import db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    posts = db.select_posts()

    return render_template('blog/index.html', posts=posts)