from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.controllers import user_controller
from flask_app.models import user_model



@app.route('/')
def index():
    users=user_model.Users.get_all()
    print(users)
    return render_template('index.html', users=users)

@app.route('/add/user')
def add_user():
    return render_template('add_user.html')

@app.route('/proccessing/form', methods=['POST'])
def proccessing_form():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
        }
    print('====== made it here processing/form   =======')
    user_model.Users.create_user(data)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data={
        'id':id
    }
    print('<===== made it to delete route  ======>')
    user_model.Users.delete(data)
    return redirect('/')

@app.route('/update/form/<int:id>')
def update_form(id):
    data={
        'id':id
    }
    user_db=user_model.Users.one_by_id(data)
    print(user_db)
    print('<===== made it to update route  ======>')
    return render_template('update_user.html', one_user=user_db)

@app.route('/update/form/<int:id>', methods=['POST'])
def update_form_int(id):
    
    data={
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    user_db=user_model.Users.update(data)
    return redirect('/show/'+str(id))

@app.route('/show/<int:id>')
def show_user(id):
    data={
        'id':id
    }
    user_db=user_model.Users.one_by_id(data)
    print('<===== made it to show_user route  ======>')
    return render_template('show_user.html', one_user=user_db)

if __name__=="__main__":
    app.run(debug=True)