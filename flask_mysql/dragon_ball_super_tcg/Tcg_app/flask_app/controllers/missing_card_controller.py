from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models.missing_card_model import Mcard
from flask_app.controllers import users_controller
from flask_app.models.users_model import Users

@app.route('/card/add')
def register_login_page():
    return render_template('add_card.html')

@app.route('/add/card/processing', methods=['POST'])
def add_card():
    card_data={
        **request.form,
        'user_id': session['uuid']
    }
    Mcard.create_card(card_data)
    print('<===== made it to add_card route *session ======>')
    return redirect('/user/dashboard')