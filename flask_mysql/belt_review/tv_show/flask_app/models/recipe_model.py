from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session
from flask_app.models import user_model

class Recipe:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instruction=data['instruction']
        self.under_30=data['under_30']
        self.user_id=data['user_id']

    #<-- Classmethods -->
    @classmethod
    def create_recipe(cls,data):
        print(data)
        query="INSERT INTO recipe(name, description, instruction, under_30, user_id) VALUES(%(name)s, %(description)s, %(instruction)s, %(under_30)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def left_get_all(cls,data):
        query="SELECT * FROM user JOIN recipe ON recipe.user_id=user.id;"
        results=connectToMySQL(DATABASE).query_db(query,data)
        this_user=cls(results[0])
        print(results)
        all_recipies=[]
        for each_row in results:
            recipe_data={**each_row}
        recipe_instance=Recipe(recipe_data)
        all_recipies.append(recipe_instance)
        this_user.posted_by=all_recipies
        return all_recipies

    @classmethod
    def get_all(cls,recipe_data):
        query="SELECT * FROM recipe;"
        results=connectToMySQL(DATABASE).query_db(query,recipe_data)
        return results
        



