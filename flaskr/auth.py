import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr import db
from orm import models

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/auth')
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # db = init_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        
        if error is None:
            try:
                db.regist_user(username, password)
            except Exception:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
                
        flash(error)

    return render_template('auth/register.html')