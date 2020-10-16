from app import app
from db_setup import init_db, db_session
from forms import GPUSearchForm
from flask import flash, render_template, request, redirect
from models import Price
from flask_table import table
from main1 import *
from flask.app import Flask
from bs4.builder._html5lib import e


init_db()
main1()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    search = GPUSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Price)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', table=table)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)