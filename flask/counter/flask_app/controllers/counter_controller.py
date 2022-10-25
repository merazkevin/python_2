from flask_app import app
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html')

@app.route('/add',  methods=['POST'])
def add2Visits():
    session['counter']+=1
    print(request.form)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_count():
    session.clear()
    print(request.form)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)