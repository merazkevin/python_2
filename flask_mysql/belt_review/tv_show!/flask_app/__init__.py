from flask import  Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "root"
DATABASE="tv_shows!"

bcrypt = Bcrypt(app) 