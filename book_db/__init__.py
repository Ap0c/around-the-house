# ----- Imports ----- #

from flask import Flask


# ----- Init ----- #

# The flask app object.
app = Flask(__name__)

import book_db.views
