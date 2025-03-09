from flask import Blueprint, render_template, request, session, redirect, url_for
from app.hedera.blockchain import get_counter, increment_counter
from app.config import Config
from app.db import db, User

hedera_bp = Blueprint('hedera', __name__, template_folder='../../templates')

@hedera_bp.route('/connect')
def connect():
    hashconnect_data = Config.HASHCONNECT_DATA
    return render_template('hedera/connect.html', hashconnect_data=hashconnect_data)

@hedera_bp.route('/set-account', methods=['POST'])
def set_account():
    data = request.get_json()
    account_id = data['account_id']
    session['account_id'] = account_id

    # Check if user exists in DB, create if not
    user = User.query.get(account_id)
    if not user:
        user = User(account_id=account_id, email=None)  # Add email later if needed
        db.session.add(user)
        db.session.commit()

    return '', 204

@hedera_bp.route('/counter', methods=['GET', 'POST'])
def counter():
    if 'account_id' not in session:
        return redirect(url_for('hedera.connect'))

    contract_id = Config.CONTRACT_ID
    current_value = get_counter(contract_id)

    if request.method == 'POST':
        tx_id = increment_counter(contract_id)
        current_value = get_counter(contract_id)
        return render_template('counter.html', current_value=current_value, tx_id=tx_id)

    return render_template('hedera/counter.html', current_value=current_value)