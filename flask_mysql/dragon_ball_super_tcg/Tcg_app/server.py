from flask_app import app
from flask_app.controllers import missing_card_controller, users_controller




if __name__=="__main__":
    app.run(debug=True)