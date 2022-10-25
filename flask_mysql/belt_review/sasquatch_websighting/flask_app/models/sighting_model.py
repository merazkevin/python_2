from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import users_model

class Sighting:
    def __init__(self,data):
        self.id=data['id']
        self.location=data['location']
        self.what_happened=data['what_happened']
        self.date_of_sighting=data['date_of_sighting']
        self.number_of_sasquatch=data['number_of_sasquatch']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']

#<---. CLASSMETHODS --->
    @classmethod
    def create_sighting(cls, data):
        query="""
        INSERT INTO sightings (location, what_happened, date_of_sighting, number_of_sasquatch, user_id) VALUES( %(location)s, %(what_happened)s, %(date_of_sighting)s, %(number_of_sasquatch)s, %(user_id)s);
        """
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results

    @classmethod
    def delete_sighting(cls, data):
        query="DELETE FROM sightings WHERE id= %(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results

    @classmethod
    def update_sighting(cls, data):
        query="UPDATE sightings SET location = %(location)s, what_happened= %(what_happened)s, date_of_sighting=%(date_of_sighting)s, number_of_sasquatch=%(number_of_sasquatch)s WHERE id=%(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query="SELECT*FROM sightings JOIN users ON sightings.user_id=users.id;"
        results=connectToMySQL(DATABASE).query_db(query)
        if len(results)>0:
            all_sightings=[]
            for row in results:
                this_sighting=cls(row)
                user_data={
                    **row,
                    'id':row['users.id'],
                    'created_at':row['users.created_at'],
                    'updated_at':row['users.updated_at']
                }
                this_user=users_model.Users(user_data)
                this_sighting.witness=this_user
                all_sightings.append(this_sighting)
            return all_sightings
        return []

    @classmethod
    def get_one_id(cls,data):
        query="SELECT*FROM sightings JOIN users ON sightings.user_id=users.id WHERE sightings.id=%(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        row=results[0]
        this_sightings=cls(row)
        user_data={
            **row,
            'id':row['users.id'],
            'created_at':row['users.created_at'],
            'updated_at':row['users.updated_at']
        }
        this_user=users_model.Users(user_data)
        this_sightings.witness=this_user
        return this_sightings

    @staticmethod
    def validator(form_data):
        is_valid=True
        if len(form_data['location'])<1:
            flash('Location required')
            is_valid=False
        if len(form_data['what_happened'])<1:
            flash('what_happened required')
            is_valid=False
        if len(form_data['date_of_sighting'])<1:
            flash('date_of_sighting required')
            is_valid=False
        if 'number_sasquatch' not in form_data:
            # flash('number_sasquatch required')
            # is_valid=False
            pass
        return is_valid
