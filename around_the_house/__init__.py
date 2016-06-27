# ----- Imports ----- #

from flask import Flask


# ----- Init ----- #

# The flask app object.
app = Flask(__name__)

import around_the_house.views
