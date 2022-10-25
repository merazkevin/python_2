from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session

class Ninjas:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.age=data['age']
        self.dojo_id=data['dojo_id']

#<---. CLASSMETHODS --->
    @classmethod
    def get_all_ninjas(cls):
        query="SELECT*FROM ninjas;"
        results=connectToMySQL(DATABASE).query_db(query)
        return results

    @classmethod
    def get_one_ninja(cls, data):
        query= "SELECT*FROM ninjas WHERE id=%(id)s"
        results=connectToMySQL(DATABASE).query_db(query)
        return results

    @classmethod
    def create_ninja(cls,data):
        query="INSERT INTO ninjas (first_name,last_name,age, dojo_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        all_ninjas_db=connectToMySQL(DATABASE).query_db(query,data)
        return all_ninjas_db