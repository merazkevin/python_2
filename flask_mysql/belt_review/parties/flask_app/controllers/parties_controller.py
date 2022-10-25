from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.users_model import Users
from flask_app.models.party_model import Party


@app.route('/parties/new')
def new_party_form():
    return render_template('party_new.html')

@app.route('/parties/create', methods=['POST'])
def create_party():
    if 'uuid' not in session:
        return redirect('/')
    if not Party.validator(request.form):
        return redirect('/parties/new')
    data={
        **request.form,
        'user_id': session['uuid']
    }
    Party.create_party(data)
    return redirect('/user/dashboard')

@app.route('/parties/<int:id>')
def one_party(id):
    if 'uuid' not in session:
        return redirect('/')
    this_party=Party.get_one_id({'id':id})
    return render_template('view_party.html', this_party=this_party)