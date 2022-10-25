from flask import  Flask 
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "root"
DATABASE="dojos_and_ninjas_schema"

bcrypt = Bcrypt(app) 