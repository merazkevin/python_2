from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash,session

class Mcard:
    def __init__(self,data):
        self.id=data['id']
        self.card_set=data['card_set']
        self.name=data['name']
        self.color=data['color']
        self.rarity=data['rarity']
        self.user_id=data['user_id']

    #<--- classmethods --->
    @classmethod
    def create_card(cls,data):
        query="INSERT INTO missing_cards_list (card_set, name, color, rarity, user_id) VALUES(%(card_set)s, %(name)s, %(color)s, %(rarity)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data)

    @classmethod
    def delete(cls,data):
        query= "DELETE FROM missing_cards_list WHERE id=%(id)s;"
        return  connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM dbs_scg_missing_card_list.missing_cards_list;"
        return  connectToMySQL(DATABASE).query_db(query)