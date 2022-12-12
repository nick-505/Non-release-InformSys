from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import routes, models
""" from flask_login import LoginManager """

app = Flask("__name__")

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:beefymoo@localhost:3306/mydb'
db = SQLAlchemy(app)

""" # Логин
login = LoginManager(app)
 """

if __name__ == '__main__':
    app.run()