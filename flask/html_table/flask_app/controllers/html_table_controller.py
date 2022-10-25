from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import users_model

@app.route('/')
def index():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html',users=users)




if __name__=="__main__":
    app.run(debug=True)