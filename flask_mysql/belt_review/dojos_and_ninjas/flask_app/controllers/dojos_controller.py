from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.controllers import ninjas_controller
from flask_app.models import ninjas_model, dojos_model

@app.route('/')
def index():
    print('<===== made it to index route  ======>')
    all_dojos_db=dojos_model.Dojos.get_all_dojos()
    print(all_dojos_db)
    return render_template('index.html', all_dojos=all_dojos_db)


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data={
        
        'name':request.form['name']
    }
    print(data)
    print('<===== made it to create_dojo route  ======>')
    dojos_model.Dojos.create_dojo(data)
    return redirect('/')

@app.route('/show/dojos/ninjas/<int:id>')
def show_dojos_ninjas(id):
    data={
        'id':id
    }
    print('<=======you made it after get on dojo wit ninjas=======>')
    all_dojos_and_ninjas=dojos_model.Dojos.get_one_dojo_with_ninjas(data)
    return render_template('show_dojo.html', one_dojo_with_ninjas=all_dojos_and_ninjas)








if __name__=="__main__":
    app.run(debug=True)