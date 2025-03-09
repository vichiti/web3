from flask import Blueprint, render_template, session, redirect, url_for
from app.db import User

auth_bp = Blueprint('auth', __name__, template_folder='../../templates/auth')

@auth_bp.route('/dashboard')
def dashboard():
    if 'account_id' not in session:
        return redirect(url_for('hedera.connect'))

    user = User.query.get(session['account_id'])
    return render_template('dashboard.html', account_id=user.account_id, email=user.email)