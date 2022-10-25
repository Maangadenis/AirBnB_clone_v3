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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

<<<<<<< HEAD

=======
>>>>>>> 9ee7170cd4aadc7d91f36c20bfd5a1fbcebd07f8
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
