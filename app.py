from flask import Flask
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)



@app.route("/salve", methods=["GET"])
def salve():
    return "salve mundo"


if __name__ == "__main__":
    app.run(debug=True)
