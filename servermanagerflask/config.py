import os


#for important key
class Config(object):
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"
