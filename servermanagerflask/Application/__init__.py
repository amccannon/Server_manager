# Flask Application Testing
# 12/14/2021
# Antonino Abeshi

# now we have access to the flask application

from flask import Flask

# current application or module being rendered
app = Flask(__name__)

# this can be the root directory (decorators using these different types of urls)

# importing routes from Application
from Application import routes