from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.users_model import Users
from flask_app.models.sighting_model import Sighting


@app.route('/sightings/new')
def new_sighting_form():
    return render_template('sighting_new.html')

@app.route('/sightings/create', methods=['POST'])
def create_sighting():
    if 'uuid' not in session:
        return redirect('/')
    if not Sighting.validator(request.form):
        return redirect('/sightings/new')
    data={
        **request.form,
        'user_id': session['uuid']
    }
    Sighting.create_sighting(data)
    return redirect('/user/dashboard')


@app.route('/sightings/<int:id>')
def one_sighting(id):
    if 'uuid' not in session:
        return redirect('/')
    user_data={
        **request.form,
        'id': session['uuid']
        }
    logged_user=Users.get_one_by_id(user_data)
    this_sighting=Sighting.get_one_id({'id':id})
    return render_template('view_sighting.html', this_sighting=this_sighting, logged_user=logged_user)

@app.route('/sightings/<int:id>/edit')
def sightings_edit(id):
    if 'uuid' not in session:
        return redirect('/')
    this_sighting=Sighting.get_one_id({'id':id})
    return render_template('sighting_edit.html',this_sighting=this_sighting)

@app.route('/sightings/<int:id>/update', methods=['POST'])
def sightings_update(id):
    if 'uuid' not in session:
        return redirect('/')
    if not Sighting.validator(request.form):
        return redirect(f'/sightings/{id}/edit')
    data={
        **request.form,
        'id':id
    }
    Sighting.update_sighting(data)
    return redirect('/user/dashboard')

@app.route('/sightings/<int:id>/delete')
def delete_sighting(id):
    if 'uuid' not in session:
        return redirect('/')
    data={
        **request.form,
        'id':id
    }
    Sighting.delete_sighting(data)
    return redirect('/user/dashboard')