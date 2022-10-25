from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.controllers import user_controller
from flask_app.models.user_model import User 
from flask_app.models.show_model import Show

@app.route('/add/show')
def add_recipe():
    return render_template('add_show.html')

@app.route('/processing/add/show', methods=['POST'])
def processing_add_show():
    data={
        'title':request.form['title'],
        'network':request.form['network'],
        'release_date':request.form['release_date'],
        'description':request.form['description'],
        'user_id':session['uuid']
        }
    print('<=== you made it to processing recipe ===>')
    Show.create_show(data)
    return redirect('/user/dashboard')
