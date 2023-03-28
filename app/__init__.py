from flask import Flask

app = Flask("__name__")

# SqlAlchemy Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appdata.db'
# Secret Key
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to see"

from .routes import *
from .models import *

if __name__ == '__main__':
    app.run()