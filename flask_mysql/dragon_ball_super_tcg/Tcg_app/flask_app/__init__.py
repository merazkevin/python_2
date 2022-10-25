from flask import  Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "root"
DATABASE="dbs_scg_missing_card_list"

bcrypt = Bcrypt(app) 