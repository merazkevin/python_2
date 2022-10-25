from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session



class Users:
    def __init__(self,data):
        self.first_name=data['first_name'],
        self.last_name=data['last_name'],
        self.email=data['email'],
        self.created_at=data['created-at'],
        self.updated_at=data['updated_at']


# <--- CLASSMETHODS --->
    @classmethod
    def get_all(cls):
        query = "select * from users;"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def one_by_id(cls,data):
        query= "SELECT*FROM users WHERE id=%(id)s;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results[0]


    @classmethod
    def create_user(cls, data): 
        query="INSERT INTO users (first_name,last_name,email) VALUES(%(first_name)s, %(last_name)s, %(email)s );"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query="DELETE FROM users WHERE id=(%(id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def update(cls, data):
        query= "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s  WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

# UPDATE
# "UPDATE table_name SET COLUMN_NAM=%{FORM_NAME}s"
