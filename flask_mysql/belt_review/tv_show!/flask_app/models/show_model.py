from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import user_model

class Show:
    def __init__(self, data):
        self.id=data['id']
        self.title=data['title']
        self.network=data['network']
        self.release_date=data['release_date']
        self.description=data['description']
        self.user_id=data['user_id']

    #<-- Classmethods -->
    @classmethod
    def create_show(cls,data):
        print(data)
        query="INSERT INTO shows(title, network, release_date, description, user_id) VALUES(%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def left_get_all(cls,data):
        query="SELECT * FROM users JOIN shows ON shows.user_id=users.id;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        this_user=Show(results[0])
        print(results)
        all_shows=[]
        for each_row in results:
            show_data={**each_row}
        show_instance=cls(show_data)
        all_shows.append(show_instance)
        this_user.posted_by=all_shows
        return all_shows

    @classmethod
    def left_get_one(cls,data):
        query="SELECT * FROM users JOIN shows ON shows.user_id=users.id WHERE shows.id=%(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        row=results[0]
        this_show=Show(row)
        user_data={
            **row,
            'id':row['users.id'],
            'created_at':row['users.created_at'],
            'updated_at':row['users.updated_at']
        }
        this_user=user_model.User(user_data)
        this_show.posted_by=this_user
        return this_show

    @classmethod
    def get_all(cls,shows_data):
        query="SELECT * FROM shows;"
        results=connectToMySQL(DATABASE).query_db(query,shows_data)
        return results
        



