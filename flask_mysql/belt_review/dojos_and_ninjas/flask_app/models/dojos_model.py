from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import ninjas_model

class Dojos:
    def __init__(self, data):
        self.name=data['name']


#<---. CLASSMETHODS --->
    @classmethod
    def get_all_dojos(cls):
        query="SELECT*FROM dojos;"
        results=connectToMySQL(DATABASE).query_db(query)
        return results

    @classmethod
    def create_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES(%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def one_by_id(cls,data):
        query= "SELECT*FROM users WHERE id=%(id)s;"
        ninja_id=connectToMySQL(DATABASE).query_db(query,data)
        return ninja_id[0]

    @classmethod#<-- Left Join-->
    def get_one_dojo_with_ninjas(cls,data): 
        query="""
        SELECT * FROM dojos 
        left JOIN ninjas 
        ON dojos.id = dojo_id
        WHERE dojos.id=%(id)s;
        """
        results=connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        this_dojo=cls(results[0])
        all_ninjas=[]
        for each_row in results:
            ninja_data={
                'id': each_row['ninjas.id'],
                'first_name':each_row['first_name'],
                'last_name': each_row['last_name'],
                'age': each_row['age'],
                'created_at':each_row['ninjas.created_at'],
                'updated_at':each_row['ninjas.updated_at'],
                'dojo_id': each_row['dojo_id']
            }
            ninja_instance=ninjas_model.Ninjas(ninja_data)
            all_ninjas.append(ninja_instance)
        this_dojo.ninjas=all_ninjas
        return this_dojo