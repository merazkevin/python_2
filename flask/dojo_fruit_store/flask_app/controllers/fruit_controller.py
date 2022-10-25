from flask_app import app
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    fruits_quantities = [
    {'fruit' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html',fruits_quantities=fruits_quantities)





if __name__=="__main__":
    app.run(debug=True)