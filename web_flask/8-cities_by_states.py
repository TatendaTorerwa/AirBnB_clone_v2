#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/cities_bt_states', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda p: p.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
