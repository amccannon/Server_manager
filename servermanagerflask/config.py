import os
from flask_sqlalchemy import SQLAlchemy


#for important key
class Config(object):
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"



# regarding SQL