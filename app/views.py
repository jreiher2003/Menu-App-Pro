from app import app,db # pragma: no cover
from app.models import Place, Menu # pragma: no cover
from flask import render_template # pragma: no cover

@app.route("/") 
def index(): 
	all_places = Place.query.all()
	return render_template('index.html', all_places=all_places)

@app.route("/<int:place_id>/<path:place_name>/")
def place_menu(place_id,place_name):
	menuitems = Menu.query.filter(Menu.place_id == place_id).all()
	return render_template("menu.html", menuitems=menuitems)