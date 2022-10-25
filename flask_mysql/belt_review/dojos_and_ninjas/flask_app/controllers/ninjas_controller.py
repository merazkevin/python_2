from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.controllers import ninjas_controller, dojos_controller
from flask_app.models.ninjas_model import Ninjas
from flask_app.models.dojos_model import Dojos




@app.route('/add/ninja')
def add_ninja():
    all_dojos_db=Dojos.get_all_dojos()
    all_ninjas_db=Ninjas.get_all_ninjas()
    return render_template('add_ninja.html', all_ninjas=all_ninjas_db, all_dojos=all_dojos_db)

@app.route('/add/ninja/process/form', methods=["POST"])
def ninja_process_form():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    all_ninjas_db= Ninjas.create_ninja(data)
    print(all_ninjas_db)
    print('<=======you made it after create ninjas=======>')
    return redirect("/")

