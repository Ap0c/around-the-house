# ----- Imports ----- #

from flask import Flask
import os.path
from db import Database


# ----- Setup ----- #

# The database schema file.
DB_SCHEMA = os.path.join(os.path.dirname(os.path.realpath(__file__)),
	'schema.sql')

# The database file.
DB_FILE = 'media.db'

# The flask app object.
app = Flask(__name__)

# Handles database connections and queries.
db = Database(DB_FILE, DB_SCHEMA)


# ----- Routes ----- #

@app.route('/')
def home():
	return 'Hello world'


@app.route('/<id>')
def book(id):

	return "Hello, I'm a book with the id {}".format(id)


# ----- Run ----- #

if __name__ == '__main__':
	app.run(debug=True)
