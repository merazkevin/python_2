from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 




class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']

#<---. CLASSMETHODS --->
    @classmethod
    def create_user(cls, data):
        query="""
        INSERT INTO users(first_name, last_name, email, password) VALUES( %(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        return cls(results[0])

#<---. STATICMETHODS --->
    @staticmethod
    def register_validator(potential_user):
        is_valid= True
        #<--first_name-->
        if len(potential_user['first_name'])<1:
            is_valid=False
            flash('first name requires 1 character')
        #<--last_name-->
        if len(potential_user['last_name'])<1:
            is_valid=False
            flash('last name requires 1 character')
        #<--email-->
        if len(potential_user['email'])<1:
            is_valid=False
            flash('email requires 1 character')
        
        if not EMAIL_REGEX.match(potential_user['email']): 
            flash("Invalid email address!")
            is_valid = False
        else:
            data={
                'email':potential_user['email']
            }
            user_in_db=Users.get_one_by_email(data)
            if user_in_db:
                is_valid=False
                flash('invalid email')
        #<--password-->
        if len(potential_user['password'])<1:
            is_valid=False
            flash('password requires 1 character')
        #<--confirm_password-->
        if len(potential_user['confirm_password'])<1 and potential_user['confirm_password']== potential_user['confirm_password']:
            is_valid=False
            flash('confirm password does not match password')
        return is_valid

    @staticmethod
    def login_validator(potential_user):
        is_valid= True
        #<--email-->
        if len(potential_user['email'])<1:
            is_valid=False
            flash('email requires 1 character')
        if not EMAIL_REGEX.match(potential_user['email']): 
            flash("Invalid email address!")
            is_valid = False
        #<--password-->
        if len(potential_user['password'])<1:
            is_valid=False
            flash('password requires 1 character')
        return is_valid

