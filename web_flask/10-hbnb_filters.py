#!/usr/bin/python3
"""
starts a Flask web application
"""
<<<<<<< HEAD
from flask import Flask, render_template

from models import *
from models import storage


=======

from flask import Flask, render_template
from models import *
from models import storage
>>>>>>> 9ee7170cd4aadc7d91f36c20bfd5a1fbcebd07f8
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

<<<<<<< HEAD

=======
>>>>>>> 9ee7170cd4aadc7d91f36c20bfd5a1fbcebd07f8
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
