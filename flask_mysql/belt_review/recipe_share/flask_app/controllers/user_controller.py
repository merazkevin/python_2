from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/user/dashboard')
    print('<===== made it to index route  ======>')
    return render_template('index.html')

@app.route('/processing/user/form', methods=['POST'])
def create_user():
    if not User.register_validator(request.form):
        return redirect('/')
    # <----password_hash--->
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    print(password_hash)
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':password_hash
    }
    
    id=User.create_user(data)
    session['uuid']=id
    print('<===== made it to create_user route *session ======>')
    return redirect('/')

@app.route('/login/user/processing', methods=['POST'])
def validate_login():
    if not User.login_validator(request.form):
        return redirect('/')
    data={
        'email':request.form['email'],
        'password':request.form['password']
    }
    user_in_db=User.get_one_by_email(data)
    if not user_in_db:
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    else:
        session['uuid']= user_in_db.id
    print('<===== made it to create_user route  ======>')
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    data={**request.form}
    recipe_data={**request.form}
    users_with_recipe_data={**request.form}
    all_users_in_db=User.get_all_user(data)
    all_recipies_db=Recipe.get_all(recipe_data)
    users_with_recipe=Recipe.left_get_all(users_with_recipe_data)
    print(users_with_recipe)
    return render_template('user_dashboard.html', all_recipies=all_recipies_db, all_users=all_users_in_db, users_with_recipe=users_with_recipe)

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)