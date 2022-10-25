#!/usr/bin/python3
"""
starts a Flask web application
"""
<<<<<<< HEAD
from flask import Flask


=======

from flask import Flask
>>>>>>> 9ee7170cd4aadc7d91f36c20bfd5a1fbcebd07f8
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

<<<<<<< HEAD

=======
>>>>>>> 9ee7170cd4aadc7d91f36c20bfd5a1fbcebd07f8
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
