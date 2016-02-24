from app import app,db # pragma: no cover
from app.models import Place # pragma: no cover
from flask import render_template # pragma: no cover

@app.route('/') 
def index(): 
	all_places = Place.query.all()
	return render_template('index.html', all_places=all_places)