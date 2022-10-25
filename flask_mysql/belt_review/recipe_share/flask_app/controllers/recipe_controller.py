from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.controllers import user_controller
from flask_app.models.user_model import User 
from flask_app.models.recipe_model import Recipe

@app.route('/add/recipe')
def add_recipe():
    return render_template('add_recipe.html')

@app.route('/processing/add/recipe', methods=['POST'])
def processing_add_recipe():
    data={
        'name':request.form['name'],
        'description':request.form['description'],
        'instruction':request.form['instruction'],
        'under_30':request.form['under_30'],
        'user_id':session['uuid']
        }
    print('<=== you made it to processing recipe ===>')
    Recipe.create_recipe(data)
    return redirect('/user/dashboard')
