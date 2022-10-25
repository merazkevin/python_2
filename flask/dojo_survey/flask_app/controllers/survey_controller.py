from flask_app import app
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data={
    'name':request.form['name'],
    'location':request.form['location'],
    'language':request.form['language'],
    'comments':request.form['comments'],
    }
    session['data']=data
    return redirect('/show/info')

@app.route('/show/info')
def show_info():
    return render_template('show_info.html')

if __name__=="__main__":
    app.run(debug=True)