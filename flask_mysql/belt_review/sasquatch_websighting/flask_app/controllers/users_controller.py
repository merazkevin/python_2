from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.users_model import Users
from flask_app.models.sighting_model import Sighting


@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/user/dashboard')
    print('<===== made it to index route  ======>')
    return render_template('index.html')

@app.route('/register/user/processing', methods=['POST'])
def create_user():
    if not Users.register_validator(request.form):
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
    
    id=Users.create_user(data)
    session['uuid']=id
    print('<===== made it to create_user route *session ======>')
    return redirect('/')

@app.route('/login/user/processing', methods=['POST'])
def validate_login():
    if not Users.login_validator(request.form):
        return redirect('/')
    data={
        **request.form,
        'email':request.form['email'],
        'password':request.form['password']
    }
    user_in_db=Users.get_one_by_email(data)
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
    user_data={
        **request.form,
        'id': session['uuid']
        }
    logged_user=Users.get_one_by_id(user_data)
    all_sightings=Sighting.get_all()
    return render_template('dashboard.html', logged_user=logged_user, all_sightings=all_sightings)

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)